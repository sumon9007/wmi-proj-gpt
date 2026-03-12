#!/usr/bin/env python3
from __future__ import annotations

import shutil
import sys
import tempfile
import zipfile
from pathlib import Path
import xml.etree.ElementTree as ET


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
DOC_REL_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"
PIC_NS = "http://schemas.openxmlformats.org/drawingml/2006/picture"
WP_NS = "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
CONTENT_NS = "http://schemas.openxmlformats.org/package/2006/content-types"

ET.register_namespace("w", W_NS)
ET.register_namespace("", REL_NS)


def qn(ns: str, tag: str) -> str:
    return f"{{{ns}}}{tag}"


def ensure_child(parent: ET.Element, ns: str, tag: str, attrs: dict[str, str] | None = None) -> ET.Element:
    child = parent.find(qn(ns, tag))
    if child is None:
        child = ET.SubElement(parent, qn(ns, tag), attrs or {})
    elif attrs:
        child.attrib.update(attrs)
    return child


def set_table_borders(tbl_pr: ET.Element, color: str, size: str = "8") -> None:
    borders = ensure_child(tbl_pr, W_NS, "tblBorders")
    for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = ensure_child(borders, W_NS, side)
        el.set(qn(W_NS, "val"), "single")
        el.set(qn(W_NS, "sz"), size)
        el.set(qn(W_NS, "space"), "0")
        el.set(qn(W_NS, "color"), color)


def set_cell_shading(cell: ET.Element, fill: str) -> None:
    tc_pr = ensure_child(cell, W_NS, "tcPr")
    shd = ensure_child(tc_pr, W_NS, "shd")
    shd.set(qn(W_NS, "val"), "clear")
    shd.set(qn(W_NS, "color"), "auto")
    shd.set(qn(W_NS, "fill"), fill)


def set_paragraph_alignment(paragraph: ET.Element, value: str) -> None:
    ppr = ensure_child(paragraph, W_NS, "pPr")
    jc = ensure_child(ppr, W_NS, "jc")
    jc.set(qn(W_NS, "val"), value)


def set_run_color(paragraph: ET.Element, color: str, bold: bool | None = None) -> None:
    for run in paragraph.findall(qn(W_NS, "r")):
        rpr = ensure_child(run, W_NS, "rPr")
        color_el = ensure_child(rpr, W_NS, "color")
        color_el.set(qn(W_NS, "val"), color)
        if bold is not None:
            b = ensure_child(rpr, W_NS, "b")
            if not bold:
                b.set(qn(W_NS, "val"), "0")


def image_dimensions(px_w: int, px_h: int, target_width_in: float) -> tuple[int, int]:
    emu_per_in = 914400
    width = int(target_width_in * emu_per_in)
    height = int(width * px_h / px_w)
    return width, height


def build_inline_image(rid: str, name: str, descr: str, cx: int, cy: int, docpr_id: int, pic_id: int) -> ET.Element:
    drawing = ET.Element(qn(W_NS, "drawing"))
    inline = ET.SubElement(drawing, qn(WP_NS, "inline"))
    ET.SubElement(inline, qn(WP_NS, "extent"), {"cx": str(cx), "cy": str(cy)})
    ET.SubElement(inline, qn(WP_NS, "effectExtent"), {"l": "0", "t": "0", "r": "0", "b": "0"})
    ET.SubElement(inline, qn(WP_NS, "docPr"), {"id": str(docpr_id), "name": name, "descr": descr})
    c_nv = ET.SubElement(inline, qn(WP_NS, "cNvGraphicFramePr"))
    ET.SubElement(c_nv, qn(A_NS, "graphicFrameLocks"), {"noChangeAspect": "1"})
    graphic = ET.SubElement(inline, qn(A_NS, "graphic"))
    graphic_data = ET.SubElement(graphic, qn(A_NS, "graphicData"), {"uri": PIC_NS})
    pic = ET.SubElement(graphic_data, qn(PIC_NS, "pic"))
    nv_pic_pr = ET.SubElement(pic, qn(PIC_NS, "nvPicPr"))
    ET.SubElement(nv_pic_pr, qn(PIC_NS, "cNvPr"), {"id": str(pic_id), "name": name, "descr": descr})
    c_nv_pic_pr = ET.SubElement(nv_pic_pr, qn(PIC_NS, "cNvPicPr"))
    ET.SubElement(c_nv_pic_pr, qn(A_NS, "picLocks"), {"noChangeAspect": "1", "noChangeArrowheads": "1"})
    blip_fill = ET.SubElement(pic, qn(PIC_NS, "blipFill"))
    ET.SubElement(blip_fill, qn(A_NS, "blip"), {qn(DOC_REL_NS, "embed"): rid})
    stretch = ET.SubElement(blip_fill, qn(A_NS, "stretch"))
    ET.SubElement(stretch, qn(A_NS, "fillRect"))
    sp_pr = ET.SubElement(pic, qn(PIC_NS, "spPr"), {"bwMode": "auto"})
    xfrm = ET.SubElement(sp_pr, qn(A_NS, "xfrm"))
    ET.SubElement(xfrm, qn(A_NS, "off"), {"x": "0", "y": "0"})
    ET.SubElement(xfrm, qn(A_NS, "ext"), {"cx": str(cx), "cy": str(cy)})
    ET.SubElement(sp_pr, qn(A_NS, "prstGeom"), {"prst": "rect"})
    return drawing


