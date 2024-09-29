
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views, Admin_views,Bidder_views,Seller_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # common path
    path('', views.BASE, name='base'),
    path('home', views.HOME, name='home'),
    path('services', views.SERVICES, name='services'),
    path('products', views.PRODUCTS, name='products'),
    path('product_details/<str:id>', views.PRODUCT_DETAILS, name='product_details'),
    path('about_us', views.ABOUTUS, name='about_us'),
    path('contact_us', views.CONTACTUS, name='contact_us'),

    # Login path
    path('login', views.LOGIN, name='login'),
    path('doLogin', views.DoLOGIN, name='doLogin'),
    path('doLogout', views.DoLOGOUT, name='doLogout'),

    
    # Profile Update
    # path('profile', views.PROFILE, name='profile'),


    # This is Admin Panel
    path('Admin/home', Admin_views.HOME, name='Admin_home'),
    path('Admin/seller', Admin_views.SELLER, name='Admin_seller'),
    path('Admin/product_detail/<str:id>', Admin_views.PRODUCT_DETAIL, name='Admin_product_detail'),
    path('Admin/approve_product/<str:id>', Admin_views.APPROVE_PRODUCT, name='Admin_approve_product'),
    path('Admin/disapprove_product/<str:id>', Admin_views.DISAPPROVE_PRODUCT, name='Admin_disapprove_product'),
    path('Admin/bidder', Admin_views.BIDDER, name='Admin_bidder'),
    path('Admin/services', Admin_views.SERVICES, name='Admin_services'),
    path('Admin/about_us', Admin_views.ABOUT_US, name='Admin_about_us'),
    path('Admin/contact_us', Admin_views.CONTACT_US, name='Admin_contact_us'),
    path('Admin/save_contact_us', Admin_views.SAVE_CONTACT_US, name='Admin_save_contact_us'),
    path('Admin/notification', Admin_views.NOTIFICATION, name='Admin_notification'),
    path('Admin/mark_as_done/<str:status>', Admin_views.MARK_AS_DONE, name='mark_as_done'),
    path('Admin/admin_profile', Admin_views.ADMIN_PROFILE, name='Admin_profile'),
    path('Admin/admin_profile_update', Admin_views.ADMIN_PROFILE_UPDATE, name='Admin_profile_update'),


    # Seller Panel
    path('Seller/home', Seller_views.HOME, name='seller_home'),
    path('Seller/s_registration', Seller_views.REGISTRATION, name='s_registration'),
    path('Seller/seller_add', Seller_views.SELLER_ADD, name='seller_add'),
    path('Seller/seller_check_bid', Seller_views.SELLER_CHECK_BID, name='seller_check_bid'),
    path('Seller/seller_services', Seller_views.SELLER_SERVICES, name='seller_services'),
    path('Seller/seller_about_us', Seller_views.SELLER_ABOUT_US, name='seller_about_us'),
    path('Seller/seller_contact_us', Seller_views.SELLER_CONTACT_US, name='seller_contact_us'),
    path('Seller/seller_save_contact_us', Seller_views.SELLER_SAVE_CONTACT_US, name='seller_save_contact_us'),
    path('Seller/seller_notification', Seller_views.SELLER_NOTIFICATION, name='seller_notification'),
    path('Seller/seller_mark_as_done/<str:status>', Seller_views.SELLER_MARK_AS_DONE, name='seller_mark_as_done'),
    path('Seller/seller_profile', Seller_views.SELLER_PROFILE, name='seller_profile'),
    path('Seller/seller_products', Seller_views.SELLER_PRODUCTS, name='seller_products'),
    path('Seller/seller_edit_products/<str:id>', Seller_views.SELLER_EDIT_PRODUCTS, name='seller_edit_products'),
    path('Seller/seller_update_products', Seller_views.SELLER_UPDATE_PRODUCTS, name='seller_update_products'),
    path('Seller/seller_delete_products/<str:id>', Seller_views.SELLER_DELETE_PRODUCTS, name='seller_delete_products'),

    # Bidder Panel
    path('Bidder/home', Bidder_views.HOME, name='bidder_home'),
    path('Bidder/b_registration', Bidder_views.REGISTRATION, name='b_registration'),
    path('Bidder/bidder_products', Bidder_views.BIDDER_PRODUCTS, name='bidder_products'),
    path('Bidder/bidder_blog', Bidder_views.BIDDER_BLOG, name='bidder_blog'),
    path('Bidder/bidder_contact_us', Bidder_views.BIDDER_CONTACT_US, name='bidder_contact_us'),
    path('Bidder/bidder_cart', Bidder_views.BIDDER_CART, name='bidder_cart'),
    path('Bidder/bidder_profile', Bidder_views.BIDDER_PROFILE, name='bidder_profile'),
    path('Bidder/bidder_self_blog', Bidder_views.BIDDER_SELF_BLOG, name='bidder_self_blog'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
