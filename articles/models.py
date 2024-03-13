from django.db import models
import uuid
from userapps.models import Profiles

# Create your models here.

class Articles(models.Model):
    owner = models.ForeignKey(Profiles,null=True,on_delete=models.SET_NULL,blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    featured_image = models.ImageField(null=True,blank=True,default="default.jpeg")
    tags = models.ManyToManyField('Tag',blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.title
    
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
         return self.name
    

              