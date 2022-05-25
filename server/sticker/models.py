from django.db import models


# Create your models here.
class imagePost(models.Model): 
    image = models.ImageField(upload_to="images") #image 필드

    def __str__(self):
        return "imagePost"
