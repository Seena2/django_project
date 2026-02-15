from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# Signal function to create profile for a user
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    #If user is created, create profile for that user
    if created: 
        Profile.objects.create(user=instance)

# Signal function to save the created profile
@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    #save the user
    instance.profile.save()


 