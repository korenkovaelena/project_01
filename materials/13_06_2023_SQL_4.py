# Задача 4 . Вывести данные о школе и учителе, используя идентификатор школы и идентификатор учителя
import sqlite3

def get_connection():
  connection = sqlite3.connect('teachers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_school(school_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    query = """SELECT * FROM School WHERE School_Id = ?""" # '?' - это place holder
    cursor.execute(query,(school_id,)) # на место place holder-а '?' встает school_id
    records = cursor.fetchall()
    print ("Данные по школе:")
    for row in records:
      print ("ID школы:", row[0])
      print ("Название школы:", row[1])
      print ("Количество мест:", row[2])
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print ('Ошибка в получении данных ', error)

def get_teacher(teacher_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    query = """SELECT * FROM Teacher WHERE Teacher_Id = ?"""
    cursor.execute(query,(teacher_id,))
    records = cursor.fetchall()
    print ("Данные по учителю")
    for row in records:
      print ("ID учителя:", row[0])
      print ("Имя учителя:", row[1])
      print ("ID школы:", row[2])
      print ("Дата найма:", row[3])
      print ("Специальность:", row[4])
      print ("ЗП:", row[5])
      print ("Опыт работы:", row[6])
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print ('Ошибка в получении данных ', error)

get_school(3)
get_teacher(102)