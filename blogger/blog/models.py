from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_pic = models.ImageField(upload_to='images', default='image/profile.png')

    def __str__(self):
        return f"{self.user.username}'s Profile"
    


@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        pro = Profile(user=instance)
        pro.save()
