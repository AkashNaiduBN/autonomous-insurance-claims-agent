
def route_claim(extracted: dict, missing: list):
    description = extracted.get("description", "").lower()
    claim_type = extracted.get("claim_type", "").lower()
    damage = int(extracted.get("estimated_damage", 0))

    if missing:
        return "Manual Review", "Mandatory fields are missing"

    if any(word in description for word in ["fraud", "inconsistent", "staged"]):
        return "Investigation Flag", "Suspicious keywords detected in description"

    if claim_type == "injury":
        return "Specialist Queue", "Injury related claim"

    if damage < 25000:
        return "Fast-track", "Low estimated damage"

    return "Standard Processing", "Default routing applied"
