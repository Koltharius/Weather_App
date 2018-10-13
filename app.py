import requests
from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
    city = 'Granada, ES'

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}' \
          '&units=metric&appid=0bb5330da026388a756cd8b7746e44c3'

    r = requests.get(url.format(city)).json()
    weather = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }

    print(weather)

    return render_template('index.html', weather=weather)
