from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=100)
    profile=models.ImageField(upload_to='images/', blank=True)
    email = models.CharField(blank = True, max_length = 100)
    bio = models.TextField(max_length=100)

    def __str__(self):
        return self.username

    def save_user(self):
        self.save()
        
    @classmethod
    def get_user(cls,id):
        profile = Profile.objects.all()
        return profile

    @classmethod
    def update_user(cls,id,new_username):
        cls.objects.filter(id=id).update(username = new_username)

    @classmethod
    def delete_user(cls,id):
        cls.objects.filter(id).delete()


    @classmethod
    def search_by_username(cls, searched_username):
        username = cls.objects.filter(username__icontains=searched_username)

        return username