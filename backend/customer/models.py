from django.db import models
from django.templatetags.static import static

class Customer(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(primary_key = True, max_length=254)
    phone = models.CharField(max_length=16, blank=False, null=False)
    photo = models.ImageField(upload_to='customer_pics/')
    
    def __str__(self):
        return self.email
    
class CustomerOtp(models.Model):
    email = models.EmailField(primary_key = True, max_length=254)
    otp = models.PositiveIntegerField()
    created_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email