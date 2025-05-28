from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view( request, *args , **kwags):
    
    print(f"the request is : {request}")
    print(f"args is : {args} , kwags is : {kwags}")
    print(f"the user is : {request.user}")

    return render(request , "home.html" ,{}) # django rendering the html doc


