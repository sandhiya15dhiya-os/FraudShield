# 🛡️ FraudShield — Real-Time Banking Transaction Anomaly Detection

## Overview
FraudShield is a real-time fraud detection microservice built with Python Flask,
containerized using Docker, and deployed on AWS EC2 via Jenkins CI/CD pipeline.

## Architecture
```
GitHub → Jenkins CI/CD → Docker Build → AWS EC2 Deployment
```

## Tech Stack
| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| Containerization | Docker, Docker Compose |
| CI/CD | Jenkins |
| Cloud | AWS EC2 |
| Testing | Pytest |
| Version Control | GitHub |

## Detection Rules
| Rule | Condition | Risk Score |
|------|-----------|-----------|
| High Amount | > 50,000 | +40 |
| Odd Hours | 12AM - 4AM | +25 |
| High Risk Country | NG, KP, IR | +30 |
| Rapid Transactions | 3+ per minute | +35 |

**Fraud Threshold: Risk Score >= 50**

## API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | /health | Service health check |
| POST | /analyze | Analyze transaction |
| GET | /history | View all transactions |
| DELETE | /history/clear | Clear history |

## Sample Request
```json
POST /analyze
{
  "txn_id": "T001",
  "amount": 80000,
  "hour": 2,
  "country": "NG",
  "account_id": "ACC1",
  "timestamp": 1700000000
}
```

## Sample Response
```json
{
  "txn_id": "T001",
  "is_fraud": true,
  "risk_score": 95,
  "flags": ["HIGH_AMOUNT", "ODD_HOUR_TRANSACTION", "HIGH_RISK_COUNTRY"],
  "status": "FRAUD ALERT"
}
```

## How to Run Locally
```bash
pip install -r requirements.txt
python run.py
```

## How to Run with Docker
```bash
docker build -t fraudshield .
docker-compose up -d
```

## CI/CD Pipeline Stages
1. Checkout code from GitHub
2. Build Docker image
3. Deploy container
4. Health check