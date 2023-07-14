from flask import Flask, render_template, request, redirect, url_for
import os
from datetime import datetime
import requests
import math

app = Flask(__name__)

api_key = "2ce2a7b7b89974f01b5a48e1834d0a8e"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city_name = request.form['name']

        url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid="+api_key
        response = requests.get(url.format(city_name)).json()

        if str(response['cod']).startswith(('4','5')) == True:
            return redirect(url_for('index'))
        
        else:
            temp = round(((response['main']['temp']) - 273.15), 2)
            weather_description = response['weather'][0]['description']
            min_temp = round(((response['main']['temp_min']) - 273.15), 2)
            max_temp = round(((response['main']['temp_max']) - 273.15), 2)
            hmdt = response['main']['humidity']
            wind_speed = response['wind']['speed']
            date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
            icon = response['weather'][0]['icon']

            print(temp, weather_description, min_temp, max_temp, hmdt, wind_speed)
            return render_template('index.html',date_time=date_time, hmdt=hmdt, wind_speed=wind_speed, temp=temp,weather=weather_description,min_temp=min_temp,max_temp=max_temp,icon=icon, city_name = city_name)
    else:
        return render_template('index.html')
        

if __name__ == '__main__':
    app.run(debug=True)