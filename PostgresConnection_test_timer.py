import psycopg2
import time

try:
    connection = psycopg2.connect(user="postgres",
                                  password="na",
                                  host="192.168.137.10",
                                  port="4090",
                                  database="pr")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")

    insert_query = '''DELETE FROM Parkeervak;
INSERT INTO Parkeervak VALUES (1);  '''

    insert_query2 = '''DELETE FROM Parkeervak;
    INSERT INTO Parkeervak VALUES (0);  '''
    a = 0
    for x in range(1000**2):
        x = insert_query
        cursor.execute(insert_query)
        connection.commit()
        print("1")
        time.sleep(0.5)
        cursor.execute(insert_query2)
        connection.commit()
        print("0 ")
        time.sleep(0.5)
        a += 1
        print("uitgevoerd: ",a)

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    # closing database connection.
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
