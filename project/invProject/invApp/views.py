from django.shortcuts import render,redirect
from .forms import ProductForm
from .models import Product
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 

from django.contrib.auth.models import User
from .forms import RegisterForm

#Crud = crate, read, update,delete

#Homw View
def home_view(request):
    return render(request,'invApp/home.html')


#Create View
def product_create_view(request):
    form=ProductForm()
    if request.method=="POST":
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request,'invApp/product_form.html',{'form':form})

#Read View
def product_list_view(request):
    products=Product.objects.all()
    return render(request,'invApp/product_list.html',{'products':products})

#Update View 
def product_update_view(request,product_id):
    product=Product.objects.get(product_id=product_id)
    form=ProductForm()
    if request.method=="POST":
        form=ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request,'invApp/product_form.html',{'form':form})
    

#delete view
def product_delete_view(request,product_id):
    product=Product.objects.get(product_id=product_id)
    if request.method =="POST":
        product.delete()
        return redirect('product_list')
    return render(request,'invAPP/product_delete.html',{'products':product})





def register_view(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=User.objects.create_user(username=username,password=password)
            login(request,user)
            return redirect('login')
    else:
        form=RegisterForm()
    return render (request,'accounts/register.html',{'form':form})
            
   

def login_view(request):
    error_message = None 
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            next_url=request.POST.get('next') or request.GET.get('next') or 'home'

            return redirect(next_url)
        else:
            error_message=("Invalid Credentials")

    return render(request,'accounts/login.html',{'error':error_message})




def logout_view(request):
    if request.method=="POST":
        logout(request)
        return redirect('login')
    return render(request, 'accounts/logout.html')
    

#Home View 
#Using the decorder
@login_required
def home_view(request):
    return render(request,'invApp/home.html')
