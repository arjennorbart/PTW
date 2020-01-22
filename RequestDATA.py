import psycopg2

def fetch_constant():
    while True:
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="na",
                                          host="83.83.6.133",
                                          port="4090",
                                          database="pr")
            cursor = connection.cursor()
            postgreSQL_select_Query = "SELECT * FROM Parkeervak;"

            cursor.execute(postgreSQL_select_Query)
            parking_spot = cursor.fetchone()

        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)

        finally:
            yield parking_spot
