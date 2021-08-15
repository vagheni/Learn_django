from typing import Generic
from django import template
from django.shortcuts import render
from django.http import HttpResponse
from .models import books
from django.template import Template
#from .models import color
from django.views import generic
from django.shortcuts import render

# Create your views here.
def books_view(request):
    Context={"books":books}

    return render(request,"library/home.html",Context)



    #return render(request,"library/home.html", {"books":books})


#class IndexView(generic.ListView):
    Template_name ="polls/Index.html"
    context_object_name="Latest_question_name"

    def get_queryset(self):
        return Question.objet.order_by("")
        
     
