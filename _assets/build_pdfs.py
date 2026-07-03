#!/usr/bin/env python3
"""Convert NEXUS Blueprint Markdown files to PDFs using fpdf2."""
import sys
import os
import re
import warnings
warnings.filterwarnings("ignore")

from fpdf import FPDF

ROOT = "/root/nexus-blueprint"
OUT_DIR = "/root/nexus-blueprint/_assets/pdfs"
MASTER_PDF = "/root/nexus-blueprint/_assets/pdfs/00_NEXUS_MASTER.pdf"

# Create output directory mirroring structure
os.makedirs(OUT_DIR, exist_ok=True)


def md_to_pdf_text(md_path: str) -> tuple[str, list]:
    """Convert markdown to plain text blocks, capturing structure for PDF rendering."""
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Strip code fences (preserve content as code block)
    blocks = []
    lines = content.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("```"):
            # Code block — collect
            lang = line.strip().lstrip("`").strip()
            i += 1
            code_lines = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            blocks.append(("code", "\n".join(code_lines), lang))
            i += 1
            continue
        if line.startswith("# "):
            blocks.append(("h1", line[2:].strip(), None))
        elif line.startswith("## "):
            blocks.append(("h2", line[3:].strip(), None))
        elif line.startswith("### "):
            blocks.append(("h3", line[4:].strip(), None))
        elif line.startswith("#### "):
            blocks.append(("h4", line[5:].strip(), None))
        elif line.startswith("| ") and "|" in line[2:]:
            # Table row — collect contiguous table
            tbl = []
            while i < len(lines) and lines[i].startswith("|"):
                tbl.append(lines[i])
                i += 1
            blocks.append(("table", "\n".join(tbl), None))
            continue
        elif line.startswith("- ") or line.startswith("* "):
            blocks.append(("bullet", line[2:].strip(), None))
        elif re.match(r"^\d+\.\s", line):
            blocks.append(("numbered", re.sub(r"^\d+\.\s+", "", line).strip(), None))
        elif line.startswith(">"):
            blocks.append(("quote", line.lstrip(">").strip(), None))
        elif line.strip() == "---":
            blocks.append(("hr", "", None))
        elif line.strip() == "":
            blocks.append(("blank", "", None))
        else:
            # Accumulate paragraph
            para = [line]
            i += 1
            while i < len(lines) and lines[i].strip() != "" and not (
                lines[i].startswith("#") or lines[i].startswith("|") or
                lines[i].startswith("- ") or lines[i].startswith("* ") or
                lines[i].startswith("```") or lines[i].startswith(">") or
                re.match(r"^\d+\.\s", lines[i])
            ):
                para.append(lines[i])
                i += 1
            blocks.append(("para", " ".join(para).strip(), None))
            continue
        i += 1
    return blocks


def clean_md_for_pdf(text: str) -> str:
    """Strip markdown formatting for plain text rendering."""
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"`(.+?)`", r"\1", text)
    text = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", text)
    text = re.sub(r"^#+\s+", "", text)
    return text


