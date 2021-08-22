from django.contrib import admin
#from .models import books_view
from .models import  Book



# Register your models here.
#class Book(models.Model):

#list_display=("titl","slug")
#list_filter=("title")
    #prepopulated_fields={"slug":"title"}



admin.site.register(Book)