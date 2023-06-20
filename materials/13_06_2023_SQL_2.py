# Задача 2. Подключиться к БД и вывести ее версию

import sqlite3

def get_connection():
  connection = sqlite3.connect('teachers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def read_database_version():
  try:
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT sqlite_version();")
    version = cursor.fetchone()
    print (version)
    close_connection(connection)
    print ("Вы подключись к версии Sqlite: ", version)
  except (Exception, sqlite3.Error) as error:
    print ('Ошибка в получении данных ', error)

read_database_version()