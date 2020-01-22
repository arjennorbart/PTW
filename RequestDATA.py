import psycopg2
import time

def fetch_constant():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="na",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="bieb")
        cursor = connection.cursor()
        postgreSQL_select_Query = "SELECT * FROM Parkeervak;"

        cursor.execute(postgreSQL_select_Query)
        parking_spot = cursor.fetchone()
        print(parking_spot)

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        while True:
            starttime = time.time()
            time.sleep(5.0 - ((time.time() - starttime) % 60.0))
            fetch_constant()

fetch_constant()