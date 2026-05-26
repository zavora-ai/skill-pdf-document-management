# PDF Skill Examples

## Example 1: "Extract data from this invoice PDF"

**User says:** "Get the line items and total from invoice.pdf"

**Tool calls:**
```
1. classify_pdf(path: "invoice.pdf")
   → {type: "invoice", confidence: 0.95}

2. extract_tables(path: "invoice.pdf")
   → {tables: [{headers: ["Description", "Qty", "Unit Price", "Total"],
       rows: [["Enterprise Plan", "1", "$750.00", "$750.00"],
              ["Extra Users (5)", "5", "$10.00", "$50.00"]]}]}

3. extract_key_values(path: "invoice.pdf")
   → {pairs: {"Invoice #": "INV-2025-001", "Date": "Jan 18, 2025", "Due": "Feb 15, 2025", "Subtotal": "$800.00", "Tax (16%)": "$128.00", "Total": "$928.00"}}
```

**Response:**
```
## Invoice Data Extracted

**Invoice #:** INV-2025-001
**Date:** Jan 18, 2025 | **Due:** Feb 15, 2025

| Description | Qty | Unit Price | Total |
|-------------|-----|-----------|-------|
| Enterprise Plan | 1 | $750.00 | $750.00 |
| Extra Users (5) | 5 | $10.00 | $50.00 |

**Subtotal:** $800.00
**Tax (16%):** $128.00
**Total:** $928.00
```

## Example 2: "Create an invoice for Acme Corp"

**User says:** "Generate an invoice for Acme Corp — Enterprise plan $750, 5 extra users at $10 each, 16% tax"

**Tool calls:**
```
1. create_invoice(
     vendor: {name: "Zavora AI", address: "Nairobi, Kenya", email: "billing@zavora.ai"},
     customer: {name: "Acme Corp", address: "123 Main St, San Francisco"},
     items: [
       {description: "Enterprise Plan - Jan 2025", quantity: 1, unit_price: 75000},
       {description: "Additional Users", quantity: 5, unit_price: 1000}
     ],
     tax_rate: 16,
     due_date: "2025-02-15",
     invoice_number: "INV-2025-001",
     payment_terms: "Net 30"
   )
   → {path: "/output/INV-2025-001.pdf", pages: 1, size: "48KB"}

2. hash_pdf(path: "/output/INV-2025-001.pdf")
   → {sha256: "a1b2c3d4..."}
```

**Response:**
```
✅ Invoice generated: INV-2025-001.pdf (48KB)

Subtotal: $800.00
Tax (16%): $128.00
Total: $928.00
Due: February 15, 2025

Integrity hash: a1b2c3d4...
Would you like me to email this to Acme with a payment link?
```

## Example 3: "This PDF has sensitive data — redact before sharing"

**User says:** "Scan report.pdf for PII and redact anything sensitive"

**Tool calls:**
```
1. scan_sensitive_data(path: "report.pdf")
   → {findings: [
       {type: "ssn", count: 3, pages: [2, 5], pattern: "XXX-XX-XXXX"},
       {type: "email", count: 8, pages: [1,2,3,4,5]},
       {type: "phone", count: 2, pages: [1, 3]}
     ]}

2. redact_pdf(path: "report.pdf", patterns: ["ssn", "phone"])
   → {redacted_count: 5, output: "report_redacted.pdf"}

3. remove_metadata(path: "report_redacted.pdf")
   → {removed: ["author", "creator", "creation_date", "modification_date"]}
```

**Response:**
```
🔒 Document secured for sharing

**PII Found:**
- 3 SSNs (pages 2, 5) → ✅ REDACTED
- 2 phone numbers (pages 1, 3) → ✅ REDACTED
- 8 emails (pages 1-5) → kept (not requested)

**Metadata:** Stripped (author, dates removed)
**Output:** report_redacted.pdf

⚠️ 8 email addresses remain. Want me to redact those too?
```

## Example 4: "Convert this PDF to markdown for editing"

**User says:** "Convert the quarterly report to markdown"

**Tool calls:**
```
1. profile_complexity(path: "q4-report.pdf")
   → {score: 2, notes: "Text-based, good structure, 3 tables"}

2. pdf_to_markdown(path: "q4-report.pdf")
   → {output: "q4-report.md", pages_converted: 12, tables_preserved: 3, headings_detected: 8}
```

**Response:**
```
✅ Converted to Markdown: q4-report.md

- 12 pages → single markdown file
- 8 headings preserved (H1-H3)
- 3 tables converted to markdown tables
- Complexity: 2/5 (clean extraction)

Ready for editing. Want me to create a Google Doc from this?
```

## Example 5: "Fill out this tax form"

**User says:** "Fill the W-9 form with our company details"

**Tool calls:**
```
1. detect_form_fields(path: "w9-blank.pdf")
   → {fields: [
       {name: "name", type: "text", value: ""},
       {name: "business_name", type: "text", value: ""},
       {name: "tax_classification", type: "checkbox", options: ["individual", "c_corp", "s_corp", "llc"]},
       {name: "ein", type: "text", value: ""},
       {name: "address", type: "text", value: ""}
     ]}

2. fill_form(path: "w9-blank.pdf", fields: {
     "name": "Zavora AI Inc",
     "business_name": "Zavora AI",
     "tax_classification": "c_corp",
     "ein": "XX-XXXXXXX",
     "address": "Nairobi, Kenya"
   })
   → {output: "w9-filled.pdf", fields_filled: 5}

3. flatten_form(path: "w9-filled.pdf")
   → {output: "w9-final.pdf", flattened: true}
```

**Response:**
```
✅ W-9 form filled and flattened

Fields completed: 5/5
- Name: Zavora AI Inc
- Business: Zavora AI
- Classification: C Corporation
- EIN: XX-XXXXXXX
- Address: Nairobi, Kenya

Form is now non-editable (flattened). Ready to submit.
```
