from functools import update_wrapper
from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=255)
    auteur=models.CharField(max_length=255)
    ISBN=models.CharField(max_length=50)
    price =models.FloatField()
    date_record=models.TimeField(auto_now_add=True)
    date_update=models.TimeField(auto_now=True)

    def __str__(self):
        return self.title

   # image=models.ImageField(upload_to="image")

books =[
    {
        "title":"les aventures romantiques",
        "ISBN" :"24-1 CD",
        "auteur" :"",
        "edition" :"bordo"
    },
    {
        "title" :"les grand robbert",
        "ISBN" :"22-1 CD",
        "auteur" :"Miria",
        "edition" :"baoba"
    },
    {
        "title" :"les genies",
        "ISBN" :"20-1 CD",
        "auteur":"Mamamia",
        "edition":"bench"
    }
]
