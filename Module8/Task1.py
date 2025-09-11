import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user= 'nika',
         password = 'password',
         autocommit=True
         )

def get_location(code):
    sql = f"select name, municipality from airport where ident = '{code}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    data = cursor.fetchone()
    return data

code_entered = input("Enter the ICAO code of an airport: ")
result = get_location(code_entered)

print(f"Airport name: {result[0]}\nLocation: {result[1]}")