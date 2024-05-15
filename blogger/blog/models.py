from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField


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

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cat_user') 
    name = models.CharField(max_length=200)
    cat_image = models.ImageField(upload_to='cat/img', blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    thumbnail_image = models.ImageField(upload_to='blog/img')
    pub_date = models.DateTimeField(auto_now_add=True)
    body = RichTextField()
    def __str__(self):
        return f"{self.title} -- {self.user.username.capitalize()} -- {self.pub_date.year} : {self.pub_date.month} : {self.pub_date.day}"