from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your actual API key from WeatherAPI
WEATHER_API_KEY = '11171966cd4348cf83470211241412'
WEATHER_API_URL = 'https://api.weatherapi.com/v1/current.json'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
    # Get the user input from the form
    location = request.form['location']
    
    # Fetch weather data for the entered location
    weather_data = get_weather_data(location)
    
    # If the API call fails, return an error message
    if not weather_data:
        return render_template('results.html', location=location, error="Could not fetch weather data.")
    
    # Render the results template with weather data
    return render_template('results.html', location=location, weather_data=weather_data)

def get_weather_data(location):
    # Set up the parameters for the API call
    params = {
        'key': WEATHER_API_KEY,
        'q': location  # This is where the user-inputted location goes
    }
    # Make the API request
    response = requests.get(WEATHER_API_URL, params=params)
    
    # Check if the response is successful
    if response.status_code == 200:
        return response.json()  # Return the JSON data
    else:
        return None  # Return None if there's an error

if __name__ == '__main__':
    app.run(debug=True)
