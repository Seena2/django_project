from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Profile models which extends/inherit builtin model class.
class Profile(models.Model):
    # create one-to-one relationship with "User" model
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profileImage=models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        # run the save method of the parent class
        super().save(*args, **kwargs)
        img=Image.open(self.profileImage.path)
        if img.height> 300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.profileImage.path)
