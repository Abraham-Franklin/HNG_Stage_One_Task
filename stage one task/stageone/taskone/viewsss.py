from django.shortcuts import render, redirect
from django.http import JsonResponse
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from .serializers import FetchDataSerializer

# Create your views here.

@api_view(['GET'])
def getData(request):
    context = {}
    if request.method == "GET":
        context['name'] = request.GET.get('name')
        city = request.GET.get('city')
    return render(request, 'taskone/index.html', context)

def hello(request):
    client_ip = request.META.get('REMOTE_ADDR', '127.0.0.1')

        api_key = "85971a067dd524d514061870d1d1502c"
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"

        response = requests.get(url)
        result = response.json()
        printjson.dumps(result, indent=4)
        if result.get('cod') != "404":
            context['temperature'] = result['list'][0]['main']['temp']
            context['description'] = result['list'][0]['weather'][0]['description']
            context['location'] = result['city']
        else:
            context['temperature'] = 'unknown'
            context['description'] = 'unknown'
            context['location'] = 'unknown'

        context['greeting'] = f"Hello, {context['name']}!, the temperature is {context['temperature']} degrees Celsius in {context['location']}."

    return render(request, 'taskone/hello.html', context)