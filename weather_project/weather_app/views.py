from django.shortcuts import render
import requests

import urllib
import json


# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')

        '''api_url = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=a52587924f9109d4710ac0bee2ab92fe').read()
        api_url2 = json.loads(api_url)
        print(api_url2)'''

        resp = requests.get(
            'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=a52587924f9109d4710ac0bee2ab92fe')
        data = resp.json()
        print(data)

        weather_data = {
            'city': city,
            'weather_description': data['weather'][0]['description'],
            'weather_temperature': data['main']['temp'],
            'weather_pressure': data['main']['pressure'],
            'weather_humidity': data['main']['humidity'],
            'weather_icon': data['weather'][0]['icon'],
        }
    else:
        weather_data = {
            'city': None,
            'weather_description': None,
            'weather_temperature': None,
            'weather_pressure': None,
            'weather_humidity': None,
            'weather_icon': None,
        }

    return render(request, 'weather_app/index.html', {'weather_data': weather_data})