def paragraph_with_image(rid: str, name: str, descr: str, cx: int, cy: int, docpr_id: int, pic_id: int, align: str) -> ET.Element:
    p = ET.Element(qn(W_NS, "p"))
    ppr = ET.SubElement(p, qn(W_NS, "pPr"))
    ET.SubElement(ppr, qn(W_NS, "jc"), {qn(W_NS, "val"): align})
    r = ET.SubElement(p, qn(W_NS, "r"))
    r.append(build_inline_image(rid, name, descr, cx, cy, docpr_id, pic_id))
    return p


def make_header_xml(variant: str) -> bytes:
    root = ET.Element(qn(W_NS, "hdr"))
    tbl = ET.SubElement(root, qn(W_NS, "tbl"))
    tbl_pr = ET.SubElement(tbl, qn(W_NS, "tblPr"))
    ET.SubElement(tbl_pr, qn(W_NS, "tblW"), {qn(W_NS, "w"): "5000", qn(W_NS, "type"): "pct"})
    borders = ET.SubElement(tbl_pr, qn(W_NS, "tblBorders"))
    for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
        ET.SubElement(borders, qn(W_NS, side), {qn(W_NS, "val"): "nil"})
    grid = ET.SubElement(tbl, qn(W_NS, "tblGrid"))
    ET.SubElement(grid, qn(W_NS, "gridCol"), {qn(W_NS, "w"): "2500"})
    ET.SubElement(grid, qn(W_NS, "gridCol"), {qn(W_NS, "w"): "4500"})
    ET.SubElement(grid, qn(W_NS, "gridCol"), {qn(W_NS, "w"): "2000"})

    tr = ET.SubElement(tbl, qn(W_NS, "tr"))

    left = ET.SubElement(tr, qn(W_NS, "tc"))
    ET.SubElement(ET.SubElement(left, qn(W_NS, "tcPr")), qn(W_NS, "tcW"), {qn(W_NS, "w"): "1800", qn(W_NS, "type"): "pct"})
    left.append(paragraph_with_image("rId1", "Waymark Logo", "Waymark Infotech", *image_dimensions(187, 50, 1.35), 101, 201, "left"))

    middle = ET.SubElement(tr, qn(W_NS, "tc"))
    ET.SubElement(ET.SubElement(middle, qn(W_NS, "tcPr")), qn(W_NS, "tcW"), {qn(W_NS, "w"): "2200", qn(W_NS, "type"): "pct"})
    p1 = ET.SubElement(middle, qn(W_NS, "p"))
    p1pr = ET.SubElement(p1, qn(W_NS, "pPr"))
    ET.SubElement(p1pr, qn(W_NS, "jc"), {qn(W_NS, "val"): "center"})
    r1 = ET.SubElement(p1, qn(W_NS, "r"))
    r1pr = ET.SubElement(r1, qn(W_NS, "rPr"))
    ET.SubElement(r1pr, qn(W_NS, "b"))
    ET.SubElement(r1pr, qn(W_NS, "color"), {qn(W_NS, "val"): "17324D"})
    ET.SubElement(r1pr, qn(W_NS, "sz"), {qn(W_NS, "val"): "20"})
    ET.SubElement(r1pr, qn(W_NS, "szCs"), {qn(W_NS, "val"): "20"})
    ET.SubElement(r1, qn(W_NS, "t")).text = "Waymark Infotech"
    p2 = ET.SubElement(middle, qn(W_NS, "p"))
    p2pr = ET.SubElement(p2, qn(W_NS, "pPr"))
    ET.SubElement(p2pr, qn(W_NS, "jc"), {qn(W_NS, "val"): "center"})
    r2 = ET.SubElement(p2, qn(W_NS, "r"))
    r2pr = ET.SubElement(r2, qn(W_NS, "rPr"))
    ET.SubElement(r2pr, qn(W_NS, "color"), {qn(W_NS, "val"): "7A6A3A"})
    ET.SubElement(r2pr, qn(W_NS, "sz"), {qn(W_NS, "val"): "18"})
    ET.SubElement(r2pr, qn(W_NS, "szCs"), {qn(W_NS, "val"): "18"})
    ET.SubElement(r2, qn(W_NS, "t")).text = "GT/GPT/009/2026"

    right = ET.SubElement(tr, qn(W_NS, "tc"))
    ET.SubElement(ET.SubElement(right, qn(W_NS, "tcPr")), qn(W_NS, "tcW"), {qn(W_NS, "w"): "1000", qn(W_NS, "type"): "pct"})
    right.append(paragraph_with_image("rId2", "GPT Logo", "Gauteng Provincial Treasury", *image_dimensions(197, 153, 0.55), 102, 202, "right"))

    if variant == "draft":
        note = ET.SubElement(root, qn(W_NS, "p"))
        note_pr = ET.SubElement(note, qn(W_NS, "pPr"))
        ET.SubElement(note_pr, qn(W_NS, "jc"), {qn(W_NS, "val"): "center"})
        note_run = ET.SubElement(note, qn(W_NS, "r"))
        note_run_pr = ET.SubElement(note_run, qn(W_NS, "rPr"))
        ET.SubElement(note_run_pr, qn(W_NS, "color"), {qn(W_NS, "val"): "9C2F2F"})
        ET.SubElement(note_run_pr, qn(W_NS, "b"))
        ET.SubElement(note_run_pr, qn(W_NS, "sz"), {qn(W_NS, "val"): "16"})
        ET.SubElement(note_run_pr, qn(W_NS, "szCs"), {qn(W_NS, "val"): "16"})
        ET.SubElement(note_run, qn(W_NS, "t")).text = "Draft for internal review"

    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def make_cover_header_xml() -> bytes:
    root = ET.Element(qn(W_NS, "hdr"))
    p = ET.SubElement(root, qn(W_NS, "p"))
    ppr = ET.SubElement(p, qn(W_NS, "pPr"))
    ET.SubElement(ppr, qn(W_NS, "jc"), {qn(W_NS, "val"): "center"})
    r = ET.SubElement(p, qn(W_NS, "r"))
    rpr = ET.SubElement(r, qn(W_NS, "rPr"))
    ET.SubElement(rpr, qn(W_NS, "color"), {qn(W_NS, "val"): "C8A75B"})
    ET.SubElement(rpr, qn(W_NS, "sz"), {qn(W_NS, "val"): "18"})
    ET.SubElement(rpr, qn(W_NS, "szCs"), {qn(W_NS, "val"): "18"})
    ET.SubElement(r, qn(W_NS, "t")).text = "Biometric Authentication Proposal"
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def make_footer_xml(variant: str, first_page: bool) -> bytes:
    root = ET.Element(qn(W_NS, "ftr"))
    p = ET.SubElement(root, qn(W_NS, "p"))
    ppr = ET.SubElement(p, qn(W_NS, "pPr"))
    ET.SubElement(ppr, qn(W_NS, "tabs"))
    tabs = ppr.find(qn(W_NS, "tabs"))
    ET.SubElement(tabs, qn(W_NS, "tab"), {qn(W_NS, "val"): "right", qn(W_NS, "pos"): "9350"})
    ET.SubElement(ppr, qn(W_NS, "jc"), {qn(W_NS, "val"): "left"})

    left_label = "Draft Proposal" if variant == "draft" else "Submission Copy"
    if first_page:
        left_label = "Confidential" if variant == "final" else "Confidential Draft"

    r1 = ET.SubElement(p, qn(W_NS, "r"))
    r1pr = ET.SubElement(r1, qn(W_NS, "rPr"))
    ET.SubElement(r1pr, qn(W_NS, "color"), {qn(W_NS, "val"): "6B7280"})
    ET.SubElement(r1pr, qn(W_NS, "sz"), {qn(W_NS, "val"): "18"})
    ET.SubElement(r1pr, qn(W_NS, "szCs"), {qn(W_NS, "val"): "18"})
    ET.SubElement(r1, qn(W_NS, "t")).text = left_label

    if not first_page:
        ET.SubElement(p, qn(W_NS, "r")).append(ET.Element(qn(W_NS, "tab")))
        r2 = ET.SubElement(p, qn(W_NS, "r"))
        r2pr = ET.SubElement(r2, qn(W_NS, "rPr"))
        ET.SubElement(r2pr, qn(W_NS, "color"), {qn(W_NS, "val"): "6B7280"})
        ET.SubElement(r2pr, qn(W_NS, "sz"), {qn(W_NS, "val"): "18"})
        ET.SubElement(r2pr, qn(W_NS, "szCs"), {qn(W_NS, "val"): "18"})
        ET.SubElement(r2, qn(W_NS, "t")).text = "Page "
        ET.SubElement(ET.SubElement(p, qn(W_NS, "r")), qn(W_NS, "fldChar"), {qn(W_NS, "fldCharType"): "begin"})
        instr_run = ET.SubElement(p, qn(W_NS, "r"))
        ET.SubElement(instr_run, qn(W_NS, "instrText"), {"{http://www.w3.org/XML/1998/namespace}space": "preserve"}).text = " PAGE "
        ET.SubElement(ET.SubElement(p, qn(W_NS, "r")), qn(W_NS, "fldChar"), {qn(W_NS, "fldCharType"): "separate"})
        ET.SubElement(ET.SubElement(p, qn(W_NS, "r")), qn(W_NS, "t")).text = "1"
        ET.SubElement(ET.SubElement(p, qn(W_NS, "r")), qn(W_NS, "fldChar"), {qn(W_NS, "fldCharType"): "end"})

    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def make_header_rels() -> bytes:
    root = ET.Element(qn(REL_NS, "Relationships"))
    ET.SubElement(root, qn(REL_NS, "Relationship"), {"Id": "rId1", "Type": f"{DOC_REL_NS}/image", "Target": "media/header-bidder-logo.png"})
    ET.SubElement(root, qn(REL_NS, "Relationship"), {"Id": "rId2", "Type": f"{DOC_REL_NS}/image", "Target": "media/header-customer-logo.png"})
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def add_header_footer(files: dict[str, bytes], variant: str) -> None:
    rels_root = ET.fromstring(files["word/_rels/document.xml.rels"])
    existing_ids = [int(el.get("Id")[3:]) for el in rels_root.findall(qn(REL_NS, "Relationship")) if el.get("Id", "").startswith("rId") and el.get("Id")[3:].isdigit()]
    next_id = max(existing_ids, default=8) + 1

    mapping = {
        "header1": f"rId{next_id}",
        "footer1": f"rId{next_id + 1}",
        "header2": f"rId{next_id + 2}",
        "footer2": f"rId{next_id + 3}",
    }
    parts = {
        "header1": ("header", "header1.xml"),
        "footer1": ("footer", "footer1.xml"),
        "header2": ("header", "header2.xml"),
        "footer2": ("footer", "footer2.xml"),
    }

    for key, (kind, target) in parts.items():
        ET.SubElement(
            rels_root,
            qn(REL_NS, "Relationship"),
            {"Id": mapping[key], "Type": f"{DOC_REL_NS}/{kind}", "Target": target},
        )
    files["word/_rels/document.xml.rels"] = ET.tostring(rels_root, encoding="utf-8", xml_declaration=True)

    doc_root = ET.fromstring(files["word/document.xml"])
    sect_pr = doc_root.find(f".//{qn(W_NS,'sectPr')}")
    if sect_pr is None:
        body = doc_root.find(qn(W_NS, "body"))
        sect_pr = ET.SubElement(body, qn(W_NS, "sectPr"))
    for child in list(sect_pr):
        if child.tag in (qn(W_NS, "headerReference"), qn(W_NS, "footerReference"), qn(W_NS, "titlePg")):
            sect_pr.remove(child)
    refs = [
        ET.Element(qn(W_NS, "headerReference"), {qn(DOC_REL_NS, "id"): mapping["header2"], qn(W_NS, "type"): "first"}),
        ET.Element(qn(W_NS, "footerReference"), {qn(DOC_REL_NS, "id"): mapping["footer2"], qn(W_NS, "type"): "first"}),
        ET.Element(qn(W_NS, "headerReference"), {qn(DOC_REL_NS, "id"): mapping["header1"], qn(W_NS, "type"): "default"}),
        ET.Element(qn(W_NS, "footerReference"), {qn(DOC_REL_NS, "id"): mapping["footer1"], qn(W_NS, "type"): "default"}),
    ]
    for idx, ref in enumerate(refs):
        sect_pr.insert(idx, ref)
    sect_pr.insert(len(refs), ET.Element(qn(W_NS, "titlePg")))
    pg_mar = ensure_child(sect_pr, W_NS, "pgMar")
    pg_mar.set(qn(W_NS, "header"), "708")
    pg_mar.set(qn(W_NS, "footer"), "708")
    files["word/document.xml"] = ET.tostring(doc_root, encoding="utf-8", xml_declaration=True)

    content_root = ET.fromstring(files["[Content_Types].xml"])
    existing_defaults = []
    for el in content_root.findall(qn(CONTENT_NS, "Default")):
        ext = el.get("Extension")
        ctype = el.get("ContentType")
        if ext and ctype and (ext, ctype) not in existing_defaults:
            existing_defaults.append((ext, ctype))
    if not any(ext == "png" for ext, _ in existing_defaults):
        existing_defaults.append(("png", "image/png"))

    existing_overrides = []
    seen_parts = set()
    for el in content_root.findall(qn(CONTENT_NS, "Override")):
        part = el.get("PartName")
        ctype = el.get("ContentType")
        if not part or not ctype:
            continue
        if part.startswith("/word/media/"):
            continue
        if part in seen_parts:
            continue
        seen_parts.add(part)
        existing_overrides.append((part, ctype))

    content_root.clear()
    for ext, ctype in existing_defaults:
        ET.SubElement(
            content_root,
            qn(CONTENT_NS, "Default"),
            {"Extension": ext, "ContentType": ctype},
        )
    for part, ctype in existing_overrides:
        ET.SubElement(
            content_root,
            qn(CONTENT_NS, "Override"),
            {"PartName": part, "ContentType": ctype},
        )
    overrides = {
        "/word/header1.xml": "application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml",
        "/word/footer1.xml": "application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml",
        "/word/header2.xml": "application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml",
        "/word/footer2.xml": "application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml",
    }
    for part_name, content_type in overrides.items():
        exists = any(el.get("PartName") == part_name for el in content_root.findall(qn(CONTENT_NS, "Override")))
        if not exists:
            ET.SubElement(content_root, qn(CONTENT_NS, "Override"), {"PartName": part_name, "ContentType": content_type})
    files["[Content_Types].xml"] = ET.tostring(content_root, encoding="utf-8", xml_declaration=True)

    files["word/header1.xml"] = make_header_xml(variant)
    files["word/footer1.xml"] = make_footer_xml(variant, first_page=False)
    files["word/header2.xml"] = make_cover_header_xml()
    files["word/footer2.xml"] = make_footer_xml(variant, first_page=True)
    files["word/_rels/header1.xml.rels"] = make_header_rels()
    files["word/media/header-bidder-logo.png"] = files["word/media/rId20.png"]
    files["word/media/header-customer-logo.png"] = files["word/media/rId23.png"]


