from flask import Flask, render_template
import requests

app = Flask(__name__)

api_key = "25a8bd03eb02605ef5235259141e2e33"
location = "Round Rock"

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}")
format = response.json()

def kelvin_to_farenheit(k):
    c = (k-273.15)
    c *= (9/5)
    c += 32
    return round(c)

@app.route('/')
def index():
    return render_template("index.html", format = format, k_to_f = kelvin_to_farenheit)

if __name__ == "__main__":
    app.run(debug=False)