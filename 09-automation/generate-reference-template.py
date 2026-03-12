#!/usr/bin/env python3
from __future__ import annotations

import shutil
import tempfile
import zipfile
from pathlib import Path
import xml.etree.ElementTree as ET

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}
ET.register_namespace("w", W)


def qn(tag: str) -> str:
    return f"{{{W}}}{tag}"


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "05-deliverables/exports/docx/2026-GAUTENGTREASURY-BIOMETRIC-AUTHENTICATION-proposal-draft.docx"
OUT = ROOT / "05-deliverables/proposals/2026-GAUTENGTREASURY-BIOMETRIC-AUTHENTICATION/attachments/reference-template.docx"


def ensure_child(parent: ET.Element, tag: str) -> ET.Element:
    child = parent.find(f"w:{tag}", NS)
    if child is None:
        child = ET.SubElement(parent, qn(tag))
    return child


def set_run_style(style: ET.Element, *, font: str | None = None, size: int | None = None, color: str | None = None, bold: bool | None = None):
    rpr = ensure_child(style, "rPr")
    if font:
        rfonts = ensure_child(rpr, "rFonts")
        rfonts.set(qn("ascii"), font)
        rfonts.set(qn("hAnsi"), font)
    if size:
        sz = ensure_child(rpr, "sz")
        sz.set(qn("val"), str(size))
        szcs = ensure_child(rpr, "szCs")
        szcs.set(qn("val"), str(size))
    if color:
        c = ensure_child(rpr, "color")
        c.set(qn("val"), color)
    if bold is not None:
        b = rpr.find("w:b", NS)
        if bold:
            if b is None:
                ET.SubElement(rpr, qn("b"))
            bcs = rpr.find("w:bCs", NS)
            if bcs is None:
                ET.SubElement(rpr, qn("bCs"))
        else:
            if b is not None:
                rpr.remove(b)


def set_para_style(style: ET.Element, *, jc: str | None = None, before: int | None = None, after: int | None = None, line: int | None = None):
    ppr = ensure_child(style, "pPr")
    if jc:
        j = ensure_child(ppr, "jc")
        j.set(qn("val"), jc)
    spacing = ensure_child(ppr, "spacing")
    if before is not None:
        spacing.set(qn("before"), str(before))
    if after is not None:
        spacing.set(qn("after"), str(after))
    if line is not None:
        spacing.set(qn("line"), str(line))
        spacing.set(qn("lineRule"), "auto")


with tempfile.TemporaryDirectory() as td:
    tmpdir = Path(td)
    with zipfile.ZipFile(SRC) as z:
        z.extractall(tmpdir)

    styles_path = tmpdir / "word/styles.xml"
    styles_tree = ET.parse(styles_path)
    styles_root = styles_tree.getroot()

    # Defaults
    doc_defaults = styles_root.find("w:docDefaults", NS)
    if doc_defaults is not None:
        rpr_default = doc_defaults.find("w:rPrDefault/w:rPr", NS)
        if rpr_default is not None:
            rfonts = ensure_child(rpr_default, "rFonts")
            rfonts.set(qn("ascii"), "Aptos")
            rfonts.set(qn("hAnsi"), "Aptos")
            sz = ensure_child(rpr_default, "sz")
            sz.set(qn("val"), "22")
            szcs = ensure_child(rpr_default, "szCs")
            szcs.set(qn("val"), "22")
        ppr_default = doc_defaults.find("w:pPrDefault/w:pPr", NS)
        if ppr_default is not None:
            spacing = ensure_child(ppr_default, "spacing")
            spacing.set(qn("after"), "120")
            spacing.set(qn("line"), "300")
            spacing.set(qn("lineRule"), "auto")
            jc = ensure_child(ppr_default, "jc")
            jc.set(qn("val"), "both")

    style_map = {s.get(qn("styleId")): s for s in styles_root.findall("w:style", NS)}

    for sid in ["Normal", "BodyText", "FirstParagraph", "Compact"]:
        s = style_map.get(sid)
        if s is not None:
            set_para_style(s, jc="both", before=0, after=120, line=300)
            set_run_style(s, font="Aptos", size=22, color="1F1F1F")

    if style_map.get("Title") is not None:
        set_para_style(style_map["Title"], jc="center", before=240, after=220, line=320)
        set_run_style(style_map["Title"], font="Aptos Display", size=34, color="163A63", bold=True)

    if style_map.get("Date") is not None:
        set_para_style(style_map["Date"], jc="center", before=0, after=200, line=280)
        set_run_style(style_map["Date"], font="Aptos", size=20, color="5A5A5A")

    for sid, size, color in [("Heading1", 30, "163A63"), ("Heading2", 24, "254F7A"), ("Heading3", 21, "345A8A"), ("TOCHeading", 24, "163A63")]:
        s = style_map.get(sid)
        if s is not None:
            set_para_style(s, jc="left", before=180, after=100, line=280)
            set_run_style(s, font="Aptos", size=size, color=color, bold=True)

    for sid in ["CaptionedFigure", "ImageCaption"]:
        s = style_map.get(sid)
        if s is not None:
            set_para_style(s, jc="center", before=40, after=40, line=240)
            set_run_style(s, font="Aptos", size=18, color="6A6A6A")

    styles_tree.write(styles_path, encoding="utf-8", xml_declaration=True)

    shutil.make_archive(str(OUT.with_suffix("")), "zip", tmpdir)
    zip_path = OUT.with_suffix(".zip")
    if OUT.exists():
        OUT.unlink()
    zip_path.rename(OUT)

print(OUT)
