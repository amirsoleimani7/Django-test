
from django.http import Http404
from django.shortcuts import render , get_object_or_404 , redirect
from .models import Product
from .forms import ProdcutForm ,RawProductForm

def dynamic_lookup_view(request, id):

    obj = get_object_or_404(Product , id = id)

    context = {
        "object" : obj
    }

    return render(request , "products/product_detail.html" , context)




def product_delete_view(request, id):

    obj = get_object_or_404(Product , id = id)

    print("Request method:", request.method)  # Add this line
    
    if request.method == "POST":
        obj.delete()
        return redirect('../../../')


    context = {
        "object" : obj
    }

    return render(request , "products/product_delete.html" , context)

















def render_initial_data(request):
    initial_data = {
        "title": "my thing" 
    }

    form  = ProdcutForm(request.POST or None , initial=initial_data)    
    context = {"form" : form}
    return render(request ,"products/product_create.html", context) 



# Create your views here.
# def product_create_view(request):

#     form  = RawProductForm()    



#     if request.method == 'POST': 
#         form  = RawProductForm(request.POST)
#         if form.is_valid():
    
#             print(f"this is test : {form.cleaned_data}")
#             # print(f"this is test1 : {**form.cleaned_data}")
#             print(f"cleaned data is: {form.cleaned_data}")
#             # ** something (passes 'seomthing' as arguemnts ..) 
#             Product.objects.create(**form.cleaned_data)
#         else:
#             form.errors
#     context = {"form" : form}
#     return render(request ,"products/product_create.html", context) 


def product_create_view(request):

    obj = Product.objects.get(id=1)

    form  = ProdcutForm(request.POST or None , instance=obj)    
    if form.is_valid():
        form.save()
        form = ProdcutForm()
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