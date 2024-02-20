from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Client(models.Model):
    user= models.OneToOneField(User, null=True, blank=True,on_delete=models.CASCADE)
    name= models.CharField(max_length=100, null=True)
    email=models.EmailField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.name
    
class Category(models.Model):
    name=models.CharField(max_length=100)
    description = models.TextField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.name
    

class Profuit(models.Model):
    