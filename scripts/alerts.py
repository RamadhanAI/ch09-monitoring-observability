
import os
import requests

def notify_slack(message):
    webhook = os.getenv("SLACK_WEBHOOK")
    if webhook:
        requests.post(webhook, json={"text": f"🚨 ALERT: {message}"})

if __name__ == "__main__":
    notify_slack("Test alert from monitoring system.")
