import telebot

TOKEN = "7230010485:AAFdgIQrOt14jLzLEVvKE0Q6BAyZNjZMZFY"  # Thay bằng Token bot từ @BotFather
GROUP_ID = -1002547636264  # Thay bằng ID nhóm Telegram (vd: -1001234567890)

bot = telebot.TeleBot(TOKEN)

users = {}  # Lưu trữ dữ liệu user tạm thời

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "🚀 Welcome to Movly Airdrop! 🎉\n\n"
                                      "👉 Please enter your **wallet address**:")

@bot.message_handler(func=lambda message: message.text and message.chat.id not in users)
def get_wallet(message):
    wallet = message.text
    users[message.chat.id] = {"wallet": wallet}
    bot.send_message(message.chat.id, "✅ Wallet saved!\n\n"
                                      "👉 Now, join our **Telegram group**: [Movly Chat](https://t.me/YOUR_GROUP_LINK) "
                                      "and then type **/done** here.")

@bot.message_handler(commands=['done'])
def check_join(message):
    user_status = bot.get_chat_member(GROUP_ID, message.chat.id)
    if user_status.status in ["member", "administrator", "creator"]:
        bot.send_message(message.chat.id, "🎉 Congrats! You have completed the Airdrop tasks!\n\n"
                                          "✅ Your data has been recorded.")
    else:
        bot.send_message(message.chat.id, "⚠️ You have not joined the Telegram group yet!\n\n"
                                          "👉 Join [Movly Chat](https://t.me/YOUR_GROUP_LINK) and try again.")

bot.polling()
