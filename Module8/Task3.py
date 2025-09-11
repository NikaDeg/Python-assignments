import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user= 'nika',
         password = 'password',
         autocommit=True
         )

def get_airport_coordinates(icao_code):
    sql = f"select latitude_deg, longitude_deg from airport where ident = '{icao_code}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    data = cursor.fetchone()
    return data

code_first = input("Enter the ICAO code of the first airport: ")
code_second = input("Enter the ICAO code of the second airport: ")

from geopy.distance import geodesic

def run_airport_distance():
    city_first = (get_airport_coordinates(code_first))
    city_second = (get_airport_coordinates(code_second))
    distance = geodesic(city_first, city_second).km
    return distance
airport_distance = run_airport_distance()
print(f"Distance between {code_first} and {code_second}: {airport_distance:.2f} kilometers")

# import mysql.connector
#
# connection = mysql.connector.connect(
#          host='127.0.0.1',
#          port= 3306,
#          database='flight_game',
#          user= 'nika',
#          password = 'password',
#          autocommit=True
#          )
#
# def get_airport_coordinates(icao_code):
#     sql = f"select latitude_deg, longitude_deg from airport where ident = '{icao_code}'"
#     cursor = connection.cursor()
#     cursor.execute(sql)
#     data = cursor.fetchone()
#     return data
# code_first = input("Enter the ICAO code of the first airport: ")
# code_second = input("Enter the ICAO code of the second airport: ")
#
# city_first = (get_airport_coordinates(code_first))
# city_second = (get_airport_coordinates(code_second))
#
# from geopy.distance import geodesic
#
# def run_airport_distance(town_one, town_two):
#     distance = geodesic(town_one, town_two).km
#     return distance
# airport_distance = run_airport_distance(city_first, city_second)
# print(f"Distance between {code_first} and {code_second}: {airport_distance:.2f} kilometers")

