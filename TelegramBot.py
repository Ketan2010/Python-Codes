#pip install pyTelegramBotAPI
import telebot
from emoji import emojize
import time
#get it from BotFather
bot_token='TOKEN'
#make instance
bot=telebot.TeleBot(token=bot_token)

#handle commands start with /
@bot.message_handler(commands=['hi'])
def send_welcome(message):
    bot.reply_to(message,'hello ketan!')


# Handles all text messages that match the regular expression
@bot.message_handler(regexp="hi")
def handle_message(message):
	bot.reply_to(message,'hello ketan')

@bot.message_handler(regexp="how are you?")
def handle_message(message):
	bot.reply_to(message,'Fine,What about You')


@bot.message_handler(regexp="fine")
def handle_message(message):
	bot.reply_to(message,'good')

@bot.message_handler(regexp="send me a joke")
def handle_message(message):
	bot.reply_to(message,'Why friend is called as Firend?')
    

@bot.message_handler(regexp="I don't know")
def handle_message(message):
	bot.reply_to(message,'Because we cannot call he as GirlFriend!')

@bot.message_handler(regexp="how funny")
def handle_message(message):
    bot.reply_to(message,'😍')
    

#in order to close telegram server connection
bot.polling()


