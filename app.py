from flask import Flask, request, jsonify
import requests
import os
 
app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name', 'Guest')
    client_ip = request.remote_addr


    # API keys
    weatherapi_key = os.getenv('WEATHERAPI_KEY')


    # Get location based on IP using ip-api.com
    ip_api_url = f"http://ip-api.com/json/{client_ip}"
    location_response = requests.get(ip_api_url).json()
    location = location_response.get("city", "Unknown location")

    # Get weather data for the location using weatherapi.com
    weather_url = f"http://api.weatherapi.com/v1/current.json?key={weatherapi_key}&q={location}"
    weather_response = requests.get(weather_url).json()
    temperature = weather_response["current"]["temp_c"]

    response = {
        "client_ip": client_ip,
        "location": location,
        "greeting": f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {location}"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
