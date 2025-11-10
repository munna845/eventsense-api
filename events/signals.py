from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User,Event,Notification

@receiver(post_save,sender=Event)
def create_Event_Notification(sende,instance,created,**kwargs):
  if created:
    users=User.objects.filter(interests__in=instance.interests.all()).distinct()

    notifications = [
      Notification(
        user=user,
        messege=f"New Event '{instance.title}' is created, Which matches your interests!"
      )
      for user in users
    ]
    Notification.objects.bulk_create(notifications)
