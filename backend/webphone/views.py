from django.shortcuts import render
from django.conf import settings
def index(request):
    return render(request, 'webphone/index.html' ,{
        "SERVER_HOST": settings.SERVER_HOST
    })
