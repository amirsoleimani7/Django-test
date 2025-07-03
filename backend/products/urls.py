from django.urls import path
from products.views import (
        product_detail_view ,
        product_create_view , 
        dynamic_lookup_view , 
        render_initial_data , 
        product_delete_view ,
        product_list_view ,
)


app_name = 'products'
urlpatterns = [    
    path('' , product_detail_view  , name = 'prodcut') , 
    path('create/' , product_create_view  , name = 'prodcut_create') , 
    path('<int:id>/' , dynamic_lookup_view , name='product') , 
    path('<int:id>/delete/' , product_delete_view , name='product_delete') , 
    path('product_list/' , product_list_view, name='product_list_view')
]

