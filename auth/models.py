from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.dispatch import receiver
from django.db.models.signals import post_save

# This is the user profile model here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profilepicture/', blank=True, default='default.png')
    status = models.CharField(max_length=140)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender = User)
    def create_profile(instance,sender,created, **kwargs):
        if created:
            Profile.objects.create(user = instance)

    @receiver(post_save, sender= User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

class Project(models.Model):
    project_name = models.CharField(max_length = 100, blank=True)
    published_date = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @classmethod
    def save_project(self):
        self.save()

    @classmethod
    def delete_project(self):
        self.delete()

    @classmethod
    def search_project(cls, search_term):
        projects = cls.objects.filter(user__username__icontains=search_term)
        return projects

class Product(models.Model):
    product_name = models.CharField(max_length = 100, blank=True)
    product_size = models.CharField(max_length = 100, blank=True)
    product_cost = models.NumField(max_length = 100, blank=True)
    published_date = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @classmethod
    def save_product(self):
        self.save()

    @classmethod
    def delete_product(self):
        self.delete()

    @classmethod
    def search_product(cls, search_term):
        products = cls.objects.filter(user__username__icontains=search_term)
        return products
