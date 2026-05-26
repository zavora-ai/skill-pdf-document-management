# PDF Tool Sequences Reference

## Tool Inventory (mcp-pdf, 57 tools)

### Inspect (8)
| Tool | Purpose |
|------|---------|
| `inspect_pdf` | Full structural profile |
| `classify_pdf` | Document type detection |
| `health_check_pdf` | Corruption detection |
| `detect_features` | Forms, signatures, JS, embedded files |
| `profile_complexity` | Extraction difficulty (1-5) |
| `get_page_count` | Page count |
| `get_info` | Quick metadata |
| `repair_pdf` | Fix corrupted PDFs |

### Extract (9)
| Tool | Purpose |
|------|---------|
| `extract_text` | All text |
| `extract_page_text` | Text from specific page |
| `extract_metadata` | Title, author, dates, XMP |
| `extract_tables` | Tables as JSON (headers + rows) |
| `extract_images` | Image info (dimensions, color) |
| `extract_bookmarks` | Outline tree |
| `extract_annotations` | Comments, highlights |
| `extract_key_values` | Label:value pairs |

### Generate (9)
| Tool | Purpose |
|------|---------|
| `create_invoice` | Invoice with logo, QR, line items |
| `create_receipt` | Payment receipt (4 stamp styles) |
| `create_quote` | Price quote with validity |
| `create_statement` | Account statement |
| `create_purchase_order` | PO with terms |
| `create_letter` | Business letter |
| `create_certificate` | Certificate (5 styles) |
| `create_report` | Multi-section report |
| `create_contract` | Agreement with signature blocks |

### Convert (6)
| Tool | Direction |
|------|-----------|
| `pdf_to_markdown` | PDF → Markdown |
| `pdf_to_html` | PDF → HTML |
| `pdf_to_json` | PDF → JSON |
| `pdf_to_csv` | PDF tables → CSV |
| `markdown_to_pdf` | Markdown → PDF |
| `images_to_pdf` | Images → PDF |

### Manipulate (11)
| Tool | Purpose |
|------|---------|
| `merge_pdfs` | Combine multiple PDFs |
| `split_pdf` | Extract page ranges |
| `split_by_bookmarks` | Split by sections |
| `rotate_pages` | Rotate 90/180/270° |
| `crop_pages` | Crop to bounding box |
| `reorder_pages` | Reorder by index |
| `delete_pages` | Remove pages |
| `compress_pdf` | Reduce size (66% typical) |
| `add_watermark` | Text watermark |
| `add_headers_footers` | Dynamic headers/footers |
| `add_page_numbers` | Page numbering |

### Numbering (2)
| Tool | Purpose |
|------|---------|
| `add_page_numbers` | Arabic/Roman/alpha |
| `add_bates_numbers` | Legal Bates numbering |

### Security (9)
| Tool | Purpose |
|------|---------|
| `hash_pdf` | SHA-256 integrity |
| `encrypt_pdf` | AES-128 password protection |
| `decrypt_pdf` | Remove password |
| `set_permissions` | Control print/copy/edit |
| `scan_sensitive_data` | Detect PII |
| `redact_pdf` | True content removal |
| `sanitize_pdf` | Remove JS, actions, files |
| `remove_metadata` | Strip author/dates |
| `detect_active_content` | Find JS/executables |

### Forms (5)
| Tool | Purpose |
|------|---------|
| `detect_form_fields` | List all fields |
| `fill_form` | Fill interactive fields |
| `flatten_form` | Make non-editable |
| `fill_flat_form` | Overlay text at x,y |
| `describe_form_layout` | Page dimensions + lines |

## Sequence: Full Document Processing (4-5 calls)

```
1. inspect_pdf(path: "document.pdf")
   → {pages: 12, size: "2.4MB", has_forms: true, has_text: true}

2. classify_pdf(path: "document.pdf")
   → {type: "invoice", confidence: 0.95}

3. extract_tables(path: "document.pdf")
   → {tables: [{headers: ["Item", "Qty", "Price"], rows: [["Widget", "10", "$50"]]}]}

4. extract_key_values(path: "document.pdf")
   → {pairs: [{"Invoice #": "INV-001"}, {"Date": "2025-01-18"}, {"Total": "$500"}]}
```

## Sequence: Generate Invoice (1-2 calls)

```
1. create_invoice(
     vendor: {name: "Zavora AI", address: "Nairobi, Kenya"},
     customer: {name: "Acme Corp", address: "123 Main St"},
     items: [{description: "Enterprise Plan", quantity: 1, unit_price: 75000}],
     tax_rate: 16,
     due_date: "2025-02-15",
     invoice_number: "INV-2025-001"
   )
   → {path: "/output/INV-2025-001.pdf", pages: 1, size: "45KB"}

2. hash_pdf(path: "/output/INV-2025-001.pdf")
   → {sha256: "abc123..."}
```

## Sequence: Secure Before Sharing (3 calls)

```
1. scan_sensitive_data(path: "report.pdf")
   → {findings: [{type: "ssn", count: 3, pages: [2, 5]}, {type: "email", count: 12}]}

2. redact_pdf(path: "report.pdf", patterns: ["ssn"])
   → {redacted: 3, output: "report_redacted.pdf"}

3. remove_metadata(path: "report_redacted.pdf")
   → {removed: ["author", "creator", "creation_date"]}
```
