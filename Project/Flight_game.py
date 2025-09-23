import mysql.connector
import random

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user= 'nika',
         password = 'password',
         autocommit=True
         )


#Empty lists to store the routes of the player and the police
#Could be printed as a part of the summary at the end (wether you win or lose)
route_records_player = ["EFHK"]  #Player always starts at Helinki Airport, Finland
route_records_police = []
rounds_counter = 0


#Function to start the game
#Gives the player information about how the game works
def start_game():
    print("You just robbed the Bank of Finland, and the police are after you!!!")
    print("Your aim is to outrun the police by visiting 10 different airports in Europe.")
    print("Luckily for you, the police are not very honest, so you can bribe them ones.")
    print("Avoid the police that is trying to get you, do not get caught!")
    print("Remember to choose the most distant airport from your current location to not get caught!")
    print("The police will always be in the closest airport.")




#Returns a list of tuples, of all the airports in Europe, the country they are in, and there ICAO-code
#Also the coordinates of the airport
def get_airport_data():
    sql = """select airport.name, country.name, airport.ident, airport.latitude_deg, airport.longitude_deg 
             from airport, country
             where airport.iso_country = country.iso_country
             and country.continent = "EU"
          """
    cursor = connection.cursor()
    cursor.execute(sql)

    data = cursor.fetchall()
    return data

#Gets the coordinates of the players current location
def get_current_location(icao_code):
    sql = f"select latitude_deg, longitude_deg from airport where ident = '{icao_code}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    data = cursor.fetchone()
    return data



#Gets the new random selection of airports the user can choose from, every round
def rounds():
    data = get_airport_data()

    airport1 = random.randint(0, len(data))
    airport2 = random.randint(0, len(data))
    airport3 = random.randint(0, len(data))
    airport4 = random.randint(0, len(data))
    airport5 = random.randint(0, len(data))

    #Stores all the random airports in a dictionary
    locations_to_choose = {data[airport1]: None,
                           data[airport2]: None,
                           data[airport3]: None,
                           data[airport4]: None,
                           data[airport5]: None}

    #Prints the airports the player can choose from
    print("For your next trip you have these airports to choose from:\n ")
    for key in locations_to_choose.keys():
        print(f"{key[0]} : {key[1]} (airport code {key[2]})")


    next_location = input("\nPleace provide the airport code of the airport you want to travel to next: ").upper()


    #Tests the user input of the ICAO code
    #Ensures no typo errors
    isTrue = True
    while isTrue:
        if next_location == data[airport1][2] or next_location == data[airport2][2] or next_location == data[airport3][2] or next_location == data[airport4][2] or next_location == data[airport5][2]:
            route_records_player.append(next_location)
            isTrue = False
        else:
            next_location = input("\nPleace provide the airport code again (be sure to write it correctly): ").upper()


    current_location = get_current_location(next_location)

    # new code from nika
    # Calculating the distance between airports to choose the nearest one
    from geopy.distance import geodesic

    def run_airport_distance():
        # Get current location
        curr_lat, curr_lon = get_current_location(next_location)
        city_current = (curr_lat, curr_lon)

        nearest_city = None
        min_distance = float("inf")

        for key in locations_to_choose.keys():
            city_candidate = (key[3], key[4])
            distance_calculated = geodesic(city_current, city_candidate).km

            if distance_calculated < min_distance:
                min_distance = distance_calculated
                nearest_city = city_candidate

        return nearest_city

    police_location = run_airport_distance()

    return current_location, police_location



print(route_records_player)

