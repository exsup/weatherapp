from django.shortcuts import render
import json
import urllib
# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST ['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=8bc94e903d4d98d75c22281e655b71f5').read()
        json_data=json.loads(res)
        data = {
            "Country_code": str(json_data['sys']['country']),
            "Cordinate": str(json_data['coord']['lon'])+ '' + str(json_data['coord']['lat']),
            "Temp": str(json_data['main']['temp']) + 'k',
            "Pressure": str(json_data['main']['pressure']),
            "Humidity":str (json_data['main']['humidity']),
        }
    else:
        city=""
        data = {}
    return render(request, 'index.html', {'city':city, 'data': data})