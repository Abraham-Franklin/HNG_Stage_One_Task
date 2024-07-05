# from django.shortcuts import render
# from django.http import JsonResponse
# import requests
# from rest_framework.decorators import api_view

# def getData(request):
#     return render(request, 'taskone/index.html')

# @api_view(['GET'])
# def hello(request):
#     visitor_name = request.GET.get('visitor_name')
#     city = request.GET.get('city')
#     client_ip = request.META.get('REMOTE_ADDR', '127.0.0.1')

#     api_key = "85971a067dd524d514061870d1d1502c"
#     url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

#     response = requests.get(url)
#     result = response.json()

#     context = {}
#     if result.get('cod') != "404":
#         temperature = result['main']['temp']
#         description = result['weather'][0]['description']
#         location = result['name']  # Use result['name'] for city name

#         context['temperature'] = temperature
#         context['description'] = description
#         context['location'] = location
#     else:
#         context['temperature'] = 'unknown'
#         context['description'] = 'unknown'
#         context['location'] = 'unknown'

#     context['greeting'] = f"Hello, {visitor_name}!, the temperature is {context['temperature']} degrees Celsius in {context['location']}."

#     return JsonResponse(context)
















from django.http import JsonResponse
import requests

def hello(request):
    client_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if client_ip:
        client_ip = client_ip.split(',')[0]
    else:
        client_ip = request.META.get('REMOTE_ADDR', '127.0.0.1')

    ipapi_url = f"https://ipapi.co/{client_ip}/json/"
    ipapi_response = requests.get(ipapi_url)
    ipapi_data = ipapi_response.json()

    if 'city' in ipapi_data and 'country' in ipapi_data:
        location = f"{ipapi_data['city']}, {ipapi_data['country']}"
    else:
        location = "Unknown location"

    visitor_name = request.GET.get('visitor_name', 'Visitor')
    temperature = 11  # Static temperature for demonstration
    greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {location}"

    context = {
        "client_ip": client_ip,
        "location": location,
        "greeting": greeting
    }

    return JsonResponse(context)
