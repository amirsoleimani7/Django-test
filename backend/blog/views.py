from django.shortcuts import render


# Create your views here.
from django.http import Http404
from django.shortcuts import render , get_object_or_404 , redirect
from .models import Article
from django.views.generic import (
    CreateView , 
    DetailView , 
    ListView , 
    UpdateView , 
    DetailView
)



# making a list view 
class ArticleListView(ListView):
    queryset = Article.objects.all()  # <blog>/<mdoelname>_list.html

