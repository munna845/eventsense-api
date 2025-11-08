from rest_framework import viewsets, permissions,filters
from django.contrib.auth import get_user_model
from .models import Event, Interest
from .serializers import User_serializer, Event_Serializer,Interest_serializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

User = get_user_model()


class User_ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Interest.objects.all().order_by('id')
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = User_serializer


# Interest View
class Interest_ViewSet(viewsets.ModelViewSet):
    queryset = Interest.objects.all().order_by('id') 
    serializer_class = Interest_serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    search_fields = ['name']
    ordering_fields = ['name']
    order = ['name']


# Event View
class Event_ViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = Event_Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ['interests','interests','created_by']
    searche_fields = ['title','description','location']
    ordering_fields = ['title','date','created_at']
    ordering = ['created_at']


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
    
    

    






