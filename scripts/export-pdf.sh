#!/usr/bin/env bash
# Convert a generated Markdown document to a clean, signable PDF.
#
# Usage:
#   scripts/export-pdf.sh output/acme-proposal.md
#   scripts/export-pdf.sh output/acme-proposal.md output/acme-proposal.pdf
#
# Requires pandoc. A LaTeX engine (for best output) or wkhtmltopdf is used if
# available; the script picks whichever it finds.

set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: $0 <input.md> [output.pdf]" >&2
  exit 1
fi

INPUT="$1"
OUTPUT="${2:-${INPUT%.md}.pdf}"

if [ ! -f "$INPUT" ]; then
  echo "Error: input file not found: $INPUT" >&2
  exit 1
fi

if ! command -v pandoc >/dev/null 2>&1; then
  echo "Error: pandoc is not installed." >&2
  echo "  Debian/Ubuntu: sudo apt-get install pandoc" >&2
  echo "  macOS:         brew install pandoc" >&2
  echo "  For best output also install a LaTeX engine, e.g. texlive-xetex." >&2
  exit 1
fi

COMMON_ARGS=(
  "$INPUT"
  -o "$OUTPUT"
  --metadata "title="
  -V geometry:margin=1in
  -V fontsize=11pt
  -V linkcolor=blue
  --toc-depth=2
)

# Pick a PDF engine that is actually installed.
if command -v xelatex >/dev/null 2>&1; then
  ENGINE=(--pdf-engine=xelatex -V mainfont="DejaVu Serif")
elif command -v pdflatex >/dev/null 2>&1; then
  ENGINE=(--pdf-engine=pdflatex)
elif command -v weasyprint >/dev/null 2>&1; then
  ENGINE=(--pdf-engine=weasyprint)
elif command -v wkhtmltopdf >/dev/null 2>&1; then
  ENGINE=(--pdf-engine=wkhtmltopdf)
else
  echo "Error: no PDF engine found." >&2
  echo "  Install one of: texlive-xetex, weasyprint, or wkhtmltopdf." >&2
  exit 1
fi

echo "Converting $INPUT -> $OUTPUT ..."
pandoc "${COMMON_ARGS[@]}" "${ENGINE[@]}"
echo "Done: $OUTPUT"
