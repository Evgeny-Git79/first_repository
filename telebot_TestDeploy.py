import telebot

# Укажите токен вашего бота
#BOT_TOKEN = ('7676159196:AAFyTebgTA3jQe-mKCpE0HLRBiG6kFP8lDU')

# Создаем экземпляр бота
bot = telebot.TeleBot('7676159196:AAFyTebgTA3jQe-mKCpE0HLRBiG6kFP8lDU')

@bot.message_handler(commands = ['start'])
def start_message(message):
    chat_id = message.chat.id
    bot.reply_to(message, 'Привет! Я чат бот')

# Обработчик всех текстовых сообщений
@bot.message_handler(func=lambda message: True)
def respond_to_all_messages(message):
    bot.reply_to(message, "3333")

# Запускаем бота
if __name__ == "__main__":
    print("Бот запущен и работает на локальном сервере")
bot.infinity_polling(none_stop= True)