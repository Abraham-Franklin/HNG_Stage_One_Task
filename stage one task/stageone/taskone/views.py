
from django.http import JsonResponse

def hello(request):
    visitor_name = request.GET.get('visitor_name', 'Guest')
    city = "New York"  # Default city if not provided in query parameters
    client_ip = request.META.get('REMOTE_ADDR', '127.0.0.1')

    temperature = 11
    location = city
    greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {location}"

    context = {
        "client_ip": client_ip,
        "location": location,
        "greeting": greeting
    }

    return JsonResponse(context)
