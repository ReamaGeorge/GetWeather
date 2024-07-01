from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name', 'Guest')
    client_ip = request.remote_addr

    # Get location based on IP (example implementation, replace with an actual IP geolocation service)
    location = "New York"
    temperature = 11  # This would be fetched from a weather API in a real implementation

    response = {
        "client_ip": client_ip,
        "location": location,
        "greeting": f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {location}"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
