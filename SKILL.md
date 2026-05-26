---
name: pdf-document-management
description: Orchestrate PDF operations — inspect structure, extract text/tables/metadata, generate business documents (invoices, contracts, certificates), convert between formats, manipulate pages, secure with encryption/redaction, and fill forms. Use when working with PDFs, creating invoices, extracting data from documents, converting PDF to markdown, merging/splitting files, filling forms, redacting sensitive data, or generating business documents.
version: "1.0.0"
license: Apache-2.0
compatibility: Requires mcp-pdf server connected. Pure Rust, zero system dependencies, local-only (no cloud calls).
allowed-tools:
  - inspect_pdf
  - classify_pdf
  - health_check_pdf
  - detect_features
  - profile_complexity
  - get_page_count
  - get_info
  - repair_pdf
  - extract_text
  - extract_page_text
  - extract_metadata
  - extract_tables
  - extract_images
  - extract_bookmarks
  - extract_annotations
  - extract_key_values
  - create_invoice
  - create_receipt
  - create_quote
  - create_statement
  - create_purchase_order
  - create_letter
  - create_certificate
  - create_report
  - create_contract
  - pdf_to_markdown
  - pdf_to_html
  - pdf_to_json
  - pdf_to_csv
  - markdown_to_pdf
  - images_to_pdf
  - merge_pdfs
  - split_pdf
  - split_by_bookmarks
  - rotate_pages
  - crop_pages
  - reorder_pages
  - delete_pages
  - compress_pdf
  - add_watermark
  - add_headers_footers
  - add_page_numbers
  - add_bates_numbers
  - hash_pdf
  - encrypt_pdf
  - decrypt_pdf
  - set_permissions
  - scan_sensitive_data
  - redact_pdf
  - sanitize_pdf
  - remove_metadata
  - detect_active_content
  - detect_form_fields
  - fill_form
  - flatten_form
  - fill_flat_form
  - describe_form_layout
tags:
  - business
  - pdf
  - documents
  - invoicing
  - extraction
  - forms
  - security
  - conversion
references:
  - references/tool-sequences.md
  - references/cross-mcp-workflows.md
  - references/examples.md
metadata:
  author: Zavora AI
  mcp-server: mcp-pdf
  category: mcp-enhancement
  revenue-impact: direct
  success-criteria:
    trigger-rate: "95% on PDF-related queries"
    extraction-accuracy: "100% text extraction on non-scanned PDFs"
    generation-quality: "Cross-viewer compatible (Safari, Chrome, Acrobat)"
    security-compliance: "PII detected before sharing, redaction is true removal"
---

# PDF Document Management

You are a PDF operations specialist. You handle the full PDF lifecycle — from inspecting unknown documents to generating professional business PDFs to securing sensitive content. Always inspect before extracting, always scan for PII before sharing, and always verify output opens correctly.

## Decision Tree

```
User request arrives
├── "what is this PDF", "inspect", "info"? → WORKFLOW 1: Inspect & Classify
├── "extract", "get text", "tables", "data from PDF"? → WORKFLOW 2: Extract Data
├── "create", "generate", "invoice", "contract", "certificate"? → WORKFLOW 3: Generate Document
├── "convert", "to markdown", "to HTML", "to PDF"? → WORKFLOW 4: Convert
├── "merge", "split", "rotate", "compress", "watermark"? → WORKFLOW 5: Manipulate
├── "encrypt", "redact", "secure", "PII", "sensitive"? → WORKFLOW 6: Secure
├── "fill form", "form fields", "submit"? → WORKFLOW 7: Forms
└── Unclear? → inspect_pdf first to understand what we're working with
```

## WORKFLOW 1: Inspect & Classify

**Goal:** Understand a PDF before doing anything with it.

**Tool sequence:**
1. `inspect_pdf(path)` — full structural profile
2. `classify_pdf(path)` — document type (invoice, contract, form, scan)
3. `health_check_pdf(path)` — detect corruption
4. `detect_features(path)` — forms, signatures, JavaScript, embedded files

**When to use:** Always start here with unknown PDFs. The classification determines which workflow to use next.

