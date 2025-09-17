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
    # select type, count(*) as airport_count from airport where iso_country '{country_code}' group by type order by airport_count desc
    cursor = connection.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    return data

def run_country_program():
    from collections import Counter
    airport_names = [name[0] for name in get_airports_by_country(country_code_entered)]
    grouped = Counter(airport_names)
    for airport, count in grouped.items():
        print(f"\n {count} {airport} airports")

print(f"Airports in {country_code_entered}:")
run_country_program()

