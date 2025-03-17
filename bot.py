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
        # Kiểm tra nếu trang chứa thông báo "Bản beta này đã đầy"
        return "Bản beta này đã đầy" not in soup.text
    except requests.RequestException as e:
        print(f"Lỗi khi truy cập trang TestFlight: {e}")
        return False

# Hàm gửi thông báo Telegram
def send_telegram_message(message):
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    if not bot_token or not chat_id:
        print("Thiếu TELEGRAM_BOT_TOKEN hoặc TELEGRAM_CHAT_ID.")
        return
    send_text = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {'chat_id': chat_id, 'text': message, 'parse_mode': 'Markdown'}
    try:
        response = requests.post(send_text, data=payload)
        response.raise_for_status()
        print("Đã gửi thông báo Telegram.")
    except requests.RequestException as e:
        print(f"Lỗi khi gửi thông báo Telegram: {e}")

# Kiểm tra và gửi thông báo nếu có slot trống
if __name__ == "__main__":
    if is_slot_available():
        message = f"Duolingo có bản cập nhật mới trên TestFlight!\n🔗 {TESTFLIGHT_URL}"
        send_telegram_message(message)
    else:
        print("Hiện tại không còn slot trống trên TestFlight cho Duolingo.")
