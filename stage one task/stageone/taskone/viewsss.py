# from django.shortcuts import render, redirect
# from django.http import JsonResponse
# import requests
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# # from .serializers import FetchDataSerializer

# # Create your views here.
# city = None
# name = None

# @api_view(['GET'])
# def getData(request):
#     global city
#     global name
#     context = {}
#     if request.method == "GET":
#         context['name'] = request.GET.get('name')
#         city = request.GET.get('city')
#     return render(request, 'taskone/index.html', context)

# def hello(request):
#     client_ip = request.META.get('REMOTE_ADDR', '127.0.0.1')

#     api_key = "85971a067dd524d514061870d1d1502c"
#     url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"

#     response = requests.get(url)
#     result = response.json()
#     print(json.dumps(result, indent=4))
#     if result.get('cod') != "404":
#         context['temperature'] = result['list'][0]['main']['temp']
#         context['description'] = result['list'][0]['weather'][0]['description']
#         context['location'] = result['city']
#     else:
#         context['temperature'] = 'unknown'
#         context['description'] = 'unknown'
#         context['location'] = 'unknown'

#     context['greeting'] = f"Hello, {context['name']}!, the temperature is {context['temperature']} degrees Celsius in {context['location']}."

#     return render(request, 'taskone/hello.html', context)


























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

@api_view(['GET'])
def hello(request):
    context = {}
    if request.method == "GET":
        if 'submitform' in request.GET:
            name = request.GET.get('name')
            city = request.GET.get('city')
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