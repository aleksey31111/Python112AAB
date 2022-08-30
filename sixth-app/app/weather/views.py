from django.shortcuts import render, redirect, get_object_or_404
import requests
from .models import City
from .forms import CityForm


def weather(request):
    app_id = '177f6d3726fc411f8bb183205222408'
    if request.method == "POST":
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    # city = 'Москва'
    cities = City.objects.all()

    all_cities = []
    for city in cities:
        url = f"http://api.weatherapi.com/v1/current.json?key={app_id}&q={city.name}&aqi=no"
        res = requests.get(url).json()
        # print(res)

        try:
            city_info = {
                'city_pk': city.id,
                'city': city.name,
                'temp': res["current"]["temp_c"],
                'icon': res["current"]["condition"]["icon"],
            }

        except KeyError:
            city_info = {
                'city_pk': city.id,
                'city': "Такого города НЕТ",
                'temp': "-",
            }
        all_cities.append(city_info)

    context = {
        # 'info': city_info
        'all_info': all_cities,
        'form': form,
    }
    return render(request, template_name='weather/weather.html', context=context)


def deletecity(request, city_pk):
    city = get_object_or_404(City, pk=city_pk)
    if request.method == 'POST':
        city.delete()
        return redirect("weather")
