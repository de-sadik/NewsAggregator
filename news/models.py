from django.db import models

# Create your models here.
class News(models.Model):
    heading = models.CharField(max_length=400,  unique=True)
    image_url = models.URLField()
    source_url = models.URLField()

    def __str__(self):
        return self.heading
    
class Category(models.Model):
    heading = models.CharField(max_length=400, unique=True)
    image_url= models.URLField()
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.heading