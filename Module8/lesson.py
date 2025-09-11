import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user= 'nika',
         password = 'password',
         autocommit=True
         )

def get_airports():
    sql = "SELECT name, ident FROM airport limit 2"
    cursor = connection.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    return data

airport = get_airports()
#print (airport)

def get_airports_by_municipality(city):
    sql = f"SELECT name, ident FROM airport where municipality = '{city}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    return data

done = get_airports_by_municipality("Helsinki")
print(done)




