from django.shortcuts import render
from .models import Product
from .forms import ProdcutForm ,RawProductForm

# Create your views here.
def product_create_view(request):

    form  = RawProductForm()    



    if request.method == 'POST': 
        form  = RawProductForm(request.POST)
        if form.is_valid():
    
            print(f"this is test : {form.cleaned_data}")
            # print(f"this is test1 : {**form.cleaned_data}")
            print(f"cleaned data is: {form.cleaned_data}")
            # ** something (passes 'seomthing' as arguemnts ..)
            Product.objects.create(**form.cleaned_data)
        else:
            form.errors
    context = {"form" : form}
    return render(request ,"products/product_create.html", context) 


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

    return render(request ,"products/product_detail.html", context) 