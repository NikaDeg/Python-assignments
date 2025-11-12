#Implement a backend service that gets the ICAO code of an airport and then returns the name and location of the airport
# in JSON format. The information is fetched from the airport database used on this course.
# For example, the GET request for EFHK would be: http://127.0.0.1:5000/airport/EFHK.
# The response must be in the format of: {"ICAO":"EFHK", "Name":"Helsinki-Vantaa Airport", "Location":"Helsinki"}.
import mysql.connector
import json
from flask import Flask, Response

app = Flask(__name__)
@app.route('/airport/<entered_code>')
def getting_location_info(entered_code):

    connection = mysql.connector.connect(
        host='127.0.0.1',
            port=3306,
            database='flight_game',
            user='nika',
            password='password',
            autocommit=True
    )
    try:
        def get_location(code):
            sql = f"select name, municipality from airport where ident = '{code}'"
            cursor = connection.cursor()
            cursor.execute(sql)
            data = cursor.fetchone()
            return data

        airp = get_location(entered_code)[0]
        city = get_location(entered_code)[1]
        response = {
            "ICAO": entered_code,
            "Name": airp,
            "Location": city
        }
        return response

    except ValueError:
        response = {
            "message": "Invalid number as addend",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response

@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)