def improve_styles(files: dict[str, bytes], variant: str) -> None:
    root = ET.fromstring(files["word/styles.xml"])
    for style in root.findall(qn(W_NS, "style")):
        style_id = style.get(qn(W_NS, "styleId"))
        if style_id == "Table":
            tbl_pr = ensure_child(style, W_NS, "tblPr")
            set_table_borders(tbl_pr, "D7DDE4", "6")
            cell_mar = ensure_child(tbl_pr, W_NS, "tblCellMar")
            for edge in ("top", "left", "bottom", "right"):
                el = ensure_child(cell_mar, W_NS, edge)
                el.set(qn(W_NS, "type"), "dxa")
                el.set(qn(W_NS, "w"), "120")
            for child in list(style.findall(qn(W_NS, "tblStylePr"))):
                if child.get(qn(W_NS, "type")) == "firstRow":
                    tc_pr = ensure_child(child, W_NS, "tcPr")
                    shd = ensure_child(tc_pr, W_NS, "shd")
                    shd.set(qn(W_NS, "val"), "clear")
                    shd.set(qn(W_NS, "fill"), "17324D")
                    shd.set(qn(W_NS, "color"), "auto")
                    rpr = ensure_child(child, W_NS, "rPr")
                    color = ensure_child(rpr, W_NS, "color")
                    color.set(qn(W_NS, "val"), "FFFFFF")
                    ensure_child(rpr, W_NS, "b")
                    break
        elif style_id == "Title":
            rpr = ensure_child(style, W_NS, "rPr")
            color = ensure_child(rpr, W_NS, "color")
            color.set(qn(W_NS, "val"), "17324D" if variant == "final" else "15304B")
        elif style_id == "Subtitle":
            rpr = ensure_child(style, W_NS, "rPr")
            color = ensure_child(rpr, W_NS, "color")
            color.set(qn(W_NS, "val"), "7A6A3A")
    files["word/styles.xml"] = ET.tostring(root, encoding="utf-8", xml_declaration=True)


