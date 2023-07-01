import telebot
from telebot import types

# Khởi tạo bot
bot = telebot.TeleBot("6342667549:AAGXrMmbZ5zcQs1B1s0V3KxPBrQmT2eN45Q")

# Xử lý tin nhắn "/start"
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Tạo danh sách các lựa chọn
    options = ['/start','/receive']

    # Tạo menu thả xuống cho các lựa chọn
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for option in options:
        markup.add(types.KeyboardButton(option))

    # Gửi tin nhắn với danh sách thả xuống
    bot.reply_to(message, "Chọn một tùy chọn:", reply_markup=markup)

# Xử lý tin nhắn "/send"
@bot.message_handler(commands=['send'])
def send_message(message):
    bot.reply_to(message, "Đã gửi tin nhắn.")

# Xử lý tin nhắn "/receive"
@bot.message_handler(commands=['receive'])
def send_file(message):
    # Tải tệp từ máy tính của bạn
    file_path = r"E:\TeraBoxDownload\anhCV.jpg"
    with open(file_path, "rb") as file:
        # Gửi tệp đính kèm trong tin nhắn Telegram
        bot.send_photo(message.chat.id, file)

# Lắng nghe và xử lý tin nhắn mới
bot.polling()