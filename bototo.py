# -*- coding: utf-8 -*-
import telegram
from telegram.ext import *
import requests
import json
import numpy

bototo = telegram.Bot(token="710400482:AAH_GTahoZlqDqxWyEXKq-fmYSmqDd8nBqI")
bototo_updater = Updater(bototo.token)

lista_de_eventos=[]

print("hola")
response = requests.get("https://api.tronalddump.io/random/quote")
print(response.json()['value'])


def crear(bot, update, pass_chat_data=True):
    evento={}
    detalles=""
    msg=update.message.text
    b = msg.split(' ')[3:]
    for word in b:
        detalles += word
        detalles += ' '
    evento["nombre"]=update.message.text.split(" ")[1]
    evento["hora"] = update.message.text.split(" ")[2]
    evento["detalles"]=detalles
    evento["creador"] = update.message.from_user.username
    evento["asistentes"]=[]
    lista_de_eventos.append(evento)
    bot.sendMessage(chat_id=update.message.chat_id, text="Evento creado!")


def eventos(bot, update, pass_chat_data=True):
    mensaje=""
    for i in range(len(lista_de_eventos)):
        mensaje += str(i+1)+". "+lista_de_eventos[i]["nombre"] + ": \n"
        mensaje += "    ·Hora: " + lista_de_eventos[i]["hora"] + "\n"
        mensaje += "    ·Asistentes: " + str(len(lista_de_eventos[i]["asistentes"])) + "\n"
    bot.sendMessage(chat_id=update.message.chat_id, text=mensaje)


def detalle(bot, update, pass_chat_data=True):
    id = int(update.message.text.split(" ")[1]) - 1
    msg = lista_de_eventos[id]['nombre'] + ": \n\n"
    msg += "Hora: " + lista_de_eventos[id]["hora"] + "\n"
    msg += "Asistentes: " + "\n"

    for j in range(len(lista_de_eventos[id]["asistentes"])):
        msg += "    -" + lista_de_eventos[id]["asistentes"][j] + "\n"

    msg += "Detalles: " + lista_de_eventos[id]["detalles"] + "\n"
    msg += "Creador: " + lista_de_eventos[id]["creador"] + "\n"
    msg += "\n"
    bot.sendMessage(chat_id=update.message.chat_id, text=msg)


def unirse(bot, update, pass_chat_data=True):
    id=int(update.message.text.split(" ")[1])-1
    lista_de_eventos[id]["asistentes"].append(update.message.from_user.username)
    msg="Unido! Por ahora hay "+str(len(lista_de_eventos[id]["asistentes"]))+" asistentes en el evento "+lista_de_eventos[id]["nombre"]
    bot.sendMessage(chat_id=update.message.chat_id, text=msg)


def salirse(bot, update, pass_chat_data=True):
    id=int(update.message.text.split(" ")[1])-1
    lista_de_eventos[id]["asistentes"].remove(update.message.from_user.first_name + " " + update.message.from_user.last_name)
    msg="Se ha salido del grupo :C ! Ahora hay "+str(len(lista_de_eventos[id]["asistentes"]))+" asistentes en el evento "+lista_de_eventos[id]["nombre"]
    bot.sendMessage(chat_id=update.message.chat_id, text=msg)


def borrar(bot, update, pass_chat_data=True):
    id=int(update.message.text.split(" ")[1])-1
    del lista_de_eventos[id]
    msg="Evento eliminado"
    bot.sendMessage(chat_id=update.message.chat_id, text=msg)


def listener(bot, update):
    id = update.message.chat_id
    mensaje = update.message.text
    print("ID : " + str(id) + "MENSAJE : " + mensaje)


def start(bot, update, pass_chat_data=True):
    update.message.chat_id
    bot.sendMessage(chat_id=update.message.chat_id, text="Hola soy bototo, vuestro organizador de eventos :)")


def echo(bot,update,pass_chat_data=True):
    a = ''
    msg=update.message.text
    b = msg.split(' ')[1:]
    for word in b:
        a += ' '
        a += word

    bot.sendMessage(chat_id=update.message.chat_id, text=a)


detalle_handler = CommandHandler("detalle", detalle)
borrar_handler = CommandHandler("borrar", borrar)
start_handler = CommandHandler("start", start)
crear_handler = CommandHandler("crear", crear)
eventos_handler = CommandHandler("eventos", eventos)
salirse_handler = CommandHandler("salirse",salirse)
unirse_handler = CommandHandler("unirse",unirse)
echo_handler = CommandHandler("echo", echo)
listener_handler = MessageHandler(Filters.text, listener)

dispatcher = bototo_updater.dispatcher

dispatcher.add_handler(detalle_handler)
dispatcher.add_handler(borrar_handler)
dispatcher.add_handler(unirse_handler)
dispatcher.add_handler(salirse_handler)
dispatcher.add_handler(crear_handler)
dispatcher.add_handler(eventos_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(listener_handler)

bototo_updater.start_polling()
bototo_updater.idle()

while True:
    pass