def style_document_tables(files: dict[str, bytes], variant: str) -> None:
    root = ET.fromstring(files["word/document.xml"])
    body = root.find(qn(W_NS, "body"))
    tables = body.findall(qn(W_NS, "tbl"))
    if not tables:
        files["word/document.xml"] = ET.tostring(root, encoding="utf-8", xml_declaration=True)
        return

    logo_table = tables[0]
    tbl_pr = ensure_child(logo_table, W_NS, "tblPr")
    borders = ensure_child(tbl_pr, W_NS, "tblBorders")
    for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = ensure_child(borders, W_NS, side)
        el.set(qn(W_NS, "val"), "nil")
    jc = ensure_child(tbl_pr, W_NS, "jc")
    jc.set(qn(W_NS, "val"), "center")

    cover_border = "B8923D" if variant == "final" else "C8A75B"
    content_border = "CBD5E1" if variant == "final" else "D7DDE4"

    if len(tables) > 1:
        cover_table = tables[1]
        tbl_pr = ensure_child(cover_table, W_NS, "tblPr")
        set_table_borders(tbl_pr, cover_border, "10")
        jc = ensure_child(tbl_pr, W_NS, "jc")
        jc.set(qn(W_NS, "val"), "center")
        for cells in [row.findall(qn(W_NS, "tc")) for row in cover_table.findall(qn(W_NS, "tr"))]:
            if len(cells) >= 2:
                set_cell_shading(cells[0], "17324D")
                set_cell_shading(cells[1], "F8F6F0")
                for p in cells[0].findall(qn(W_NS, "p")):
                    set_paragraph_alignment(p, "left")
                    set_run_color(p, "FFFFFF", bold=True)
                for p in cells[1].findall(qn(W_NS, "p")):
                    set_paragraph_alignment(p, "left")
                    set_run_color(p, "20364A")

    for tbl in tables[2:]:
        tbl_pr = ensure_child(tbl, W_NS, "tblPr")
        set_table_borders(tbl_pr, content_border, "6")
        rows = tbl.findall(qn(W_NS, "tr"))
        if rows:
            for cell in rows[0].findall(qn(W_NS, "tc")):
                set_cell_shading(cell, "17324D")
                for p in cell.findall(qn(W_NS, "p")):
                    set_paragraph_alignment(p, "left")
                    set_run_color(p, "FFFFFF", bold=True)
            band_a = "FBFCFD" if variant == "draft" else "F7FAFC"
            band_b = "F3F6F8" if variant == "draft" else "EEF2F6"
            for row in rows[1:]:
                for idx, cell in enumerate(row.findall(qn(W_NS, "tc"))):
                    set_cell_shading(cell, band_a if idx % 2 == 0 else band_b)

    files["word/document.xml"] = ET.tostring(root, encoding="utf-8", xml_declaration=True)


def rewrite_docx(input_path: Path, output_path: Path, variant: str) -> None:
    with zipfile.ZipFile(input_path, "r") as source_zip:
        files = {name: source_zip.read(name) for name in source_zip.namelist()}

    improve_styles(files, variant)
    style_document_tables(files, variant)
    add_header_footer(files, variant)

    with tempfile.TemporaryDirectory() as tmp_dir:
        temp_out = Path(tmp_dir) / output_path.name
        with zipfile.ZipFile(temp_out, "w", compression=zipfile.ZIP_DEFLATED) as out_zip:
            for name, data in files.items():
                out_zip.writestr(name, data)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(temp_out, output_path)


def main() -> int:
    if len(sys.argv) not in (3, 4):
        print("Usage: polish-exported-docx.py <input.docx> <output.docx> [draft|final]")
        return 1

    variant = sys.argv[3] if len(sys.argv) == 4 else "draft"
    if variant not in {"draft", "final"}:
        print("Variant must be 'draft' or 'final'")
        return 1

    rewrite_docx(Path(sys.argv[1]), Path(sys.argv[2]), variant)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
