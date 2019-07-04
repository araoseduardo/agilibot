# -*- coding: utf-8 -*-
import telegram
from telegram.ext import *
import requests
import json
import numpy

bototo = telegram.Bot(token="690440067:AAG6YMG5UjNz14nmnSbQFZEVuoc6KegKlL8")
bototo_updater = Updater(bototo.token)

print("hola")
response = requests.get("https://api.tronalddump.io/random/quote")
print(response.json()['value'])

def listener(bot, update):
	id = update.message.chat_id
	mensaje = update.message.text
	print("ID : " + str(id) + "MENSAJE : " + mensaje)

def start(bot, update, pass_chat_data=True):
	update.message.chat_id
	bot.sendMessage(chat_id=update.message.chat_id, text="hola adios penes tetas")


def tramp(bot, update, pass_chat_data=True):
	update.message.chat_id
	response = requests.get("https://api.tronalddump.io/random/quote")
	quote = response.json()['value']
	bot.sendMessage(chat_id=update.message.chat_id, text=quote)

def memetramp(bot, update, pass_chat_data=True):
	update.message.chat_id
	r = numpy.random.randint(1, 16)
	s = "http://cdn.pichunter.com/352/2/3522658/3522658_"+ str(r) +"_o.jpg"
	bot.sendPhoto(chat_id= update.message.chat_id, photo = s)

def echo(bot,update,pass_chat_data=True):
	a = ''
	msg=update.message.text
	b = msg.split(' ')[1:]
	for word in b:
		a += ' '
		a += word

	bot.sendMessage(chat_id=update.message.chat_id, text=a)

start_handler = CommandHandler("start", start)
tramp_handler = CommandHandler("tramp", tramp)
echo_handler = CommandHandler("echo", echo)
memetramp_handler = CommandHandler("memetramp", memetramp)
listener_handler = MessageHandler(Filters.text, listener)

dispatcher = bototo_updater.dispatcher

dispatcher.add_handler(echo_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(listener_handler)
dispatcher.add_handler(tramp_handler)
dispatcher.add_handler(memetramp_handler)

bototo_updater.start_polling()
bototo_updater.idle()

while True:
	pass