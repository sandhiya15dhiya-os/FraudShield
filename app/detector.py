RULES = {
    "max_amount": 50000,
    "max_per_minute": 3,
    "odd_hours": (0, 4),
    "blacklisted_countries": ["NG", "KP", "IR"],
}

def detect_anomaly(transaction: dict, history: list) -> dict:
    flags = []
    risk_score = 0

    if transaction["amount"] > RULES["max_amount"]:
        flags.append("HIGH_AMOUNT")
        risk_score += 40

    h = transaction["hour"]
    if RULES["odd_hours"][0] <= h <= RULES["odd_hours"][1]:
        flags.append("ODD_HOUR_TRANSACTION")
        risk_score += 25

    if transaction.get("country") in RULES["blacklisted_countries"]:
        flags.append("HIGH_RISK_COUNTRY")
        risk_score += 30

    recent = [
        t for t in history
        if t["account_id"] == transaction["account_id"]
        and abs(t["timestamp"] - transaction["timestamp"]) <= 60
    ]
    if len(recent) >= RULES["max_per_minute"]:
        flags.append("RAPID_TRANSACTIONS")
        risk_score += 35

    is_fraud = risk_score >= 50

    return {
        "txn_id": transaction["txn_id"],
        "is_fraud": is_fraud,
        "risk_score": risk_score,
        "flags": flags,
        "status": "🚨 FRAUD ALERT" if is_fraud else "✅ LEGITIMATE"
    }