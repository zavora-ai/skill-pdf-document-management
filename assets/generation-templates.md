# PDF Generation Templates

## Invoice Parameters

```json
{
  "vendor": {
    "name": "Company Name",
    "address": "Street, City, Country",
    "email": "billing@company.com",
    "phone": "+254 700 000000",
    "logo_path": "optional/path/to/logo.png"
  },
  "customer": {
    "name": "Customer Name",
    "address": "Customer Address",
    "email": "customer@email.com"
  },
  "items": [
    {"description": "Line item description", "quantity": 1, "unit_price": 75000}
  ],
  "invoice_number": "INV-2025-001",
  "date": "2025-01-18",
  "due_date": "2025-02-15",
  "tax_rate": 16,
  "payment_terms": "Net 30",
  "notes": "Thank you for your business",
  "qr_code_data": "https://pay.company.com/inv/001"
}
```

## Certificate Styles

| Style | Best For |
|-------|----------|
| `classic` | Traditional awards, formal recognition |
| `modern` | Tech companies, startups |
| `elegant` | Executive awards, VIP recognition |
| `academic` | Course completion, training |
| `minimal` | Internal recognition, badges |

## Contract Structure

```json
{
  "title": "Service Agreement",
  "parties": [
    {"name": "Provider Co", "role": "Service Provider", "address": "..."},
    {"name": "Client Co", "role": "Client", "address": "..."}
  ],
  "clauses": [
    "1. Scope of Services: ...",
    "2. Payment Terms: Net 30 from invoice date",
    "3. Duration: 12 months from effective date",
    "4. Termination: 30 days written notice"
  ],
  "effective_date": "2025-02-01",
  "value": 75000,
  "signature_blocks": true
}
```
