from django.shortcuts import render
from .models import Event

def index(request):
    event_list = Event.objects.all().order_by('event_date')
    return render(request, 'index.html', 
                  {
                      'event_list': event_list
                  })

def sign_up(request):
    return render(request, 'sign_up.html', {})
