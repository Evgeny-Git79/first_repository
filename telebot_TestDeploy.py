import telebot

# Укажите токен вашего бота
BOT_TOKEN = "7676159196:AAFyTebgTA3jQe-mKCpE0HLRBiG6kFP8lDU"

# Создаем экземпляр бота
bot = telebot.TeleBot(BOT_TOKEN)

# Обработчик всех текстовых сообщений
@bot.message_handler(func=lambda message: True)
def respond_to_all_messages(message):
    bot.reply_to(message, "Этот бот лежит на локальном сервере с автозапуском")

# Запускаем бота
if __name__ == "__main__":
    print("Бот запущен и работает на локальном сервере")
    bot.infinity_polling()