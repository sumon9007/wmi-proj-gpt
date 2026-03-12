#!/usr/bin/env python3
from __future__ import annotations

import shutil
import sys
import tempfile
import zipfile
from pathlib import Path
import xml.etree.ElementTree as ET


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
ET.register_namespace("w", W_NS)


def qn(tag: str) -> str:
    return f"{{{W_NS}}}{tag}"


def ensure_child(parent: ET.Element, tag: str) -> ET.Element:
    child = parent.find(qn(tag))
    if child is None:
        child = ET.SubElement(parent, qn(tag))
    return child


def set_paragraph_style(
    style: ET.Element,
    *,
    based_on: str | None = None,
    next_style: str | None = None,
    after: str | None = None,
    before: str | None = None,
    line: str | None = None,
    line_rule: str | None = None,
    jc: str | None = None,
    keep_next: bool = False,
    keep_lines: bool = False,
    page_break_before: bool = False,
    contextual_spacing: bool = False,
    outline_level: str | None = None,
    left: str | None = None,
    right: str | None = None,
    border_bottom_color: str | None = None,
    border_bottom_sz: str | None = None,
) -> None:
    if based_on:
        node = ensure_child(style, "basedOn")
        node.set(qn("val"), based_on)
    if next_style:
        node = ensure_child(style, "next")
        node.set(qn("val"), next_style)

    ppr = ensure_child(style, "pPr")
    spacing = ensure_child(ppr, "spacing")
    if after is not None:
        spacing.set(qn("after"), after)
    if before is not None:
        spacing.set(qn("before"), before)
    if line is not None:
        spacing.set(qn("line"), line)
    if line_rule is not None:
        spacing.set(qn("lineRule"), line_rule)
    if jc is not None:
        node = ensure_child(ppr, "jc")
        node.set(qn("val"), jc)
    if keep_next:
        ensure_child(ppr, "keepNext")
    if keep_lines:
        ensure_child(ppr, "keepLines")
    if page_break_before:
        ensure_child(ppr, "pageBreakBefore")
    if contextual_spacing:
        ensure_child(ppr, "contextualSpacing")
    if left is not None or right is not None:
        ind = ensure_child(ppr, "ind")
        if left is not None:
            ind.set(qn("left"), left)
        if right is not None:
            ind.set(qn("right"), right)
    if outline_level is not None:
        node = ensure_child(ppr, "outlineLvl")
        node.set(qn("val"), outline_level)
    if border_bottom_color or border_bottom_sz:
        pbdr = ensure_child(ppr, "pBdr")
        bottom = ensure_child(pbdr, "bottom")
        bottom.set(qn("val"), "single")
        bottom.set(qn("space"), "6")
        bottom.set(qn("color"), border_bottom_color or "C8A75B")
        bottom.set(qn("sz"), border_bottom_sz or "12")


def set_run_style(
    style: ET.Element,
    *,
    ascii_font: str | None = None,
    hansi_font: str | None = None,
    eastasia_font: str | None = None,
    color: str | None = None,
    size: str | None = None,
    bold: bool | None = None,
    italic: bool | None = None,
    caps: bool | None = None,
    small_caps: bool | None = None,
) -> None:
    rpr = ensure_child(style, "rPr")
    if ascii_font or hansi_font or eastasia_font:
        fonts = ensure_child(rpr, "rFonts")
        if ascii_font:
            fonts.set(qn("ascii"), ascii_font)
        if hansi_font:
            fonts.set(qn("hAnsi"), hansi_font)
        if eastasia_font:
            fonts.set(qn("eastAsia"), eastasia_font)
    if color is not None:
        node = ensure_child(rpr, "color")
        node.set(qn("val"), color)
    if size is not None:
        node = ensure_child(rpr, "sz")
        node.set(qn("val"), size)
        node_cs = ensure_child(rpr, "szCs")
        node_cs.set(qn("val"), size)
    if bold is not None:
        node = ensure_child(rpr, "b")
        if not bold:
            node.set(qn("val"), "0")
        else:
            node.attrib.pop(qn("val"), None)
        node_cs = ensure_child(rpr, "bCs")
        if not bold:
            node_cs.set(qn("val"), "0")
        else:
            node_cs.attrib.pop(qn("val"), None)
    if italic is not None:
        node = ensure_child(rpr, "i")
        if not italic:
            node.set(qn("val"), "0")
        else:
            node.attrib.pop(qn("val"), None)
    if caps:
        ensure_child(rpr, "caps")
    if small_caps:
        ensure_child(rpr, "smallCaps")