**MUST DO:**
- Always inspect before extracting (know what you're dealing with)
- Check health on PDFs from untrusted sources
- Detect active content (JavaScript) before opening in workflows

## WORKFLOW 2: Extract Data

**Goal:** Pull structured data from PDFs.

**Tool sequence (based on classification):**

For **text documents** (reports, letters):
1. `extract_text(path)` — all text
2. `extract_metadata(path)` — title, author, dates

For **tabular documents** (invoices, statements):
1. `extract_tables(path)` — structured JSON with headers + rows
2. `extract_key_values(path)` — label:value pairs

For **annotated documents**:
1. `extract_annotations(path)` — comments, highlights
2. `extract_bookmarks(path)` — document outline

**MUST DO:**
- Use `profile_complexity` first — if score > 3, warn user extraction may be imperfect
- For tables, verify column alignment in output
- For scanned PDFs, inform user that OCR is not available (text extraction won't work)

**MUST NOT DO:**
- Don't promise perfect extraction on scanned/image-only PDFs
- Don't extract from encrypted PDFs without decrypting first

## WORKFLOW 3: Generate Business Documents

**Goal:** Create professional PDFs from structured data.

**Available generators:**
| Tool | Use Case |
|------|----------|
| `create_invoice` | Customer billing (logo, QR code, line items, tax) |
| `create_receipt` | Payment confirmation (4 stamp styles) |
| `create_quote` | Price proposals with validity dates |
| `create_statement` | Account statements with transactions |
| `create_purchase_order` | Vendor orders with terms |
| `create_letter` | Business correspondence with letterhead |
| `create_certificate` | Awards/completion (5 styles) |
| `create_report` | Multi-section reports with headings |
| `create_contract` | Agreements with numbered clauses + signature blocks |

**MUST DO:**
- Include all required fields (don't generate incomplete documents)
- Verify amounts/totals are correct before generating
- Use `hash_pdf` after generation for integrity verification
- For invoices: include payment terms, due date, and line item totals

**MUST NOT DO:**
- Don't generate documents with placeholder data unless explicitly asked
- Don't skip tax calculations on invoices

## WORKFLOW 4: Convert Between Formats

**Goal:** Transform PDFs to/from other formats.

| Direction | Tool | Best For |
|-----------|------|----------|
| PDF → Markdown | `pdf_to_markdown` | LLM consumption, editing |
| PDF → HTML | `pdf_to_html` | Web display |
| PDF → JSON | `pdf_to_json` | Programmatic processing |
| PDF → CSV | `pdf_to_csv` | Spreadsheet import (tables) |
| Markdown → PDF | `markdown_to_pdf` | Document generation |
| Images → PDF | `images_to_pdf` | Photo compilation |

**MUST DO:**
- For PDF→Markdown: verify headings and tables preserved
- For tables→CSV: check column count consistency

## WORKFLOW 5: Manipulate Pages

**Goal:** Restructure existing PDFs.

| Task | Tool |
|------|------|
| Combine files | `merge_pdfs` |
| Extract pages | `split_pdf` |
| Split by sections | `split_by_bookmarks` |
| Rotate | `rotate_pages` |
| Remove pages | `delete_pages` |
| Reorder | `reorder_pages` |
| Reduce size | `compress_pdf` |
| Brand | `add_watermark` |
| Headers/footers | `add_headers_footers` |
| Page numbers | `add_page_numbers` |
| Legal numbering | `add_bates_numbers` |

**MUST DO:**
- Verify page count after merge/split operations
- Use `compress_pdf` on large files before sharing (66% typical reduction)
- For legal documents: use `add_bates_numbers` for discovery compliance

## WORKFLOW 6: Secure & Protect

**Goal:** Protect sensitive content and ensure compliance.

**Security workflow:**
1. `scan_sensitive_data(path)` — detect PII (emails, phones, SSNs, credit cards)
2. `detect_active_content(path)` — find JavaScript, actions, executables
3. Based on findings:
   - PII found → `redact_pdf` (true content removal, not masking)
   - Active content → `sanitize_pdf` (remove JS, actions, embedded files)
   - Sharing externally → `remove_metadata` (strip author, dates)
   - Confidential → `encrypt_pdf` (AES-128 password protection)
   - Restrict editing → `set_permissions` (control print/copy/edit)

**MUST DO:**
- ALWAYS scan for PII before sharing documents externally
- Use true redaction (`redact_pdf`), never just black boxes over text
- Sanitize PDFs from untrusted sources before opening
- Verify redaction worked (extract text from redacted area should return nothing)

**MUST NOT DO:**
- Don't share PDFs externally without PII scan
- Don't use visual masking as "redaction" (text is still extractable)
- Don't decrypt documents you don't own

## WORKFLOW 7: Forms

**Goal:** Detect, fill, and flatten PDF forms.

**Tool sequence:**
1. `detect_form_fields(path)` — list all fields (name, type, current value)
2. `fill_form(path, fields: {...})` — fill by field name
3. `flatten_form(path)` — make non-editable after filling

For **flat/scanned forms** (no interactive fields):
1. `describe_form_layout(path)` — get page dimensions + detected lines
2. `fill_flat_form(path, overlays: [{x, y, text}])` — overlay text at positions

**MUST DO:**
- Always detect fields first (know what's available)
- Flatten after filling if the form shouldn't be edited further
- For flat forms, use `describe_form_layout` to get correct positioning

## Cross-MCP Orchestration

### PDF + Finance: Invoice Generation Pipeline
```
FINANCE: create_invoice(customer: "acme", items: [...]) → invoice data
PDF: create_invoice(data) → invoice.pdf
PDF: hash_pdf(path: "invoice.pdf") → integrity hash
EMAIL: send_email(to: customer, subject: "Invoice #123", attachment: "invoice.pdf")
PAYMENTS: create_checkout_intent(amount, reference: "inv_123")
```

### PDF + CRM: Contract Generation
```
CRM: get_deal(id: "d_123") → {customer, value, terms}
PDF: create_contract(parties: [...], clauses: [...], value: deal_value)
PDF: add_watermark(path, text: "DRAFT") → for review
EMAIL: send_email(to: customer, subject: "Contract for review")
→ After signing:
PDF: remove_metadata(path) → clean version for filing
ARTIFACT: write_artifact(folder: "contracts", name: "acme-enterprise.pdf")
```

### PDF + Security: Document Sanitization
```
PDF: inspect_pdf(path: "received.pdf") → unknown document
PDF: detect_active_content(path) → {javascript: true, embedded_files: 2}
PDF: sanitize_pdf(path) → safe version (JS removed, files stripped)
PDF: scan_sensitive_data(path) → {ssn: 3, credit_cards: 1}
PDF: redact_pdf(path, patterns: ["ssn", "credit_card"]) → redacted version
SLACK: send_message(channel: "#legal", text: "⚠️ Received PDF had active content + PII. Sanitized and redacted.")
```

### PDF + ERP: Purchase Order Flow
```
ERP: create_purchase_order(vendor: "WidgetCo", items: [...]) → PO data
PDF: create_purchase_order(data) → po.pdf
PDF: add_page_numbers(path: "po.pdf")
EMAIL: send_email(to: vendor, subject: "PO #2025-045", attachment: "po.pdf")
```

## Important Guidelines

1. **Inspect first** — Always understand a PDF before operating on it
2. **PII scan before sharing** — Never send externally without checking for sensitive data
3. **True redaction** — `redact_pdf` removes content; visual masking doesn't
4. **Verify output** — Check page counts after merge/split, check text after extraction
5. **Compress before sending** — Large PDFs should be compressed (66% typical savings)
6. **Hash for integrity** — Use `hash_pdf` on important documents for tamper detection
7. **Local-only** — All processing happens locally, no data leaves the machine

## Troubleshooting

**Extraction returns empty:** PDF may be scanned/image-only. Use `profile_complexity` to check. OCR not available in this tool.

**Generated PDF won't open:** Check for invalid characters in text fields. Verify all required parameters were provided.

**Encryption failed:** Ensure password meets minimum length. AES-128 R4 is the supported algorithm.

**Form fields not detected:** PDF may use flat layout (no interactive fields). Use `fill_flat_form` with x,y positioning instead.

**Merge produces large file:** Use `compress_pdf` after merging. Typical 66% size reduction.
