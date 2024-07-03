from django.shortcuts import render, redirect
from django.http import JsonResponse
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from .serializers import FetchDataSerializer

# Create your views here.

# @api_view(['GET'])
# def getData(request):
#     context = {}
#     return render(request, 'taskone/index.html', context)

@api_view(['GET', 'POST'])
def hello(request):
    context = {}
    if request.method == "POST":
        name = request.POST.get('name')
        city = request.POST.get('city')
        client_ip = request.META.get('REMOTE_ADDR', '127.0.0.1')

        api_key = "85971a067dd524d514061870d1d1502c"
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"

        response = requests.get(url)
        result = response.json()

        if result.get('cod') != "404":
            temperature = result['list'][0]['main']['temp']
            description = result['list'][0]['weather'][0]['description']
            location = city
            greeting = f"Hello, {name}!, the temperature is {temperature} degrees Celsius in {location}"

            response_data = {
                "client_ip": client_ip,
                "location": location,
                "greeting": greeting
            }

            return JsonResponse(response_data)
        else:
            temperature = 'unknown'
            description = 'unknown'
            location = 'unknown'
            response_data = {
                "client_ip": client_ip,
                "location": "unknown",
                "greeting": f"Hello, {name}!, the temperature is unknown in {city}"
            }

            return JsonResponse(response_data)
    else:
        return render(request, 'taskone/hello.html', context)