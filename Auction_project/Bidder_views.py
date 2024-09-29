from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from Auction_app.models import CustomUser,Bidder

@login_required(login_url='/login')
def HOME(request):
    return render(request,'Bidder/bidder_home.html')

def REGISTRATION(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email_id')
        username = request.POST.get('username')
        password = request.POST.get('password')
        mobile_no = request.POST.get('mobile_no')
        date_of_birth = request.POST.get('date_of_birth')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        # print(profile_pic,first_name,last_name,email,username,password,mobile_no,date_of_birth,address,gender)
        if password=="" or first_name=="" or last_name=="" or profile_pic=="" or mobile_no=="" or gender=="" or date_of_birth=="" or address=="":
            messages.success(request,'Please fill the form properly...')
            return redirect('b_registration')


        if CustomUser.objects.filter(email=email).exists():
            messages.error(request,'Email Already Exists...')
            return redirect('b_registration')

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request,'Username Already Exists...')
            return redirect('b_registration')



        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                profile_pic = profile_pic,
                email = email,
                username = username,
                user_type = 3
            )
            user.set_password(password)
            user.save()

            bidder = Bidder(
                admin = user,
                address = address,
                gender = gender,
                mobile_no = mobile_no,
                date_of_birth = date_of_birth
            )
            bidder.save()

            messages.success(request,'success')
            return redirect('bidder_home')


    return render(request,'Bidder/b_registration.html')


def BIDDER_PRODUCTS(request):
    return render(request,'Bidder/bidder_products.html')

def BIDDER_BLOG(request):
    return render(request,'Bidder/bidder_blog.html')

def BIDDER_CONTACT_US(request):
    return render(request,'Bidder/bidder_contact_us.html')

def BIDDER_CART(request):
    return render(request,'Bidder/bidder_cart.html')

def BIDDER_PROFILE(request):
    return render(request,'Bidder/bidder_profile.html')

def BIDDER_SELF_BLOG(request):
    return render(request,'Bidder/bidder_self_blog.html')
