import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user= 'nika',
         password = 'password',
         autocommit=True
         )

country_code_entered = input("Enter the country code (e.g., FI for Finland): ")
def get_airports_by_country(country_code):
    sql = f"select type from airport where iso_country = '{country_code}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    return data

def run_country_program():
    from collections import Counter
    airport_names = [name[0] for name in get_airports_by_country(country_code_entered)]
    grouped = Counter(airport_names)
    result = list(grouped.items())
    for airport, count in result:
        print(f"\n {count} {airport} airports")

print("Airports in FI:")
run_country_program()

