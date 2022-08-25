from django.shortcuts import render
import requests


def weather(request):
    app_id = '177f6d3726fc411f8bb183205222408'
    city = 'Москва'
    url = f"http://api.weatherapi.com/v1/current.json?key={app_id}&q={city}&aqi=no"
    res = requests.get(url).json()
    print(res)
    return render(request, template_name='weather/weather.html')

