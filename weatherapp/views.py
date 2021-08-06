from django.shortcuts import render
import json
import urllib.request


def index(request):   
    try:  
        if request.method == 'POST':
            city = request.POST['city']
            my_request = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=fbdbd7a6921d19bdac6295324eb4dc11").read()
            json_data = json.loads(my_request)
            # converting temperature from kelvin to celcius 
            temp = round(int(json_data['main']['temp']) - 273.15)
            weather = json_data['weather']
            # since the information from the api is a list with a dict we have to convert it back to a dictionary before we can access the description key 
            weather_dict = {}
            for d in weather:
                weather_dict.update(d)

            context = {
                "city": city,
                "country": str(json_data['sys']['country']),
                "coordinates": str(json_data['coord']['lon']) + " " + str(json_data['coord']['lat']),
                "temperature": str(temp) + "°C",
                "pressure": str(json_data['main']['pressure']) + "Pa",
                "humidity": str(json_data['main']['humidity']),
                "weather_desc": weather_dict['description'],
            }
        else:
            context = {}
    except: 
        if city == "":
            error = ""
        else: 
            error = f"Sorry!... KB weather couldn't find '{ city }'"
        context = {"error": error}

    return render(request, "index.html", context)