def style_by_id(styles_root: ET.Element, style_id: str) -> ET.Element | None:
    for style in styles_root.findall(qn("style")):
        if style.get(qn("styleId")) == style_id:
            return style
    return None


def add_cover_styles(styles_root: ET.Element) -> None:
    if style_by_id(styles_root, "CoverMetaLabel") is None:
        style = ET.SubElement(
            styles_root,
            qn("style"),
            {
                qn("type"): "paragraph",
                qn("styleId"): "CoverMetaLabel",
                qn("customStyle"): "1",
            },
        )
        ET.SubElement(style, qn("name"), {qn("val"): "Cover Meta Label"})
        ET.SubElement(style, qn("qFormat"))
        set_paragraph_style(
            style,
            based_on="Normal",
            next_style="CoverMetaValue",
            after="0",
            before="120",
            jc="center",
            keep_next=True,
        )
        set_run_style(
            style,
            ascii_font="Aptos",
            hansi_font="Aptos",
            eastasia_font="Aptos",
            color="7A6A3A",
            size="18",
            bold=True,
            caps=True,
        )

    if style_by_id(styles_root, "CoverMetaValue") is None:
        style = ET.SubElement(
            styles_root,
            qn("style"),
            {
                qn("type"): "paragraph",
                qn("styleId"): "CoverMetaValue",
                qn("customStyle"): "1",
            },
        )
        ET.SubElement(style, qn("name"), {qn("val"): "Cover Meta Value"})
        ET.SubElement(style, qn("qFormat"))
        set_paragraph_style(
            style,
            based_on="Normal",
            next_style="CoverMetaLabel",
            after="80",
            before="0",
            jc="center",
        )
        set_run_style(
            style,
            ascii_font="Aptos",
            hansi_font="Aptos",
            eastasia_font="Aptos",
            color="20364A",
            size="22",
        )


