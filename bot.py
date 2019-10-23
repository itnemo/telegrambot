import telebot
import constans

bot = telebot.TeleBot(constans.token)

#bot.send_message(852311002, "Hello")

upd = bot.get_updates()
#print(upd)

last_upd = upd[-1]
message_from_user = last_upd.message
#print(message_from_user)

@bot.message_handler(content_types=['commands'])
def handle_command(message) : bot.send_message(852311002, "Hello")

bot.polling(none_stop=True, interval=0)