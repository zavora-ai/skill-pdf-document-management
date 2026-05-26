# PDF Document Management Skill

> The complete PDF operating layer for AI agents — 57 tools for inspecting, extracting, generating, converting, manipulating, securing, and filling PDFs. Pure Rust, zero dependencies, local-only.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--pdf-green)](https://github.com/zavora-ai/mcp-pdf)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

This skill orchestrates **57 PDF tools** across 7 categories into governed document workflows — from inspecting unknown PDFs to generating professional invoices to redacting PII before sharing.

| Workflow | Tool Calls | What It Achieves |
|----------|-----------|------------------|
| Inspect & Classify | 2-4 | Understand any PDF (type, health, features) |
| Extract Data | 2-3 | Text, tables, metadata, key-values from PDFs |
| Generate Documents | 1-2 | Professional invoices, contracts, certificates |
| Convert Formats | 1 | PDF ↔ Markdown, HTML, JSON, CSV, Images |
| Manipulate Pages | 1-2 | Merge, split, rotate, compress, watermark |
| Secure & Protect | 2-3 | PII scan, redaction, encryption, sanitization |
| Fill Forms | 2-3 | Detect fields, fill, flatten |

### Without this skill:
- Unknown PDFs opened without security checks
- Data extracted manually (copy-paste from PDFs)
- Invoices created in Word then exported (inconsistent)
- PII shared externally without detection
- Forms filled by hand, one field at a time

### With this skill:
- Every unknown PDF inspected + classified before processing
- Tables and key-values extracted as structured JSON
- Professional documents generated directly (invoice, contract, certificate)
- PII scanned and truly redacted (content removed, not masked)
- Forms auto-detected, filled, and flattened in 3 calls

## Installation

### Claude Code
```bash
git clone https://github.com/zavora-ai/skill-pdf-document-management.git \
  ~/.skills/skills/pdf-document-management
```

### ADK-Rust
```bash
cp -r pdf-document-management /path/to/project/.skills/skills/
```

### Claude.ai
Download ZIP → Settings > Capabilities > Skills > Upload

## Requirements

**Required:**
- `mcp-pdf` server (v3.0.0+, 57 tools, 17MB binary, zero system dependencies)

**Cross-MCP integrations:**
- `mcp-finance` — invoice data → PDF generation
- `mcp-email` — send generated PDFs as attachments
- `mcp-crm` — contract generation from deal data
- `mcp-erp` — purchase order PDF generation
- `mcp-slack` — security alerts on risky PDFs
- `mcp-artifact-store` — archive generated documents

## Folder Structure

```
pdf-document-management/
├── SKILL.md                       # 322 lines — 7 workflows, decision tree, cross-MCP
├── scripts/
│   └── scan_pdf_risk.py           # Pre-processing risk assessment
├── assets/
│   └── generation-templates.md    # Invoice, certificate, contract parameter templates
├── references/
│   ├── tool-sequences.md          # All 57 tools categorized with exact call patterns
│   ├── cross-mcp-workflows.md     # PDF + Finance + CRM + ERP + Security + KB
│   └── examples.md                # 5 real scenarios with full traces
├── README.md
└── LICENSE
```

## How It Works

### Decision Tree

```
User request arrives
├── "what is this PDF"? → Inspect & Classify
├── "extract", "get data"? → Extract (text/tables/metadata)
├── "create", "generate"? → Generate (invoice/contract/certificate)
├── "convert", "to markdown"? → Convert
├── "merge", "split", "compress"? → Manipulate
├── "secure", "redact", "encrypt"? → Secure
├── "fill form"? → Forms
└── Unknown PDF? → Always inspect first
```

### The Security-First Principle

For PDFs from untrusted sources:
1. `health_check_pdf` — detect corruption
2. `detect_active_content` — find JavaScript/executables
3. `sanitize_pdf` — remove dangerous content
4. `scan_sensitive_data` — detect PII
5. Only then proceed with extraction/processing

## Example

**User:** "Create an invoice for Acme Corp — Enterprise plan $750, 5 extra users at $10, 16% tax"

**Agent behavior:**
1. Calls `create_invoice` with structured parameters
2. Calls `hash_pdf` for integrity verification
3. Offers to email with payment link

**Result:**
```
✅ Invoice generated: INV-2025-001.pdf (48KB)
Subtotal: $800.00 | Tax (16%): $128.00 | Total: $928.00
Due: February 15, 2025
Integrity: SHA-256 verified

Would you like me to email this to Acme with a payment link?
```

## Success Criteria

| Metric | Target |
|--------|--------|
| Trigger rate | 95% on PDF-related queries |
| Extraction accuracy | 100% on text-based PDFs |
| Generation quality | Cross-viewer compatible (Safari, Chrome, Acrobat) |
| Security | PII always scanned before external sharing |
| Redaction | True content removal (not visual masking) |

## Scripts

### `scan_pdf_risk.py`
Pre-processing risk assessment for unknown PDFs:
```bash
python scripts/scan_pdf_risk.py '{"has_javascript": true, "pii_count": 5, "health": "ok"}'
# → {"risk_level": "high", "safe_to_process": false, "recommended_actions": ["sanitize_pdf", "redact_pdf"]}
```

## MCP Server Compatibility

Designed for [mcp-pdf](https://github.com/zavora-ai/mcp-pdf) v3.0.0+:

| Category | Tools | Count |
|----------|-------|-------|
| Inspect | inspect, classify, health_check, detect_features, profile, count, info, repair | 8 |
| Extract | text, page_text, metadata, tables, images, bookmarks, annotations, key_values | 8 |
| Generate | invoice, receipt, quote, statement, PO, letter, certificate, report, contract | 9 |
| Convert | pdf→md, pdf→html, pdf→json, pdf→csv, md→pdf, images→pdf | 6 |
| Manipulate | merge, split, split_bookmarks, rotate, crop, reorder, delete, compress, watermark, headers, numbers | 11 |
| Security | hash, encrypt, decrypt, permissions, scan_pii, redact, sanitize, remove_metadata, detect_active | 9 |
| Forms | detect_fields, fill, flatten, fill_flat, describe_layout | 5 |
| **Total** | | **57** |

## Related Skills

- [skill-finance-accounting](https://github.com/zavora-ai/skill-finance-accounting) — Invoice data source
- [skill-crm-customer-management](https://github.com/zavora-ai/skill-crm-customer-management) — Contract triggers
- [skill-email-management](https://github.com/zavora-ai/skill-email-management) — PDF delivery
- [skill-erp-operations](https://github.com/zavora-ai/skill-erp-operations) — PO generation

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;" alt=""/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0

---

Part of the [ADK-Rust Enterprise](https://enterprise.adk-rust.com) skills ecosystem. Built with ❤️ by [Zavora AI](https://zavora.ai)
