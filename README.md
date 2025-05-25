# Chapter 9: Monitoring & Observability for ML Systems

This repository implements drift detection, metrics logging, and real-time alerting pipelines for deployed ML models. It's designed to help teams keep their models honest and maintain performance in production.

## 📂 Project Structure

```bash
ch09-monitoring-observability/
├── scripts/
│   ├── log_features.py       # Logs input and prediction data
│   ├── drift_detector.py     # KS-test based drift detection
│   └── alerts.py             # Slack alert trigger
├── data/
│   ├── reference_data.csv    # Known good distribution
│   └── current_data.csv      # Incoming production data
└── .github/
    └── workflows/
        └── drift_check.yml   # GitHub Actions daily monitor

🚀 Features

✅ Feature & prediction logging to CSV (simulating cloud storage)
✅ Daily drift detection via GitHub Actions
✅ Slack alerts for drift anomalies
✅ Modular scripts, easy to integrate into existing pipelines
🔧 Setup

Add secrets to your GitHub repo:
AWS_ACCESS_KEY
SLACK_WEBHOOK
Modify S3 paths or simulate logs locally.
Enable GitHub Actions for automatic drift detection.
🧪 Example Usage

🚀 Features

✅ Feature & prediction logging to CSV (simulating cloud storage)
✅ Daily drift detection via GitHub Actions
✅ Slack alerts for drift anomalies
✅ Modular scripts, easy to integrate into existing pipelines
🔧 Setup

Add secrets to your GitHub repo:
AWS_ACCESS_KEY
SLACK_WEBHOOK
Modify S3 paths or simulate logs locally.
Enable GitHub Actions for automatic drift detection.
🧪 Example Usage

python scripts/log_features.py
python scripts/drift_detector.py
python scripts/alerts.py
📊 Real-World Application

Used for post-deployment monitoring in fraud detection, insurance claims, and retail forecast systems.

📘 From Production-Grade AI Systems, Chapter 9
✍🏽 Written by @RamadhanAI
