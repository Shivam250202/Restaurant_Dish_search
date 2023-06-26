from django.db import models


class Restaurant_Details(models.Model):
    
    resturant_id = models.IntegerField()
    name = models.CharField(max_length = 50,primary_key = True)
    location = models.CharField(max_length = 50)
    dish = models.CharField(max_length = 100)
   

    def __str__(self):
        return self.name

