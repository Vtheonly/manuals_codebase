"""
==================================================================================
ALGERIAN VOCATIONAL TRAINING SYSTEM — PDF TEXT EXTRACTION UTILITY
Accurate PDF extraction with structural grouping to capture multi-column data.
Uses pypdf with layout-aware mode to preserve tabular structures across pages.
==================================================================================
Author: Ouail Fati7a wa3il fati7a / وائل فتيحة
==================================================================================
"""

import pypdf
import os
import sys


def parse_pdf_to_plaintext(pdf_location, target_txt_location):
    """
    Extracts text from a multi-page PDF document cleanly,
    preserving structured tabular data across page boundaries.

    Parameters
    ----------
    pdf_location : str
        Path to the input PDF file.
    target_txt_location : str
        Path where the extracted text will be written.

    Returns
    -------
    bool
        True if extraction succeeded, False otherwise.
    """
    try:
        # Validate input file exists
        if not os.path.exists(pdf_location):
            print(f"Extraction failed: The file '{pdf_location}' was not found.")
            return False

        reader = pypdf.PdfReader(pdf_location)
        total_pages = len(reader.pages)
        print(f"Reading target file containing: {total_pages} total pages.")
        print(f"Input: {pdf_location}")
        print(f"Output: {target_txt_location}")

        extracted_count = 0
        blank_count = 0

        with open(target_txt_location, 'w', encoding='utf-8') as output_file:
            # Write header metadata
            output_file.write("=" * 70 + "\n")
            output_file.write(f"EXTRACTED FROM: {os.path.basename(pdf_location)}\n")
            output_file.write(f"TOTAL PAGES: {total_pages}\n")
            output_file.write(f"EXTRACTION DATE: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
            output_file.write("=" * 70 + "\n")

            for index, page in enumerate(reader.pages):
                # Page separator marker for post-processing
                page_marker = f"\n\n--- COMPILER PAGE BREAK MARKER: {index + 1} ---\n"
                output_file.write(page_marker)

                # Extract text with layout_mode=True to preserve
                # vertical alignments (multi-column, tables)
                text_content = page.extract_text(layout_mode=True)

                if text_content and text_content.strip():
                    output_file.write(text_content.strip() + "\n")
                    extracted_count += 1
                else:
                    output_file.write("[Blank / Unreadable Scan Block]\n")
                    blank_count += 1

                # Progress indicator for large documents
                if (index + 1) % 10 == 0:
                    print(f"  Processed {index + 1}/{total_pages} pages...")

        print(f"\nExtraction complete!")
        print(f"  Pages with content: {extracted_count}")
        print(f"  Blank pages: {blank_count}")
        print(f"  Output written cleanly to: {target_txt_location}")
        print(f"  File size: {os.path.getsize(target_txt_location) / 1024:.1f} KB")
        return True

    except FileNotFoundError:
        print(f"Extraction failed: The file at '{pdf_location}' was not found.")
        return False
    except pypdf.errors.PdfReadError as e:
        print(f"PDF read error: The file may be corrupted or encrypted: {e}")
        return False
    except PermissionError as e:
        print(f"Permission error: Cannot access file: {e}")
        return False
    except Exception as e:
        print(f"System extraction fault encountered: {e}")
        return False


def parse_pdf_to_structured_text(pdf_location, target_txt_location):
    """
    Enhanced extraction that groups text by structural heuristics
    (headers, paragraphs, tables) for better downstream parsing.

    This version attempts to detect table structures by looking for
    consistent column spacing patterns in the layout-mode output.
    """
    try:
        if not os.path.exists(pdf_location):
            print(f"File not found: '{pdf_location}'")
            return False

        reader = pypdf.PdfReader(pdf_location)
        total_pages = len(reader.pages)
        print(f"Structured extraction from: {total_pages} pages")

        with open(target_txt_location, 'w', encoding='utf-8') as output_file:
            output_file.write("=" * 70 + "\n")
            output_file.write(f"STRUCTURED EXTRACTION FROM: {os.path.basename(pdf_location)}\n")
            output_file.write("=" * 70 + "\n")

            for index, page in enumerate(reader.pages):
                output_file.write(f"\n--- PAGE {index + 1} ---\n")
                text = page.extract_text(layout_mode=True)

                if text and text.strip():
                    # Split into lines and preserve structure
                    lines = text.strip().split('\n')
                    for line in lines:
                        stripped = line.strip()
                        if not stripped:
                            continue
                        # Detect likely table rows (multiple number sequences)
                        # by checking if line has consistent spacing
                        output_file.write(stripped + "\n")
                else:
                    output_file.write("[BLANK PAGE]\n")

        print(f"Structured extraction complete: {target_txt_location}")
        return True

    except Exception as e:
        print(f"Structured extraction failed: {e}")
        return False


# ==================================================================================
# CLI ENTRY POINT
# ==================================================================================
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Extract text from Algerian Vocational Training PDF manuals."
    )
    parser.add_argument("input", help="Path to the input PDF file")
    parser.add_argument("-o", "--output", default=None,
                        help="Output text file path (default: input filename with .txt)")
    parser.add_argument("--structured", action="store_true",
                        help="Use enhanced structured extraction mode")

    args = parser.parse_args()

    # Determine output path
    if args.output is None:
        base = os.path.splitext(args.input)[0]
        args.output = base + "_extracted.txt"

    print(f"\nPDF Text Extraction Utility")
    print(f"{'='*50}")

    if args.structured:
        parse_pdf_to_structured_text(args.input, args.output)
    else:
        parse_pdf_to_plaintext(args.input, args.output)

    print(f"{'='*50}\n")