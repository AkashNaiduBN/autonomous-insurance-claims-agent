
import re

MANDATORY_FIELDS = [
    "policy_number",
    "policyholder_name",
    "incident_date",
    "incident_location",
    "claim_type",
    "estimated_damage"
]

def extract_fields(text: str):
    extracted = {}

    patterns = {
        "policy_number": r"POLICY NUMBER[:\s]+([A-Z0-9-]+)",
        "policyholder_name": r"NAME OF INSURED.*?\n([A-Za-z ]+)",
        "incident_date": r"DATE OF LOSS.*?(\d{2}/\d{2}/\d{4})",
        "incident_location": r"LOCATION OF LOSS.*?\n(.+)",
        "description": r"DESCRIPTION OF ACCIDENT.*?\n(.+)",
        "estimated_damage": r"ESTIMATE AMOUNT[:\s]+\$?(\d+)",
        "claim_type": r"CLAIM TYPE[:\s]+([A-Za-z]+)"
    }

    for field, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if match:
            extracted[field] = match.group(1).strip()

    missing = [f for f in MANDATORY_FIELDS if f not in extracted]

    return extracted, missing
