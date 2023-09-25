from django.contrib import admin
from .models import (
    Venue, Users, Event
)

admin.site.register(Venue)
admin.site.register(Users)
admin.site.register(Event)

