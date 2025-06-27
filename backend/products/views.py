from django.shortcuts import render
from .models import Product


# Create your views here.
def product_detail_view(request):   
    
    obj = Product.objects.get(id=1)

    # context = {
    #     'title' : obj.title , 
    #     'summary' : obj.summary
    # }

    context = {
        'object' : obj
    }

    
    print(f"title is : {obj.title} ,  summary is : {obj.summary}")

    return render(request ,"product/detail.html", context)