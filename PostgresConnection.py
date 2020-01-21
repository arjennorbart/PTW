import psycopg2

try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "na",
                                  host = "192.168.137.101",
                                  port = "5432",
                                  database = "pr")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    create_table_query = '''CREATE TABLE bier
          (kaas INT PRIMARY KEY     NOT NULL,
          borrelnootjes           TEXT    NOT NULL,
          bittergarnituur         REAL); '''

    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
