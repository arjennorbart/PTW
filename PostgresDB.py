import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                  password="na",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="AH")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")

    create_table_query = '''CREATE TABLE Parkeergarage
          (vestigingnummer INT NOT NULL,
          adres           VARCHAR(255)  ,
          plaats         VARCHAR(255),
          postcode       CHAR(6),
          PRIMARY KEY(vestigingnummer)     ); 

          CREATE TABLE Parkeervak
          (vaknummer       INT NOT NULL,
          hoogte           INT   ,
          verdieping       INT ,
          voertuigtype      VARCHAR(255),
          Parkeergaragevestigingnummer INT NOT NULL ,
          PRIMARY KEY(vaknummer)); 
          
          CREATE TABLE Informatiescherm
          (ID INT NOT NULL,
          verdieping           INT    ,
          locatie         VARCHAR ,
          Parkeergaragevestigingnummer INT NOT NULL ,
          PRIMARY KEY(ID)); 
          
          CREATE TABLE Betaalautomaat
          (automaatID INT NOT NULL,
          locatie           VARCHAR(255)    ,
          verdieping         INT ,
          Parkeergaragevestigingnummer INT NOT NULL ,
          PRIMARY KEY(automaatID));
 
ALTER TABLE Parkeervak ADD FOREIGN KEY(Parkeergaragevestigingnummer) REFERENCES Parkeergarage(vestigingnummer); 
ALTER TABLE Informatiescherm ADD FOREIGN KEY(Parkeergaragevestigingnummer) REFERENCES Parkeergarage(vestigingnummer); 
ALTER TABLE Betaalautomaat ADD FOREIGN KEY(Parkeergaragevestigingnummer) REFERENCES Parkeergarage(vestigingnummer);
'''

    cursor.execute(create_table_query)
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