def update_styles(styles_xml: bytes) -> bytes:
    root = ET.fromstring(styles_xml)

    doc_defaults = root.find(qn("docDefaults"))
    if doc_defaults is not None:
        ppr_default = doc_defaults.find(f"{qn('pPrDefault')}/{qn('pPr')}")
        if ppr_default is None:
            ppr_default = ET.SubElement(ensure_child(doc_defaults, "pPrDefault"), qn("pPr"))
        spacing = ensure_child(ppr_default, "spacing")
        spacing.set(qn("after"), "120")
        spacing.set(qn("line"), "300")
        spacing.set(qn("lineRule"), "auto")
        jc = ensure_child(ppr_default, "jc")
        jc.set(qn("val"), "both")

        rpr_default = doc_defaults.find(f"{qn('rPrDefault')}/{qn('rPr')}")
        if rpr_default is None:
            rpr_default = ET.SubElement(ensure_child(doc_defaults, "rPrDefault"), qn("rPr"))
        fonts = ensure_child(rpr_default, "rFonts")
        fonts.set(qn("ascii"), "Aptos")
        fonts.set(qn("hAnsi"), "Aptos")
        fonts.set(qn("eastAsia"), "Aptos")
        size = ensure_child(rpr_default, "sz")
        size.set(qn("val"), "22")
        size_cs = ensure_child(rpr_default, "szCs")
        size_cs.set(qn("val"), "22")

    for style_id in ("Normal", "BodyText", "FirstParagraph", "Compact"):
        style = style_by_id(root, style_id)
        if style is None:
            continue
        set_paragraph_style(
            style,
            after="120" if style_id != "Compact" else "60",
            before="0",
            line="300",
            line_rule="auto",
            jc="both",
        )
        set_run_style(
            style,
            ascii_font="Aptos",
            hansi_font="Aptos",
            eastasia_font="Aptos",
            color="1F2933",
            size="22",
            bold=False,
            italic=False,
        )

    title = style_by_id(root, "Title")
    if title is not None:
        set_paragraph_style(
            title,
            based_on="Normal",
            next_style="Subtitle",
            before="120",
            after="120",
            line="360",
            line_rule="auto",
            jc="center",
            keep_next=True,
            keep_lines=True,
        )
        set_run_style(
            title,
            ascii_font="Cambria",
            hansi_font="Cambria",
            eastasia_font="Cambria",
            color="17324D",
            size="34",
            bold=True,
        )

    subtitle = style_by_id(root, "Subtitle")
    if subtitle is not None:
        set_paragraph_style(
            subtitle,
            based_on="Normal",
            next_style="BodyText",
            before="0",
            after="120",
            jc="center",
            keep_next=True,
            keep_lines=True,
        )
        set_run_style(
            subtitle,
            ascii_font="Aptos",
            hansi_font="Aptos",
            eastasia_font="Aptos",
            color="6A7480",
            size="22",
            italic=True,
        )

    for style_id, size in (("Heading1", "30"), ("Heading2", "26"), ("Heading3", "23")):
        style = style_by_id(root, style_id)
        if style is None:
            continue
        set_paragraph_style(
            style,
            based_on="Normal",
            next_style="BodyText",
            before="320" if style_id == "Heading1" else "220",
            after="80",
            jc="left",
            keep_next=True,
            keep_lines=True,
            contextual_spacing=True,
            outline_level={"Heading1": "0", "Heading2": "1", "Heading3": "2"}[style_id],
            border_bottom_color="C8A75B" if style_id == "Heading1" else None,
        )
        set_run_style(
            style,
            ascii_font="Cambria",
            hansi_font="Cambria",
            eastasia_font="Cambria",
            color="17324D" if style_id == "Heading1" else "274C67",
            size=size,
            bold=True,
            italic=False,
        )

    for style_id in ("Author", "Date"):
        style = style_by_id(root, style_id)
        if style is None:
            continue
        set_paragraph_style(
            style,
            based_on="Normal",
            next_style="BodyText",
            after="60",
            before="0",
            jc="center",
            keep_next=True,
        )
        set_run_style(
            style,
            ascii_font="Aptos",
            hansi_font="Aptos",
            eastasia_font="Aptos",
            color="5A6570",
            size="20",
        )

    captioned = style_by_id(root, "CaptionedFigure")
    if captioned is not None:
        set_paragraph_style(captioned, based_on="Normal", after="0", before="0", jc="center")

    image_caption = style_by_id(root, "ImageCaption")
    if image_caption is not None:
        set_paragraph_style(image_caption, based_on="Normal", after="0", before="0", jc="center")
        set_run_style(
            image_caption,
            ascii_font="Aptos",
            hansi_font="Aptos",
            eastasia_font="Aptos",
            color="FFFFFF",
            size="2",
        )

    add_cover_styles(root)
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: create-reference-template.py <source.docx> <output.docx>")
        return 1

    source = Path(sys.argv[1])
    output = Path(sys.argv[2])
    output.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir) / source.name
        shutil.copy2(source, tmp_path)

        with zipfile.ZipFile(tmp_path, "r") as source_zip:
            styles_xml = source_zip.read("word/styles.xml")
            files = {name: source_zip.read(name) for name in source_zip.namelist()}

        files["word/styles.xml"] = update_styles(styles_xml)

        rewritten_path = Path(tmp_dir) / f"rewritten-{source.name}"
        with zipfile.ZipFile(rewritten_path, "w", compression=zipfile.ZIP_DEFLATED) as out_zip:
            for name, data in files.items():
                out_zip.writestr(name, data)

        shutil.copy2(rewritten_path, output)

    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
