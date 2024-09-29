from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import get_object_or_404
from Auction_app.models import CustomUser,Seller,Product,Categories,Brand,Color,Filter_Price,Images,Tag,Admin_Notification,Seller_Notification



@login_required(login_url='/login')
def HOME(request):
    return render(request,'Seller/seller_home.html')

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
            return redirect('s_registration')


        if CustomUser.objects.filter(email=email).exists():
            messages.error(request,'Email Already Exists...')
            return redirect('s_registration')

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request,'Username Already Exists...')
            return redirect('s_registration')



        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                profile_pic = profile_pic,
                email = email,
                username = username,
                user_type = 2
            )
            user.set_password(password)
            user.save()

            seller = Seller(
                admin = user,
                address = address,
                gender = gender,
                mobile_no = mobile_no,
                date_of_birth = date_of_birth
            )
            seller.save()

            messages.success(request,'success')
            return redirect('seller_home')


    return render(request,'Seller/s_registration.html')

def SELLER_ADD(request):
    if request.method == "POST":
        # Fetching form data
        seller_id = request.POST.get('seller_id')
        name = request.POST.get('name')
        price = request.POST.get('price')
        condition = request.POST.get('condition')
        information = request.POST.get('information')
        description = request.POST.get('description')
        stock = request.POST.get('stock')
        image = request.FILES.get('image')
        categories_id = request.POST.get('categories')
        brand_id = request.POST.get('brand')
        color_id = request.POST.get('color')
        filter_price_id = request.POST.get('filter_price')
        tags = request.POST.get('tags')  # Assume comma-separated tags
        images = request.FILES.getlist('images')
        end_date = request.POST.get('end_date')

        # Fetching related objects
        seller = get_object_or_404(Seller, admin=request.user) # Replace with the actual seller logic
        categories = Categories.objects.get(id=categories_id)
        brand = Brand.objects.get(id=brand_id)
        color = Color.objects.get(id=color_id)
        filter_price = Filter_Price.objects.get(id=filter_price_id)

        # Creating a Product object
        product = Product.objects.create(
            seller_id=seller,
            name=name,
            price=price,
            condition=condition,
            information=information,
            description=description,
            stock=stock,
            image=image,
            created_date=timezone.now(),
            end_date=end_date,
            categories=categories,
            brand=brand,
            color=color,
            filter_price=filter_price
        )
        product.save()
        messages.success(request,'Your Product Will Be Go For Approval')

        # Handling tags
        if tags:
            tag_list = tags.split(',')
            for tag_name in tag_list:
                Tag.objects.create(name=tag_name.strip(), product=product)
        if images:
            for image in images:
                Images.objects.create(image=image, product=product)

        return redirect('seller_add')

        # Fetching necessary data for the form
    categories = Categories.objects.all()
    brands = Brand.objects.all()
    colors = Color.objects.all()
    filter_prices = Filter_Price.objects.all()

    return render(request, 'Seller/seller_add.html', {
        'categories': categories,
        'brands': brands,
        'colors': colors,
        'filter_prices': filter_prices,
    })

def SELLER_CHECK_BID(request):
    return render(request,'Seller/seller_check_bid.html')

def SELLER_SERVICES(request):
    return render(request,'Seller/seller_services.html')

def SELLER_ABOUT_US(request):
    return render(request,'Seller/seller_about_us.html')

def SELLER_CONTACT_US(request):
    admin_users = CustomUser.objects.filter(is_superuser=True)
    see_message = Admin_Notification.objects.all().order_by('-id')[0:5]

    context = {
        'admin_users': admin_users,
        'see_message': see_message,
    }
    return render(request,'Seller/seller_contact_us.html',context)

def SELLER_SAVE_CONTACT_US(request):
    if request.method == 'POST':
        admin_id = request.POST.get('admin')  # Get the admin ID from the POST data
        message = request.POST.get('message')  # Get the message from the POST data

        # Fetch the CustomUser instance using the admin ID
        try:
            admin_user = CustomUser.objects.get(id=admin_id, user_type=1)  # Ensure the user_type is Admin
        except CustomUser.DoesNotExist:
            messages.error(request, 'Admin user not found.')
            return redirect('seller_contact_us')

        # Create and save the Admin_Notification
        notification = Admin_Notification(
            admin=admin_user,
            message=message,
        )
        notification.save()

        messages.success(request, 'Message are successfully send........')
        return redirect('seller_contact_us')

def SELLER_NOTIFICATION(request):
    seller = request.user.seller
    seller_notification = Seller_Notification.objects.filter(seller_id=seller)

    return render(request, 'Seller/seller_notification.html', {
        'seller_notification': seller_notification,
    })
def SELLER_MARK_AS_DONE(request,status):
    notification = Seller_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('seller_notification')
def SELLER_PROFILE(request):
    return render(request,'Seller/seller_profile.html')

def SELLER_PRODUCTS(request):
    seller = request.user.seller  # logic for fetching the seller
    products = Product.objects.filter(seller_id=seller)

    return render(request, 'Seller/seller_products.html', {
        'products': products,
    })

def SELLER_EDIT_PRODUCTS(request,id):
    product = get_object_or_404(Product, id=id)


    # Fetching necessary data for the form
    categories = Categories.objects.all()
    brands = Brand.objects.all()
    colors = Color.objects.all()
    filter_prices = Filter_Price.objects.all()

    return render(request, 'Seller/seller_edit_products.html', {
        'product': product,
        'categories': categories,
        'brands': brands,
        'colors': colors,
        'filter_prices': filter_prices,
    })

def SELLER_UPDATE_PRODUCTS(request):
    if request.method == 'POST':
        # Fetching form data
        product_id = request.POST.get('product_id')
        name = request.POST.get('name')
        price = request.POST.get('price')
        condition = request.POST.get('condition')
        information = request.POST.get('information')
        description = request.POST.get('description')
        stock = request.POST.get('stock')
        image = request.FILES.get('image')
        categories_id = request.POST.get('categories')
        brand_id = request.POST.get('brand')
        color_id = request.POST.get('color')
        filter_price_id = request.POST.get('filter_price')
        tags = request.POST.get('tags')  # Assume comma-separated tags
        images = request.FILES.getlist('images')
        end_date = request.POST.get('end_date')

        # Fetch the existing product
        product = Product.objects.get(id=product_id)

        # Update product fields
        product.name = name
        product.price = price
        product.condition = condition
        product.information = information
        product.description = description
        product.stock = stock
        product.end_date = end_date

        # Update image if a new one is uploaded
        if image:
            product.image = image

        # Save the product after all updates
        product.save()

        # Handling tags
        if tags:
            # Clear existing tags
            product.tag_set.all().delete()
            tag_list = tags.split(',')
            for tag_name in tag_list:
                tag_name = tag_name.strip()
                # Create new tags
                Tag.objects.create(name=tag_name, product=product)

        # Handling images
        if images:
            for image in images:
                # Add new images
                Images.objects.create(image=image, product=product)

        # Update related fields (foreign keys)
        product.categories = Categories.objects.get(id=categories_id)
        product.brand = Brand.objects.get(id=brand_id)
        product.color = Color.objects.get(id=color_id)
        product.filter_price = Filter_Price.objects.get(id=filter_price_id)

        # Save the product with updated relationships
        product.save()

        messages.success(request, 'Record Successfully Updated...')
        return redirect('seller_products')

    return render(request, 'Seller/seller_edit_products.html')


def SELLER_DELETE_PRODUCTS(request,id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    messages.success(request,'Record Are Successfully Deleted...')
    return redirect('seller_products')

