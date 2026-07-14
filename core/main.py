import telebot

API_TOKEN="8917590739:AAFZw4MdabkZrj991Qo3r27qL0pHUzRBHcs"
ADMIN_ID = 8057427088

bot = telebot.TeleBot(API_TOKEN)

telebot.apihelper.proxy = {
    'http': 'socks5h://127.0.0.1:1080',
    'https': 'socks5h://127.0.0.1:1080'
}
telebot.apihelper.READ_TIMEOUT = 30
telebot.apihelper.CONNECT_TIMEOUT = 30

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hiii!Welcome")

@bot.message_handler(commands=['reply'])
def reply_to_user(message):
    if message.from_user.id != ADMIN_ID:
        return
    parts = message.text.split(' ', 2)
    user_id = int(parts[1])
    reply_text = parts[2]
    bot.send_message(user_id, reply_text)
    bot.reply_to(message, "message sent...")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, "sent.")
    user_info = f"پیام از: {message.from_user.first_name} (@{message.from_user.username})\nآیدی: {message.from_user.id}\nمتن: {message.text}"
    bot.send_message(ADMIN_ID, user_info)

bot.infinity_polling()