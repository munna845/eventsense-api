from rest_framework import serializers
from django.contrib.auth import get_user_model,authenticate
from .models import Event, Interest,Interest,Notification

User = get_user_model()
#user serializer
class User_serializer(serializers.ModelSerializer):
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
  created_by = User_serializer(read_only=True)

  class Meta:
    model=Event
    fields= ['id', 'title', 'description', 'location', 'date', 'interests', 'created_by', 'created_at']
    
#register serializer
class Register_Serializer(serializers.ModelSerializer):
  password =serializers.CharField(write_only=True, min_length =6)
  interests = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Interest.objects.all(), required=False
    )

  class Meta:
    model =User
    fields = ['id','username','email','phone','password','interests']
  

  def create(self,validated_data):
    interests = validated_data.pop(interests,[])
    user =User.objects.create_user(
      username=validated_data['username'],
      email=validated_data['email',''],
      password=validated_data['password'],
      phone=validated_data['phone','']
    )
    user.interests.set(interests)
    return user
        
#Login serializer
class Login_Serializer(serializers.ModelSerializer):
  username = serializers.CharField(max_length=20)
  password =serializers.CharField(write_only=True)


  def validate(self, data):
    user =authenticate(**data)
    if not user:
      raise serializers.ValidationError('Please insert correct username or password')
    if not user.is_active:
      raise serializers.ValidationError('this user is not active')
    return user
  
#Notification serializer
class Notification_serializer(serializers.ModelSerializer):
  class Meta:
    model = Notification
    fields =['user','messege','is_read','created_at']