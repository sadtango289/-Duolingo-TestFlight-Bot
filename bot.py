print("Hello, Duolingo Bot!")
import requests
import os

# Lấy thông tin từ GitHub Secrets
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# URL TestFlight của Duolingo
TESTFLIGHT_URL = "https://testflight.apple.com/join/Sq8bYSnJ"

# Hàm gửi tin nhắn Telegram
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "disable_web_page_preview": True
    }
    response = requests.post(url, data=data)
    return response.json()

# Kiểm tra trạng thái TestFlight (giả sử có logic kiểm tra cập nhật)
def check_duolingo_update():
    # TODO: Thêm code kiểm tra cập nhật TestFlight
    update_available = True  # Giả sử có bản cập nhật mới

    if update_available:
        message = f"📢 Duolingo có bản cập nhật mới trên TestFlight!\n🔗 {TESTFLIGHT_URL}"
        send_telegram_message(message)

# Chạy kiểm tra
if __name__ == "__main__":
    check_duolingo_update()
