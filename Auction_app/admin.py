from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class UserModel(UserAdmin):
    list_display = ['username','user_type']

class ImagesTublerinline(admin.TabularInline):
    model = Images

class TagTublerinline(admin.TabularInline):
    model = Tag

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImagesTublerinline,TagTublerinline]



admin.site.register(CustomUser,UserModel)
admin.site.register(Seller)
admin.site.register(Bidder)

admin.site.register(Product,ProductAdmin)
admin.site.register(Filter_Price)
admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(Categories)
admin.site.register(Images)
admin.site.register(Tag)
admin.site.register(Seller_Notification)
admin.site.register(Admin_Notification)