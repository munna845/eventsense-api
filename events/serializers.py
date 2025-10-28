from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Event, Interest

User = get_user_model()
#user serializer
class user_serializer(serializers.ModelSerializer):
  Interest= serializers.StringRelatedField(many=True,read_only=True)
  
  class Meta:
    model=User
    fields = ['id', 'username', 'email', 'phone', 'interests']

#interest serializer
class Interest_serializer(serializers.ModelSerializer):
  class Meta:
    model=Interest
    fields = ['id', 'name']
    
#Event serializer
class Event_Serializer(serializers.ModelSerializer):
  Interest= serializers.StringRelatedField(many=True,read_only=True)
  created_by = user_serializer(read_only=True)

  class Meta:
    model=Event
    fields=fields = ['id', 'title', 'description', 'location', 'date', 'interests', 'created_by', 'created_at']
    