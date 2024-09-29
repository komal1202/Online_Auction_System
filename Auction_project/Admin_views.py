from django.contrib import messages
from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from Auction_app.models import CustomUser,Seller,Bidder,Product,Seller_Notification,Admin_Notification

@login_required(login_url='/login')
def HOME(request):
    return render(request,'Admin/home.html')


def SELLER(request):
    products = Product.objects.all()

    context = {
        'products':products
    }

    return render(request, 'Admin/seller.html',context)

def BIDDER(request):
    # Filter products with status = 1 (Approved)
    products = Product.objects.filter(status=1)
    return render(request, 'Admin/bidder.html', {'products': products})

def SERVICES(request):
    return render(request,'Admin/services.html')

def ABOUT_US(request):
    return render(request,'Admin/about_us.html')

def SAVE_CONTACT_US(request):
    if request.method == 'POST':
        seller_id = request.POST.get('seller_id')
        message = request.POST.get('message')

        seller = Seller.objects.get(id = seller_id)
        notification = Seller_Notification(
            seller_id = seller,
            message = message,
        )
        notification.save()
        messages.success(request,'Message are successfully send........')
        return redirect('Admin_contact_us')

def CONTACT_US(request):
    sellers = Seller.objects.all()
    see_message = Seller_Notification.objects.all()

    context = {
        'sellers': sellers,
        'see_message': see_message,
    }
    return render(request,'Admin/contact_us.html',context)


def NOTIFICATION(request):
    admin = request.user
    admin_notification = Admin_Notification.objects.filter(admin=admin)

    return render(request, 'Admin/notification.html', {
        'admin_notification': admin_notification,
    })

def MARK_AS_DONE(request,status):
    admin_notification = Admin_Notification.objects.get(id = status)
    admin_notification.status = 1
    admin_notification.save()
    return redirect('Admin_notification')

def ADMIN_PROFILE(request):
    user = CustomUser.objects.get(id = request.user.id)

    context = {
        "user" : user,
    }
    return render(request,'Admin/admin_profile.html',context)


def ADMIN_PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        # email = request.POST.get('email_id')
        # username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id = request.user.id)

            customuser.first_name = first_name
            customuser.last_name = last_name

            if password != None and password != "":
                customuser.set_password(password)
            if profile_pic != None and profile_pic != "":
                customuser.profile_pic = profile_pic
            customuser.save()
            messages.success(request,"your profile updated successfully....")
            return redirect('Admin_profile')
        except:
            messages.error(request,"Failed to update your profile....")
    return render(request,'Admin/admin_profile.html')


def APPROVE_PRODUCT(request,id):
    product = Product.objects.get(id = id)
    product.status = 1
    product.save()
    return redirect('Admin_seller')


def DISAPPROVE_PRODUCT(request,id):
    product = Product.objects.get(id=id)
    product.status = 2
    product.save()
    return redirect('Admin_seller')


def PRODUCT_DETAIL(request,id):
    product = get_object_or_404(Product, id = id)
    context = {
        'product': product
    }
    return render(request, 'Admin/product_detail.html', context)