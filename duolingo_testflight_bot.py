import requests
import os
import re
import time

# Lấy thông tin từ GitHub Actions Secrets
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

TESTFLIGHT_URL = "https://testflight.apple.com/join/Sq8bYSnJ"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def check_testflight():
    try:
        response = requests.get(TESTFLIGHT_URL, headers=HEADERS)
        if response.status_code != 200:
            return "⚠️ Lỗi khi kiểm tra TestFlight!"
        
        page_content = response.text
        if "This beta is full" in page_content:
            return "❌ TestFlight của Duolingo đã đầy."
        else:
            return "✅ Có chỗ trống trong TestFlight Duolingo!"
    except Exception as e:
        return f"⚠️ Lỗi: {e}"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, json=payload)

if __name__ == "__main__":
    status = check_testflight()
    send_telegram_message(status)
