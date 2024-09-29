from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from Auction_app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Auction_app.models import CustomUser,Seller,Bidder,Product

def BASE(request):
    return render(request,'base.html')


def LOGIN(request):
    return render(request, 'login.html')



def DoLOGIN(request):
    if request.method == 'POST':
        user = EmailBackEnd.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password'),)
        if user != None:
            login(request,user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('Admin_home')
            elif user_type == '2':
                return redirect('seller_home')
            elif user_type == '3':
                return redirect('bidder_home')
            else:
                messages.error(request,"Email and Password are invalid !")
                return redirect('login')
        else:
            messages.error(request, "Email and Password are invalid !")
            return redirect('login')

# Logout function
def DoLOGOUT(request):
    logout(request)
    return redirect('/')


# def PROFILE(request):
#
#     return render(request,'profile.html')


def HOME(request):
    return render(request,'home.html')

def SERVICES(request):
    return render(request,'services.html')

def PRODUCTS(request):
    products = Product.objects.filter(status=1)
    return render(request, 'products.html', {'products': products})

def ABOUTUS(request):
    return render(request,'about_us.html')

def CONTACTUS(request):
    return render(request,'contact_us.html')


def PRODUCT_DETAILS(request,id):
    product = get_object_or_404(Product, id=id)
    context = {
        'product': product
    }
    return render(request, 'product_details.html', context)