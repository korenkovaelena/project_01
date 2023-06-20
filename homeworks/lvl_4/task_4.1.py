# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:


import sqlite3

# connection = sqlite3.connect('teachers.db')
# cursor = connection.cursor()
# query = """CREATE TABLE Students (
# Student_Id INTEGER NOT NULL,
# Student_Name TEXT NOT NULL,
# School_Id INTEGER NOT NULL PRIMARY KEY);"""
# cursor.execute(query)
# connection.commit()
# connection.close()


# connection = sqlite3.connect('teachers.db') 
# cursor = connection.cursor()
# query = """INSERT INTO Students (Student_Id, Student_Name, School_Id)
# VALUES
# (201, 'Иван', '1'),
# (202, 'Петр', '2'),
# (203, 'Анастасия', '3'),
# (204, 'Игорь', '4');
# """
# cursor.execute(query)
# connection.commit()
# connection.close()



# С помощью JOIN
def get_info(Student_Id):
    try:
        connection = sqlite3.connect('teachers.db') 
        cursor = connection.cursor()
        query = """SELECT Student_Id, Student_Name, Students.School_Id, School_Name  FROM School
    JOIN Students on  Students.School_Id = School.School_id
    where Students.student_id = ?;"""
        cursor.execute(query,(Student_Id,))
        records = cursor.fetchall()
        # print (records)
        for row in records:
            print ("ID Студента:", row[0])
            print('Имя студента:', row[1])
            print("ID школы:", row[2])
            print('Название школы:', row[3])
    except (Exception, sqlite3.Error) as error:
        print ('Ошибка в получении данных ', error)




# С помощью функций
def get_info_functions(Student_Id):
    try:
        connection = sqlite3.connect('teachers.db') 
        cursor = connection.cursor()
        query = "SELECT * FROM Students WHERE Student_Id = ?"
        cursor.execute(query,(Student_Id,))
        records = cursor.fetchall()
        for row in records:
            print ("ID Студента:", row[0])
            print('Имя студента:', row[1])
            print("ID школы:", row[2])
            print('Название школы:', get_school_name(row[2]))
    except (Exception, sqlite3.Error) as error:
        print ('Ошибка в получении данных ', error)
        

def get_school_name(School_Id):
    try:
        connection = sqlite3.connect('teachers.db') 
        cursor = connection.cursor()
        query = "SELECT * FROM School WHERE School_Id = ?"
        cursor.execute(query,(School_Id,))
        records = cursor.fetchone()
        return records[1]
    except (Exception, sqlite3.Error) as error:
        print ('Ошибка в получении данных ', error)


x = input('Введите ID Студента: ')
# get_info(x)
get_info_functions(x)