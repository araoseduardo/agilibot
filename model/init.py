import sqlite3

##########################################################
# Script que se encarga de carcar las tablas a la base de
# datos.
# El Servidor de Bototo usa sqlite.
##########################################################

schema_script = open('model/db.sql', 'rt')
schema_string = schema_script.read()  #.replace('\n', '')
connection = sqlite3.connect('bototo.db')
cursor = connection.cursor()
cursor.executescript(schema_string)
connection.close()