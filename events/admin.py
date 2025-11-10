from django.contrib import admin
from .models import User, Event, Interest

from django.contrib import admin
from .models import User, Event, Interest,Notification

admin.site.register(User)
admin.site.register(Event)
admin.site.register(Interest)
admin.site.register(Notification)

