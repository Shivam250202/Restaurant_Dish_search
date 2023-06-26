from django.shortcuts import render
from .models import Restaurant_Details
from django.http import HttpResponse 
from app.serializers import *
import csv 
filename = "C:\\Users\\Lenovo\\OneDrive\\Desktop\\New folder\\venv\\Scripts\\Restaurant_Dish\\restaurants_small.csv"

from rest_framework import viewsets



def add_record(request):
    with open(filename,'r') as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            ro = Restaurant_Details(resturant_id = row[0],name = row[1],location=row[2],dish = row[3])
            ro.save()
    return HttpResponse("Data inserted successfuly")
        




class Detail(viewsets.ModelViewSet):
    queryset = Restaurant_Details.objects.all()
     
    
    serializer_class = Restaurant_Serializer





    

        
    
    
    
        
        
        
   

    
    
    

