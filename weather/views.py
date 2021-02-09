from django.shortcuts import render,redirect,get_object_or_404
import requests
from .models import Add
# Create your views here.
def index(request):
  url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=8962ce22f91e70954e8d9a9e3ffbca7d"

  cities =  Add.objects.all()

  weather_data = []

  for city in cities:

    r = requests.get(url.format(city)).json()

    city_weather = {
      'city': city.name,
      'temperature': r['main']['temp'],
      'description': r['weather'][0]['description'],
      'icon': r['weather'][0]['icon'],
    }
    weather_data.append(city_weather)  
   
  context = {
      'weather_data':weather_data,
    }
  return render(request,'weather/weather.html',context)


  # 8962ce22f91e70954e8d9a9e3ffbca7d

def add(request):
    obj = request.POST['add']
    existing_city = Add.objects.filter(name = obj).count()
    if existing_city == 0:
      url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=8962ce22f91e70954e8d9a9e3ffbca7d"
      r = requests.get(url.format(obj)).json()
      if r['cod']==200:
        add = Add(name=obj)
        add.save()
        return redirect('/')
      else:
        err_msg = "Invalid city name!" 
        return render(request,'weather/msg.html',{'err':err_msg})
    else:
      err_msg = "City already exists!"
      return render(request,'weather/msg.html',{'err':err_msg})


def delete(request,city_name):
  new = get_object_or_404(Add,name=city_name)
  new.delete()
  return redirect('/')    