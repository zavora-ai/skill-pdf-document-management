#!/usr/bin/env python3
"""
PDF Security Scanner
Pre-checks a PDF for risks before processing: active content, PII patterns, corruption indicators.
Usage: python scan_pdf_risk.py '{"has_javascript": true, "has_embedded_files": 2, "pii_count": 5, "is_encrypted": false, "health": "ok"}'
"""
import json
import sys


def scan(data):
    risks = []
    risk_score = 0

    if data.get("has_javascript"):
        risks.append({"type": "active_content", "severity": "high", "detail": "JavaScript detected — may execute on open"})
        risk_score += 30

    embedded = data.get("has_embedded_files", 0)
    if embedded > 0:
        risks.append({"type": "embedded_files", "severity": "medium", "detail": f"{embedded} embedded file(s) — could contain malware"})
        risk_score += 15 * min(embedded, 3)

    pii = data.get("pii_count", 0)
    if pii > 0:
        risks.append({"type": "pii_detected", "severity": "high", "detail": f"{pii} PII instance(s) found — redact before sharing"})
        risk_score += 20

    if data.get("is_encrypted"):
        risks.append({"type": "encrypted", "severity": "info", "detail": "Document is encrypted — need password to process"})

    if data.get("health") != "ok":
        risks.append({"type": "corruption", "severity": "high", "detail": "PDF structure issues detected — repair before processing"})
        risk_score += 25

    risk_level = "critical" if risk_score >= 50 else "high" if risk_score >= 30 else "medium" if risk_score > 0 else "safe"

    actions = []
    if any(r["type"] == "active_content" for r in risks):
        actions.append("sanitize_pdf — remove JavaScript and actions")
    if any(r["type"] == "pii_detected" for r in risks):
        actions.append("redact_pdf — remove PII before sharing")
    if any(r["type"] == "corruption" for r in risks):
        actions.append("repair_pdf — fix structure before processing")
    if any(r["type"] == "embedded_files" for r in risks):
        actions.append("sanitize_pdf — remove embedded files")

    return {
        "risk_level": risk_level,
        "risk_score": min(risk_score, 100),
        "risks": risks,
        "recommended_actions": actions,
        "safe_to_process": risk_score < 30,
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python scan_pdf_risk.py \'{"has_javascript": true, "pii_count": 3}\'')
        sys.exit(1)
    print(json.dumps(scan(json.loads(sys.argv[1])), indent=2))
