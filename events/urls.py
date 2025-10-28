from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import User_ViewSet, Event_ViewSet, Interest_ViewSet

router = DefaultRouter()
router.register(r'user', User_ViewSet, basename='user')
router.register(r'events', Event_ViewSet, basename='events')
router.register(r'interests', Interest_ViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
