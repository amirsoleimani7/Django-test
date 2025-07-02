from django import forms 
from .models import Product


class ProdcutForm(forms.ModelForm):

    email = forms.EmailField()

    class Meta:
        model = Product
        fields = [
            'title' , 
            'description',
            'price'
        ]

    def clean_title(self , *args , **kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("this is not a valid title bruh") 
        if not "NEWS" in title:
            raise forms.ValidationError("this is not a valid title bruh1") 
        return title

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("this is not a valid email bruh1") 
        return email


class RawProductForm(forms.Form):
    title = forms.CharField(label='title' , widget=forms.TextInput(attrs={
                                                            "placeholder" : "your title"
    })      )

    description = forms.CharField(required=False ,
                                 widget=forms.Textarea(
                                     attrs= {
                                         "placeholder" : "your description" , 
                                         "class" : "new_class_name" , 
                                         "id" : "my-id-for-text-area" , 
                                         "rows" : 20 , 
                                         "cols" : 50  ,
                                     }
                                 ),
                                )

    price = forms.DecimalField(initial=199.99)
