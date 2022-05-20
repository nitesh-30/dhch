from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models import Product
from store.models import categry
from store.models import customber
from django.views import View

class index(View):
    def post(self,request):
        product=request.POST.get(Product)
        return redirect('homepage')

    def get(self,request):
        products= Product.objects.all()
        categrys=categry.objects.all()
        catgeryid=request.GET.get('categry')
        if catgeryid:
           products=Product.get_all_products_by_categryid(catgeryid)
        else:
            products=Product.get_all_products();
            data={}
            data['products']=products
            data['categrys']=categrys
            return render(request,'index.html',data)


# Create your views here.
def index(request):
    products= Product.objects.all()
    categrys=categry.objects.all()
    catgeryid=request.GET.get('categry')
    if catgeryid:
        products=Product.get_all_products_by_categryid(catgeryid)
    else:
        products=Product.get_all_products();
    data={}
    data['products']=products
    data['categrys']=categrys
    return render(request,'index.html',data)
def signup(request):
    if request.method=="GET":
       return render(request,'signup.html')
    else:
       std =customber()
       std.first_name=request.POST.get('firstname')
       std.last_name=request.POST.get('lastname')
       std.phone=request.POST.get('phone')
       std.email=request.POST.get('email')
       std. password=request.POST.get('password')
       std.save()
       return redirect('homepage')
def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
         return redirect('homepage')