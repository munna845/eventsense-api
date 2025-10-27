from django.contrib import admin
from .models import User, Event, Interest

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'phone', 'get_interests']

    def get_interests(self, obj):
        return ", ".join([i.name for i in obj.interests.all()])
    get_interests.short_description = 'Interests'


@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'location', 'date', 'get_interests', 'created_by', 'created_at']

    def get_interests(self, obj):
        return ", ".join([i.name for i in obj.interests.all()])
    get_interests.short_description = 'Interests'
