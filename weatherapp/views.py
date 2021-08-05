from django.shortcuts import render
from django.http import Http404
import json
import urllib.request


def index(request):   
    try:  
        if request.method == 'POST':
            city = request.POST['city']
            my_request = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=fbdbd7a6921d19bdac6295324eb4dc11").read()
            json_data = json.loads(my_request)
            context = {
                "city": city,
                "country": str(json_data['sys']['country']),
                "coordinates": str(json_data['coord']['lon']) + " " + str(json_data['coord']['lat']),
                # "temperature": str((int(json_data['main']['temp'])-273.15)) + "°C",
                "temperature": str(json_data['main']['temp']) + "K",
                "pressure": str(json_data['main']['pressure']),
                "humidity": str(json_data['main']['humidity']),
            }
        else: 
            context = {}
    except:
        raise Http404('Sorry!.. this country cannot be found')
    return render(request, "index.html", context)


