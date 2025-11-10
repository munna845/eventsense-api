from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import User_ViewSet, Event_ViewSet, Interest_ViewSet,Notification_viewset

router = DefaultRouter()
router.register(r'user', User_ViewSet, basename='user')
router.register(r'events', Event_ViewSet, basename='events')
router.register(r'interests', Interest_ViewSet, basename='interesrs')
router.register('notifications', Notification_viewset, basename='notification') 



urlpatterns = [
    path('', include(router.urls)),
]
