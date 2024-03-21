from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class Profiles(models.Model):
    id = models.UUIDField(max_length=36,primary_key=True, default=uuid.uuid4, editable=False)
 
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to='profiles/', default="profiles/user-default.png")
    created = models.DateTimeField(auto_now_add=True,null=True)
    
    
    def __str__(self):
        return self.name
    

class Certificates(models.Model):
    description = models.TextField(max_length=50,null=True,blank=True)
    image = models.ImageField(upload_to='profiles/')
    source_link = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.description

  
    
    
class ProfilesName(models.Model):
    pass
