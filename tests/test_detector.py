from app.detector import detect_anomaly

def test_high_amount_fraud():
    txn = {
        "txn_id": "T001", "amount": 80000,
        "hour": 14, "country": "IN",
        "account_id": "ACC1", "timestamp": 1700000000
    }
    result = detect_anomaly(txn, [])
    assert result["is_fraud"] == True
    assert "HIGH_AMOUNT" in result["flags"]

def test_legitimate_transaction():
    txn = {
        "txn_id": "T002", "amount": 1000,
        "hour": 10, "country": "IN",
        "account_id": "ACC2", "timestamp": 1700000000
    }
    result = detect_anomaly(txn, [])
    assert result["is_fraud"] == False

def test_odd_hour_and_high_risk_country():
    txn = {
        "txn_id": "T003", "amount": 2000,
        "hour": 2, "country": "NG",
        "account_id": "ACC3", "timestamp": 1700000000
    }
    result = detect_anomaly(txn, [])
    assert result["is_fraud"] == True
    assert "ODD_HOUR_TRANSACTION" in result["flags"]
    assert "HIGH_RISK_COUNTRY" in result["flags"]