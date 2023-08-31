from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

# user profile model

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') # default image is default.jpg and it will be uploaded to profile_pics folder
    is_verified = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.user.username} Profile'
    
#product models
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='product_pics')
    def __str__(self):
        return self.name
    
    
# store model
class Store(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    # product has many to many relationship with store
    product = models.ManyToManyField(Product)
    website = models.URLField(max_length=200)
    # store logo is optional
    logo = models.ImageField(default='default.jpg', upload_to='store_pics', blank=True)
    # store owner is optional
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    # cordinates of store
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    # store is verified or not
    is_verified = models.BooleanField(default=False)
    # store is active or not
    is_active = models.BooleanField(default=True)
    # store is open or not
    def __str__(self):
        return self.name
# favourite model for user to add their favourite stores
class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey('Store', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user.username} Favourite'