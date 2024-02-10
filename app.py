import requests
from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')

def get_weather(city):
    url = f"https://goweather.herokuapp.com/weather/{city}"
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        current_temperature = weather_data["temperature"]
        wind_speed = weather_data["wind"]
        weather_description = weather_data["description"]
        forecast = weather_data["forecast"]
        return current_temperature, wind_speed, weather_description, forecast
    else:
        return None, None, None, None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form.get("city", "newyorkcity")
    else:
        city = "newyorkcity"

    current_temperature, wind_speed, weather_description, forecast = get_weather(city)
    return render_template("index.html", temperature=current_temperature, wind=wind_speed, description=weather_description, forecast=forecast, city=city)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
