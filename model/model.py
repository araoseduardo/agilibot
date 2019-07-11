import sqlite3

##########################################################
# Script que contiene y encapsula las funciones para
# manipular la base de datos.
##########################################################

connection = sqlite3.connect('bototo.db')
cursor = connection.cursor()

connection.close()

def create_event(user_name, event_name, event_hora, event_detalle):
  connection = sqlite3.connect('bototo.db')
  cursor = connection.cursor()

  sql_get_user_id = "SELECT user_id FROM Usuarios WHERE telegram_name=?;"
  sql_add_evento = "INSERT INTO Eventos(creador, evento_name, evento_hora, evento_detalle) VALUES (?, ?, ?, ?);"

  connection.close()
  return "hola"


def delete_event(event_name):
  connection = sqlite3.connect('bototo.db')
  cursor = connection.cursor()

  # el nombre de eventos es unico?
  sql_statement = "DELETE FROM Eventos WHERE evento_name=?;"

  connection.close()
  return "hola"


def join_event(user_name, event_name):
  connection = sqlite3.connect('bototo.db')
  cursor = connection.cursor()

  sql_get_user_id = "SELECT user_id FROM Usuarios WHERE telegram_name=?;"
  sql_get_evento_id = "SELECT evento_id FROM Eventos WHERE evento_name=?;"
  sql_add_asistente = "INSERT INTO Asistentes(user_id, evento_id) VALUES (?, ?);"
  sql_get_asistentes_evento = "SELECT u.telegram_name FROM Asistentes AS a LEFT JOIN Usuarios AS u ON a.user_id=u.user_id WHERE a.evento_id=?;"

  connection.close()
  return "hola"


def list_events():
  connection = sqlite3.connect('bototo.db')
  cursor = connection.cursor()

  # falta cantidad de asistentes
  sql_get_all_events = "SELECT e.evento_name, e.evento_hora, u.telegram_name FROM Eventos AS e LEFT JOIN Usuarios AS u ON e.creador=u.user_id WHERE e.evento_name=?;"

  connection.close()
  return "hola"

