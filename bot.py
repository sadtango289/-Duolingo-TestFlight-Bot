import requests
from bs4 import BeautifulSoup
import os

# URL của trang TestFlight Duolingo
TESTFLIGHT_URL = "https://testflight.apple.com/join/Sq8bYSnJ"

# Hàm kiểm tra trạng thái slot trống
def is_slot_available():
    try:
        response = requests.get(TESTFLIGHT_URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return "Bản beta này đã đầy" not in soup.text
    except requests.RequestException as e:
        print(f"Lỗi khi truy cập trang TestFlight: {e}")
        return False

# Hàm gửi thông báo Telegram
def send_telegram_message(message):
