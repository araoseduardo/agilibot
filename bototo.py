# -*- coding: utf-8 -*-
import telegram
from telegram.ext import *
import requests
import json
import numpy

bototo = telegram.Bot(token="690440067:AAG6YMG5UjNz14nmnSbQFZEVuoc6KegKlL8")
bototo_updater = Updater(bototo.token)

lista_de_eventos=[]

print("hola")
response = requests.get("https://api.tronalddump.io/random/quote")
print(response.json()['value'])

def crear(bot, update, pass_chat_data=True):
	evento={}
	detalles=""
	msg=update.message.text
	b = msg.split(' ')[2:]
	for word in b:
		detalles += word
		detalles += ' '
	evento["nombre"]=update.message.text.split(" ")[1]
	evento["detalles"]=detalles
	evento["asistentes"]=0
	lista_de_eventos.append(evento)
	bot.sendMessage(chat_id=update.message.chat_id, text="Evento creado!")

def eventos(bot, update, pass_chat_data=True):
	mensaje=""
	for i in range(len(lista_de_eventos)):
		mensaje+=str(i+1)+". "+lista_de_eventos[i]["nombre"]+"\n"
		mensaje+="Asistentes: "+str(lista_de_eventos[i]["asistentes"])+"\n"
		mensaje+="Detalles: "+lista_de_eventos[i]["detalles"]+"\n"
		mensaje+="\n"
	bot.sendMessage(chat_id=update.message.chat_id, text=mensaje)

def unirse(bot, update, pass_chat_data=True):
	id=int(update.message.text.split(" ")[1])-1
	lista_de_eventos[id]["asistentes"]+=1
	msg="Unido! Por ahora hay "+str(lista_de_eventos[id]["asistentes"])+" asistentes en el evento "+lista_de_eventos[id]["nombre"]
	bot.sendMessage(chat_id=update.message.chat_id, text=msg)

def borrar(bot, update, pass_chat_data=True):
	id=int(update.message.text.split(" ")[1])-1
	lista_de_eventos.remove(id)
	msg="Evento eliminado"
	bot.sendMessage(chat_id=update.message.chat_id, text=msg)

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

borrar_handler = CommandHandler("borrar", borrar)
start_handler = CommandHandler("start", start)
crear_handler = CommandHandler("crear", crear)
eventos_handler = CommandHandler("eventos", eventos)
unirse_handler = CommandHandler("unirse",unirse)
tramp_handler = CommandHandler("tramp", tramp)
echo_handler = CommandHandler("echo", echo)
memetramp_handler = CommandHandler("memetramp", memetramp)
listener_handler = MessageHandler(Filters.text, listener)

dispatcher = bototo_updater.dispatcher


dispatcher.add_handler(borrar_handler)
dispatcher.add_handler(unirse_handler)
dispatcher.add_handler(crear_handler)
dispatcher.add_handler(eventos_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(listener_handler)
dispatcher.add_handler(tramp_handler)
dispatcher.add_handler(memetramp_handler)

bototo_updater.start_polling()
bototo_updater.idle()

while True:
	pass