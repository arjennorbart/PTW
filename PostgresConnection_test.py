import psycopg2

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

    for x in range(1000**2):
        x = insert_query
        cursor.execute(insert_query)
        connection.commit()
        print("Table created successfully in PostgreSQL ")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    # closing database connection.
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
