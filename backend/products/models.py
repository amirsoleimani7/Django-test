from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):

    title = models.CharField(max_length=120)  
    description = models.TextField(blank=True, null=False , default='default description')
    price = models.DecimalField(decimal_places=2 , max_digits=10 )
    summary = models.TextField(blank=False , null=False)
    featured = models.BooleanField(default=True)
    

    # instance method
    def get_absolute_url(self):
        return reverse("prodcuts:product" , kwargs={"id" : self.id})