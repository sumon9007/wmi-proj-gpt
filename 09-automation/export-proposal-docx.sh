#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROPOSAL_DIR="$ROOT_DIR/05-deliverables/proposals/2026-GAUTENGTREASURY-BIOMETRIC-AUTHENTICATION"
SRC="$PROPOSAL_DIR/draft/proposal.md"
OUT_DIR="$ROOT_DIR/05-deliverables/exports/docx"
OUT_FILE="$OUT_DIR/2026-GAUTENGTREASURY-BIOMETRIC-AUTHENTICATION-proposal-draft.docx"
TMP_MD="$(mktemp)"
REFERENCE_DOC="$PROPOSAL_DIR/attachments/reference-template.docx"
TEMPLATE_SCRIPT="$ROOT_DIR/09-automation/create-reference-template.py"
TEMPLATE_SOURCE_DOC="$OUT_FILE"
POLISH_SCRIPT="$ROOT_DIR/09-automation/polish-exported-docx.py"
SUBMISSION_TEMPLATE="$PROPOSAL_DIR/attachments/submission-template.docx"
FINAL_OUT_FILE="$OUT_DIR/2026-GAUTENGTREASURY-BIOMETRIC-AUTHENTICATION-proposal-final.docx"

BIDDER_LOGO_SVG="$PROPOSAL_DIR/attachments/branding/bidder-logo.svg"
BIDDER_LOGO_PNG="$PROPOSAL_DIR/attachments/branding/bidder-logo.png"
CUSTOMER_LOGO_SVG="$PROPOSAL_DIR/attachments/branding/customer-logo.svg"
CUSTOMER_LOGO_PNG="$PROPOSAL_DIR/attachments/branding/customer-logo.png"

cleanup() {
  rm -f "$TMP_MD"
}
trap cleanup EXIT

if ! command -v pandoc >/dev/null 2>&1; then
  echo "pandoc is not installed."
  echo "Install it on Ubuntu with:"
  echo "  sudo apt update && sudo apt install -y pandoc"
  exit 1
fi

pick_logo() {
  local svg_path="$1"
  local png_path="$2"
  if [[ -f "$svg_path" ]]; then
    printf '%s' "$svg_path"
  elif [[ -f "$png_path" ]]; then
    printf '%s' "$png_path"
  else
    printf ''
  fi
}

BIDDER_LOGO="$(pick_logo "$BIDDER_LOGO_SVG" "$BIDDER_LOGO_PNG")"
CUSTOMER_LOGO="$(pick_logo "$CUSTOMER_LOGO_SVG" "$CUSTOMER_LOGO_PNG")"

{
  printf -- '---\n'
  printf -- 'lang: en\n'
  printf -- 'toc: true\n'
  printf -- 'toc-depth: 2\n'
  printf -- 'numbersections: false\n'
  printf -- '...\n\n'

  if [[ -n "$BIDDER_LOGO" && -n "$CUSTOMER_LOGO" ]]; then
    printf -- '| ![](%s){ width=42%% } | ![](%s){ width=26%% } |\n' "$BIDDER_LOGO" "$CUSTOMER_LOGO"
    printf -- '|:--|--:|\n\n'
  else
    if [[ -n "$BIDDER_LOGO" ]]; then
      printf -- '![](%s){ width=30%% }\n\n' "$BIDDER_LOGO"
    else
      printf -- '**Waymark Infotech**\n\n'
    fi
    if [[ -n "$CUSTOMER_LOGO" ]]; then
      printf -- '![](%s){ width=24%% }\n\n' "$CUSTOMER_LOGO"
    else
      printf -- '**Gauteng Provincial Treasury**\n\n'
    fi
  fi

  printf -- '::: {custom-style="Title"}\n'
  printf -- 'Proposal for Gauteng Provincial Treasury\n'
  printf -- ':::\n\n'

  printf -- '::: {custom-style="Subtitle"}\n'
  printf -- 'Development of Biometric Authentication System Including Support and Maintenance for a Period of 3 Years\n'
  printf -- ':::\n\n'

  printf -- '| Document Detail | Value |\n'
  printf -- '|:--|:--|\n'
  printf -- '| Tender Reference | GT/GPT/009/2026 |\n'
  printf -- '| Prepared By | Waymark Infotech |\n'
  printf -- '| Prepared For | Gauteng Provincial Treasury |\n'
  printf -- '| Document Status | Draft for internal review |\n'
  printf -- '| Date | 2026-03-13 |\n\n'

  printf -- '\\newpage\n\n'

  awk '
    BEGIN { skip = 1 }
    /^## 1\. Executive Summary$/ { skip = 0 }
    skip { next }
    { print }
  ' "$SRC"
} > "$TMP_MD"

mkdir -p "$OUT_DIR"

if [[ ! -f "$REFERENCE_DOC" ]]; then
  if [[ -f "$TEMPLATE_SOURCE_DOC" && -x "$TEMPLATE_SCRIPT" ]]; then
    python3 "$TEMPLATE_SCRIPT" "$TEMPLATE_SOURCE_DOC" "$REFERENCE_DOC" >/dev/null
  fi
fi

PANDOC_ARGS=(
  "$TMP_MD"
  --from markdown
  --to docx
  --standalone
  --table-of-contents
  --toc-depth=2
  -o "$OUT_FILE"
)

if [[ -f "$REFERENCE_DOC" ]]; then
  PANDOC_ARGS+=(--reference-doc="$REFERENCE_DOC")
fi

pandoc "${PANDOC_ARGS[@]}"

if [[ -x "$POLISH_SCRIPT" ]]; then
  python3 "$POLISH_SCRIPT" "$OUT_FILE" "$OUT_FILE" draft
  python3 "$POLISH_SCRIPT" "$OUT_FILE" "$SUBMISSION_TEMPLATE" final
fi

echo "Draft Word document created:"
echo "  $OUT_FILE"
if [[ -z "$BIDDER_LOGO" || -z "$CUSTOMER_LOGO" ]]; then
  echo
  echo "Note: one or both logo files were missing, so fallback text was inserted instead."
fi
