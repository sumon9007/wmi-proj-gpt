#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DOCX_SCRIPT="$ROOT_DIR/09-automation/export-proposal-docx.sh"
DOCX_OUT="$ROOT_DIR/05-deliverables/exports/docx/2026-GAUTENGTREASURY-BIOMETRIC-AUTHENTICATION-proposal-draft.docx"
PDF_OUT_DIR="$ROOT_DIR/05-deliverables/exports/pdf"
PDF_OUT="$PDF_OUT_DIR/2026-GAUTENGTREASURY-BIOMETRIC-AUTHENTICATION-proposal-draft.pdf"

if [[ ! -x "$DOCX_SCRIPT" ]]; then
  echo "DOCX export helper is missing or not executable:"
  echo "  $DOCX_SCRIPT"
  exit 1
fi

if ! command -v libreoffice >/dev/null 2>&1; then
  echo "libreoffice is not installed."
  echo "Install it on Ubuntu with:"
  echo "  sudo apt update && sudo apt install -y libreoffice-writer"
  exit 1
fi

mkdir -p "$PDF_OUT_DIR"

"$DOCX_SCRIPT"

if [[ ! -f "$DOCX_OUT" ]]; then
  echo "Expected DOCX export was not created:"
  echo "  $DOCX_OUT"
  exit 1
fi

libreoffice --headless --convert-to pdf --outdir "$PDF_OUT_DIR" "$DOCX_OUT" >/dev/null

if [[ ! -f "$PDF_OUT" ]]; then
  echo "PDF export did not produce the expected file:"
  echo "  $PDF_OUT"
  exit 1
fi

echo "Draft PDF document created:"
echo "  $PDF_OUT"
