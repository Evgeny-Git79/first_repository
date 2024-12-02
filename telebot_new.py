import telebot
import datetime
import threading
import time
bot = telebot.TeleBot('token')
reminder_list = {}
@bot.message_handler(commands = ['start'])
def start_message(message):
    chat_id = message.chat.id
    bot.reply_to(message, 'Привет! Я чат бот, который будет присылать напоминания')
    reminder_list[chat_id] = {}
@bot.message_handler(commands = ['1_reminder'])
def start_message(message):
    bot.reply_to(message, 'Добавьте 1 напоминание')
    bot.register_next_step_handler(message, save_1_reminder)
def save_1_reminder(message):
    chat_id = message.chat.id
    first_reminder = message.text
    reminder_list[chat_id] ['first_reminder']= first_reminder
    bot.send_message(chat_id, f'Теперь укажи время в формате чч:мм')
    bot.register_next_step_handler(message, time_1_reminder)
def time_1_reminder(message):
    chat_id = message.chat.id
    time_first_reminder = message.text
    reminder_list[chat_id] ['time_first_reminder'] = time_first_reminder
    bot.send_message(chat_id, f'Напоминание сохранено!')
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()
@bot.message_handler(commands=['spisok'])
def spisok(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f'{reminder_list[chat_id]['first_reminder']} - {reminder_list[chat_id]['time_first_reminder']}')
def send_reminders(chat_id):
    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if now == reminder_list[chat_id] ['time_first_reminder']:
            bot.send_message(chat_id, f'{reminder_list[chat_id] ['first_reminder']}')
            time.sleep(61)
        time.sleep(1)
bot.polling(none_stop=True)
