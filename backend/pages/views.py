from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view( request, *args , **kwags):
    
    print(f"the request is : {request}")
    print(f"args is : {args} , kwags is : {kwags}")
    print(f"the user is : {request.user}")
   
    

    test_template = {
        'inner_dict1': 'this is the inner one' , 
        'inner_dict2': 'this is the inner two' , 
        'inner_dict3': 'this is the inner three' , 
        'inner_dict4': 'this is the inner four' ,
    }
    
    my_context = {
        'my_text' : "this is about me" ,
        'my_number' : 123 , 
        'my_list' : [12,123,123123] ,
        'inner'  : test_template
    }
    

    return render(request , "home.html" ,  my_context) # django rendering the html doc


