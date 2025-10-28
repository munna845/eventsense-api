from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from .models import Event, Interest
from .serializers import user_serializer, Event_Serializer,Interest_serializer

User = get_user_model()


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = user_serializer
#user view
    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

# Interest View
class InterestViewSet(viewsets.ModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = Interest_serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Event View
class EventViewSet(viewsets.ModelViewSet):
    serializer_class = Event_Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Event.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
