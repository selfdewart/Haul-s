import psycopg2
from config import host, user, password, db_name


try:
    # пытаемся подключиться к базе данных
      connection= psycopg2.connect(
         host=host, 
         user=user, 
         password=password, 
         database=db_name
         )
      connection.autocommit = True
    #   cursor = connection.cursor()

      with connection.cursor() as cursor:
           cursor.execute(
                "SELECT version();"
           )

           print(f"Server version: {cursor.fetchone()}")
      
# создание новой таблицы
     #  with connection.cursor() as cursor:
     #       cursor.execute(
     #            """CREATE TABLE users7(
     #            id serial PRIMARY KEY, 
     #            first_name varchar(50) NOT NULL, 
     #            nick_name varchar(50) NOT NULL)"""
     #       )

     #       connection.commit()
     #       print("[INFO] Table created succesfully")

     # insert data into table 
      with connection.cursor() as cursor:
           cursor.execute(
                """SELECT nick_name FROM users7 WHERE first_name = 'Oleg';"""
           )

           print(cursor.fetchone())




except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
