from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from .models import Event, Interest
from .serializers import user_serializer, Event_Serializer,Interest_serializer
from rest_framework.decorators import action
from rest_framework.response import Response

User = get_user_model()


class User_ViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = user_serializer
#user view
    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

# Interest View
class Interest_ViewSet(viewsets.ModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = Interest_serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Event View
class Event_ViewSet(viewsets.ModelViewSet):
    serializer_class = Event_Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Event.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


    #recomention
    @action(detail=False, methods =['get'], url_path='recommended')
    def recommended(self,request):
      user = request.user

      if not user.is_authenticated:
        events =Event.objects.all().order_by('created_at')[:10]
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)
      if not user.is_authenticated:
        events =Event.objects.all().order_by('created_at')[:10]
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)
      user_interests = user.interests.all()
      events = Event.objects.all().filter(interests__in=user_interests).distinct()


      if events.count() < 5 :
        others = Event.objects.exclude(insterests__in =user_interests)
        events = (events | others).distinct()

      serializer= self.get_serializer(events,many=True)
      return Response(serializer.data)
    
    

    