def render_pdf(md_files: list, out_path: str, title: str = "NEXUS Blueprint") -> bool:
    """Render all md files into a single PDF."""
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_margins(left=15, top=15, right=15)
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 18)
    pdf.cell(0, 12, title, new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.set_font("Helvetica", "I", 10)
    pdf.cell(0, 8, f"{len(md_files)} documents", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.ln(4)

    for idx, md_path in enumerate(md_files, 1):
        rel = os.path.relpath(md_path, ROOT)
        try:
            blocks = md_to_pdf_text(md_path)
        except Exception as e:
            print(f"  err {rel}: {e}", file=sys.stderr)
            continue

        pdf.add_page()
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(120, 120, 120)
        pdf.cell(0, 5, f"[{idx}/{len(md_files)}] {rel}", new_x="LMARGIN", new_y="NEXT")
        pdf.set_text_color(0, 0, 0)
        pdf.ln(1)

        for kind, text, lang in blocks:
            text = clean_md_for_pdf(text)
            if kind == "h1":
                pdf.set_font("Helvetica", "B", 16)
                pdf.ln(2)
                pdf.multi_cell(0, 7, text)
                pdf.ln(2)
            elif kind == "h2":
                pdf.set_font("Helvetica", "B", 13)
                pdf.ln(2)
                pdf.multi_cell(0, 6, text)
                pdf.ln(1)
            elif kind == "h3":
                pdf.set_font("Helvetica", "B", 11)
                pdf.ln(1)
                pdf.multi_cell(0, 5.5, text)
            elif kind == "h4":
                pdf.set_font("Helvetica", "B", 10)
                pdf.multi_cell(0, 5, text)
            elif kind == "para":
                pdf.set_font("Helvetica", "", 10)
                pdf.multi_cell(0, 5, text)
                pdf.ln(1)
            elif kind == "bullet":
                pdf.set_font("Helvetica", "", 10)
                pdf.multi_cell(0, 5, f"  • {text}")
            elif kind == "numbered":
                pdf.set_font("Helvetica", "", 10)
                pdf.multi_cell(0, 5, f"  {text}")
            elif kind == "code":
                pdf.set_font("Courier", "", 8)
                pdf.set_fill_color(240, 240, 240)
                # Truncate very long code
                if len(text) > 1500:
                    text = text[:1500] + "\n... (truncated)"
                pdf.multi_cell(0, 4, text, fill=True)
                pdf.ln(1)
                pdf.set_font("Helvetica", "", 10)
            elif kind == "table":
                pdf.set_font("Courier", "", 7)
                # Truncate tables to keep file size reasonable
                tbl_lines = text.split("\n")
                if len(tbl_lines) > 25:
                    text = "\n".join(tbl_lines[:25]) + "\n... (table truncated)"
                pdf.multi_cell(0, 3.5, text)
                pdf.ln(1)
                pdf.set_font("Helvetica", "", 10)
            elif kind == "quote":
                pdf.set_font("Helvetica", "I", 10)
                pdf.multi_cell(0, 5, f"  {text}")
            elif kind == "hr":
                pdf.ln(2)
                pdf.line(15, pdf.get_y(), 195, pdf.get_y())
                pdf.ln(2)
            elif kind == "blank":
                pdf.ln(2)

    try:
        pdf.output(out_path)
        return True
    except Exception as e:
        print(f"  PDF write err: {e}", file=sys.stderr)
        return False


def collect_md_files() -> list:
    """Collect all .md files in canonical reading order."""
    order = [
        "README.md",
        "MASTER_INDEX.md",
        "_assets/PROGRESS.md",
        "00_EXECUTIVE",
        "01_PRODUCT",
        "02_DESIGN_SYSTEM",
        "03_UI_SCREENS",
        "04_BROWSER_ENGINE",
        "05_AI_PLATFORM",
        "06_ENGINEERING_TEAM",
        "07_BACKEND",
        "08_SECURITY",
        "09_MARKETPLACE",
        "10_DEPLOYMENT",
        "11_BUSINESS",
        "12_DEVELOPER_GUIDE",
        "99_MASTER_PROMPTS",
    ]
    out = []
    seen = set()
    # Top-level files first
    for name in ["README.md", "MASTER_INDEX.md"]:
        p = os.path.join(ROOT, name)
        if os.path.isfile(p) and p not in seen:
            out.append(p)
            seen.add(p)
    # Then in order
    for d in order:
        full = os.path.join(ROOT, d)
        if not os.path.isdir(full):
            continue
        # Recurse — DFS, sort files
        for subdir, _, files in os.walk(full):
            # Skip _assets to avoid PDFs-in-PDFs
            if "_assets" in subdir:
                continue
            for f in sorted(files):
                if f.endswith(".md"):
                    p = os.path.join(subdir, f)
                    if p not in seen:
                        out.append(p)
                        seen.add(p)
    # Then _assets files except PROGRESS (already at top)
    for subdir, _, files in os.walk(os.path.join(ROOT, "_assets")):
        for f in sorted(files):
            if f.endswith(".md") and f != "PROGRESS.md":
                p = os.path.join(subdir, f)
                if p not in seen:
                    out.append(p)
                    seen.add(p)
    return out


if __name__ == "__main__":
    md_files = collect_md_files()
    print(f"Found {len(md_files)} markdown files")

    if len(sys.argv) > 1 and sys.argv[1] == "--master":
        print(f"Building master PDF → {MASTER_PDF}")
        ok = render_pdf(md_files, MASTER_PDF)
        print(f"Master PDF: {'OK' if ok else 'FAILED'}")
        if os.path.isfile(MASTER_PDF):
            sz = os.path.getsize(MASTER_PDF)
            print(f"  size: {sz:,} bytes ({sz/1024/1024:.1f} MB)")
    else:
        # Per-directory PDFs
        by_dir = {}
        for p in md_files:
            rel = os.path.relpath(p, ROOT)
            top = rel.split("/")[0]
            by_dir.setdefault(top, []).append(p)
        for top, files in by_dir.items():
            out = os.path.join(OUT_DIR, f"NEXUS_{top}.pdf")
            print(f"Building {top} ({len(files)} files) → {out}")
            ok = render_pdf(files, out, title=f"NEXUS Blueprint — {top}")
            sz = os.path.getsize(out) if os.path.isfile(out) else 0
            print(f"  {'OK' if ok else 'FAIL'}: {sz:,} bytes")