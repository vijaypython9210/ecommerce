import json
from django.shortcuts import render,redirect,HttpResponse
from . models import *
from django.contrib import messages
from shop.forms import CustumUserForm
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse

# Create your views here.
def home(request):
    trending=Product.objects.filter(quantity__lte=100 , quantity__gt=0)
    return render(request,'shop/index.html',{'trending':trending})

def register(request):
    form=CustumUserForm()
    if request.method=='POST':
        form=CustumUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Register Success You can Login now..!')
            return redirect('loginPage')
    return render(request,'shop/register.html',{'form':form})

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,'Logged in Successfully')
                return redirect('/')
            else:
                messages.error(request,'Invalid Username and Password !')
                return redirect('loginPage')
        return render(request,'shop/login.html')

def logoutPage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'Logged out Successfully')
    return redirect('/')


def collections(request):
    category=Category.objects.filter(status=0)
    return render(request,'shop/collections.html',{'category':category})

def collectionView(request,name):
    if(Category.objects.filter(status=0,name=name)):
        products_details=Product.objects.filter(category__name=name)
        return render(request,'shop/products/index.html',{'products':products_details,'categoryName':name})
    else:
        messages.warning(request,'Category not found')
        return redirect('collections')
    
def product_details(request,cname,pname):
    if(Category.objects.filter(status=0,name=cname)):
        if(Product.objects.filter(product_name=pname,status=0)):
            product=Product.objects.filter(product_name=pname,status=0).first()
            print('Successfully')
            return render(request,'shop/products/product_details.html',{'product':product})
        else:
            messages.error(request,'No Such a product')
            print('product fault')
            return redirect('collections')
    else:
        messages.error(request,'No Such a Category')
        print('category fault')
        return redirect('collections')
    
def add_to_cart(request):
    if request.headers.get('X-Requested-With')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            pid=data['product_id']
            qnty=data['product_qnty']
            product_status=Product.objects.get(id=pid)
            if Cart.objects.filter(user=request.user,product_id=pid):
                return JsonResponse({'status':'Product already in the Cart'},status=200)
            else:
                if product_status.quantity>=qnty:
                    Cart.objects.create(user=request.user,product_qnty=qnty,product_id=pid)
                    return JsonResponse({'status':'Product Added to Cart'},status=200)
                else:
                    return JsonResponse({'status':'Product Not Available in Cart'},status=200)
            return JsonResponse({'status':'Product added to Cart Success'},status=200)
        else:
             return JsonResponse({'status':'Login To Addcart'},status=200)
    else:
        return JsonResponse({'status':'Invalid access'},status=200)

def view_cart(request):
    if request.user.is_authenticated:
        cart_product=Cart.objects.filter(user=request.user)
        return render(request,'shop/products/cart.html',{'cart':cart_product})
    else:
        return redirect('/')

def remove_cart(request,cid):
    cart=Cart.objects.filter(id=cid)
    cart.delete()
    return redirect('/viewcart')

def fav(request):
    if request.headers.get('X-Requested-With')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            pid=data['product_id']
            product_status=Product.objects.get(id=pid)
            if Favourite.objects.filter(user=request.user,product_id=pid):
                return JsonResponse({'status':'Product already in Favourate'},status=200)
            else:
                Favourite.objects.create(user=request.user,product_id=pid)
                return JsonResponse({'status':'Product Added to Favourate'},status=200)
        else:
             return JsonResponse({'status':'Login To Addcart'},status=200)
    else:
        return JsonResponse({'status':'Invalid access'},status=200)
    
def view_fav(request):
    if request.user.is_authenticated:
        fav_product=Favourite.objects.filter(user=request.user)
        return render(request,'shop/products/fav.html',{'fav':fav_product})
    else:
        return redirect('/')

def remove_fav(request,fid):
    fav=Favourite.objects.filter(id=fid)
    fav.delete()
    return redirect('/viewfav')

