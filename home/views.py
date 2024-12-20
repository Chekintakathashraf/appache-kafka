from django.shortcuts import render
from home.models import *
from django.http import JsonResponse
import os

def index(request):
    api_key = os.getenv('MY_API_KEY')
    return render(request, 'my_template.html', {'api_key': api_key})

def get_data(request):
    latest_data = LocationUpdate.objects.order_by('-timestamp').first()
    if latest_data:
        return JsonResponse({
            "latitude": latest_data.latitude,
            "longitude": latest_data.longitude,
            "timestamp": latest_data.timestamp
        })
    else:
        return JsonResponse({
            "message": "No location data available"
        }, status=200)