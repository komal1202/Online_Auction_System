from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class CustomUser(AbstractUser):
    USER =(
        (1,'Admin'),
        (2,'Seller'),
        (3,'Bidder'),
    )
    user_type = models.CharField(choices=USER,max_length=50,default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')



class Seller(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    mobile_no = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return self.admin.username

class Bidder(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    mobile_no = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return self.admin.username


class Categories(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Filter_Price(models.Model):
    FILTER_PRICE = (
        ('1000 To 10000','1000 To 10000'),
        ('10000 To 20000','10000 To 20000'),
        ('20000 To 30000','20000 To 30000'),
        ('30000 To 40000','30000 To 40000'),
        ('40000 To 50000','40000 To 50000'),
        ('50000 To 60000','50000 To 60000'),
        ('60000 To 70000','60000 To 70000'),
        ('70000 To 80000','70000 To 80000'),
        ('80000 To 90000','80000 To 90000'),
        ('90000 To 100000','90000 To 100000'),
    )
    price = models.CharField(choices=FILTER_PRICE,max_length=100)

    def __str__(self):
        return self.price



class Product(models.Model):
    CONDITION = (('New','New'),('Old','Old'))
    STOCK = ('In stock','In stock'),('Sold out','Sold out')

    seller_id = models.ForeignKey(Seller,on_delete=models.CASCADE)
    unique_id = models.CharField(unique = True,max_length=200,null=True,blank=True)
    image = models.ImageField(upload_to='media/products')
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    condition = models.CharField(choices=CONDITION, max_length=100)
    information = models.TextField()
    description = models.TextField()
    stock = models.CharField(choices=STOCK, max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(default=0)

    categories = models.ForeignKey(Categories,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    filter_price = models.ForeignKey(Filter_Price,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.unique_id is None and self.created_date and self.id:
            self.unique_id = self.created_date.strftime('75%Y%m%d24') + str(self.id)
        return super().save(*args,**kwargs)

    def __str__(self):
        return self.name



class Images(models.Model):
    image = models.ImageField(upload_to ='media/products')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)



class Tag(models.Model):
    name = models.CharField(max_length=200)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Seller_Notification(models.Model):
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True,default=0)

    def __str__(self):
        return f"Notification for {self.seller_id.admin.username}"



class Admin_Notification(models.Model):
    admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 1})
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True,default=0)

    def __str__(self):
        return self.admin.username