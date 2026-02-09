
import json
from extractor.fnol_extractor import extract_fields
from router.claim_router import route_claim

def process_document(text: str):
    extracted, missing = extract_fields(text)
    route, reasoning = route_claim(extracted, missing)

    output = {
        "extractedFields": extracted,
        "missingFields": missing,
        "recommendedRoute": route,
        "reasoning": reasoning
    }

    return output

if __name__ == "__main__":
    with open("sample_docs/sample_fnol.txt", "r") as f:
        text = f.read()

    result = process_document(text)
    print(json.dumps(result, indent=2))
