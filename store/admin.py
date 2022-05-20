from django.contrib import admin
from store.models import Product
from store.models import categry
from store.models import customber
admin.site.register(customber)

class Adminproduct(admin.ModelAdmin):
    list_display=['name','price','cat']
admin.site.register(Product,Adminproduct)
class Admincategry(admin.ModelAdmin):
    list_display=['name']
admin.site.register(categry,Admincategry)
# Register your models here.
