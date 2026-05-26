# PDF Cross-MCP Workflows

## PDF + Finance: Invoice-to-Cash

```
FINANCE: create_invoice(customer: "acme", items: [...]) → invoice data
PDF: create_invoice(vendor, customer, items, tax, due_date) → invoice.pdf
PDF: hash_pdf(path: "invoice.pdf") → integrity hash for audit
PAYMENTS: create_checkout_intent(amount: 55000, reference: "INV-2025-001")
EMAIL: send_email(to: "billing@acme.com", subject: "Invoice INV-2025-001", attachment: "invoice.pdf", body: "Pay online: [link]")
CRM: create_activity(type: "email", subject: "Invoice sent to Acme")
```

## PDF + CRM: Contract Lifecycle

```
CRM: get_deal(id: "d_123") → {customer: "Acme", value: 75000, terms: "Net 30"}
PDF: create_contract(
  parties: [{name: "Zavora AI", role: "Provider"}, {name: "Acme Corp", role: "Client"}],
  clauses: ["Service scope", "Payment terms: Net 30", "Duration: 12 months"],
  value: 75000
) → contract.pdf
PDF: add_watermark(path: "contract.pdf", text: "DRAFT") → draft version
EMAIL: send_email(to: customer, subject: "Contract for review", attachment: "contract_draft.pdf")
→ After approval:
PDF: remove_metadata(path: "contract_final.pdf")
PDF: encrypt_pdf(path: "contract_final.pdf", password: "...")
ARTIFACT: write_artifact(folder: "contracts/acme", name: "enterprise-2025.pdf")
CRM: move_deal_stage(id: "d_123", stage: "Closed Won")
```

## PDF + ERP: Purchase Order Flow

```
ERP: create_purchase_order(vendor: "WidgetCo", items: [...]) → PO data
PDF: create_purchase_order(buyer, vendor, items, terms, delivery_date) → po.pdf
PDF: add_page_numbers(path: "po.pdf")
PDF: hash_pdf(path: "po.pdf") → integrity
EMAIL: send_email(to: "orders@widgetco.com", subject: "PO #2025-045", attachment: "po.pdf")
```

## PDF + Security: Document Intake (Untrusted Sources)

```
PDF: inspect_pdf(path: "received.pdf") → structure
PDF: health_check_pdf(path: "received.pdf") → no corruption ✅
PDF: detect_active_content(path: "received.pdf") → {javascript: true, actions: 3}
PDF: sanitize_pdf(path: "received.pdf") → safe version (JS removed)
PDF: scan_sensitive_data(path: "received_safe.pdf") → {ssn: 2, credit_cards: 1}
SLACK: send_message(channel: "#security", text: "⚠️ Received PDF had JS + PII. Sanitized. PII flagged for review.")
```

## PDF + Knowledge Base: Document → Searchable Content

```
PDF: pdf_to_markdown(path: "policy.pdf") → markdown text
KB: create_draft(title: "Company Policy v3", body: markdown_content, category: "policies")
KB: publish_article(id: "draft_new")
```

## PDF + Legal: Bates Numbering + Redaction

```
PDF: merge_pdfs(paths: ["doc1.pdf", "doc2.pdf", "doc3.pdf"]) → combined.pdf
PDF: add_bates_numbers(path: "combined.pdf", prefix: "CASE-2025-", start: 1) → numbered
PDF: scan_sensitive_data(path: "combined_bates.pdf") → PII locations
PDF: redact_pdf(path: "combined_bates.pdf", patterns: ["ssn", "phone"]) → redacted
PDF: set_permissions(path: "combined_redacted.pdf", allow_print: true, allow_copy: false)
```

## PDF + HRIS: Certificate Generation

```
HRIS: get_employee(id: "emp_123") → {name: "Sarah Mitchell", title: "VP Engineering"}
PDF: create_certificate(
  recipient: "Sarah Mitchell",
  title: "Leadership Excellence Award",
  date: "2025-01-18",
  style: "elegant",
  issuer: "Zavora AI"
) → certificate.pdf
EMAIL: send_email(to: sarah, subject: "Congratulations! Your certificate", attachment: "certificate.pdf")
SLACK: send_message(channel: "#team", text: "🏆 Congrats Sarah Mitchell — Leadership Excellence Award!")
```
