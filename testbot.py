import telebot

# Khởi tạo bot
bot = telebot.TeleBot("6342667549:AAGXrMmbZ5zcQs1B1s0V3KxPBrQmT2eN45Q")

# Xử lý tin nhắn "/start"
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Xin chào! Tôi là bot. Tôi biết bạn là ai rồi đó \n /send để nhận tin tiếp theo")

# Xử lý tin nhắn "/send"
@bot.message_handler(commands=['send'])
def send_message(message):
    bot.reply_to(message, "Đã gửi tin nhắn.")

# Lắng nghe và xử lý tin nhắn mới
bot.polling()