from django.db import models
from datetime import timedelta
import uuid
from django.templatetags.static import static


class AdminOtp(models.Model):
    email = models.EmailField(max_length=254, blank=False, null=False, unique=True)
    otp = models.PositiveIntegerField()
    created_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

class Client(models.Model):
    name = models.CharField(blank=False, null=False, max_length=150, unique = True)
    image = models.ImageField(upload_to='client_images/')


class Product(models.Model):
    name = models.CharField(blank=False, null=False, max_length=150, unique=True)
    image = models.ImageField(upload_to='product_images/')
    link = models.URLField(max_length=250, null=False, blank=False)
    

    def __str__(self):
        return self.name

class Technician(models.Model):
    name = models.CharField(blank=False, null=False, max_length=150)
    email = models.EmailField(blank=False, null=False, max_length=254, unique=True)
    mobile = models.CharField(blank=False, null=False, max_length=20, unique=True)
    department = models.CharField(blank=False, null=False, max_length=200)
    residential_location = models.TextField()
    photo = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.name
    
def warranty_unique_id(): # for creating an unique id for warranty
    return "WTY" + (str(uuid.uuid4().hex)[:9]).upper()

class WarrantyApplication(models.Model):
    id = models.CharField(max_length=50, primary_key=True, default=warranty_unique_id, editable=False)
    application_datetime = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(blank=False, null=False, max_length=150)    
    contact_number = models.CharField(blank=False, null=False, max_length=20)
    email_id = models.EmailField(blank=False, null=False, max_length=254)
    alternative_number = models.CharField(blank=True, null=True, max_length=20)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    billing_name = models.CharField(blank=False, null=False, max_length=150)
    invoice_number = models.CharField(blank=False, null=False, max_length=50)
    serial_number = models.CharField(blank=False, null=False, max_length=50)
    model_number = models.CharField(blank=False, null=False, max_length=50)    
    product_complain = models.TextField(blank=False, null=False)
    address = models.TextField(blank=False, null=False)
    viewed = models.BooleanField(default=False)

    def __str__(self):
        return self.id

class FinishedWarranty(models.Model):
    id = models.CharField(primary_key=True, max_length=50)    
    application_datetime = models.DateTimeField()
    finished_datetime =  models.DateTimeField(auto_now_add = True)
    customer_name = models.CharField(blank=False, null=False, max_length=150)    
    contact_number = models.CharField(blank=False, null=False, max_length=20)
    email_id = models.EmailField(blank=False, null=False,   max_length=254)
    alternative_number = models.CharField(blank=True, null=True, max_length=20)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    billing_name = models.CharField(blank=False, null=False, max_length=150)
    invoice_number = models.CharField(blank=False, null=False, max_length=50)
    serial_number = models.CharField(blank=False, null=False, max_length=50)
    model_number = models.CharField(blank=False, null=False, max_length=50)
    address = models.TextField(blank=False, null=False)
    product_complain = models.TextField(blank=False, null=False)    
    remark = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.id
    
class RejectedWarranty(models.Model):
    id = models.CharField(primary_key=True, max_length=50)    
    application_datetime = models.DateTimeField()
    rejected_datetime =  models.DateTimeField(auto_now_add = True)
    customer_name = models.CharField(blank=False, null=False, max_length=150)    
    contact_number = models.CharField(blank=False, null=False, max_length=20)
    email_id = models.EmailField(blank=False, null=False,   max_length=254)
    alternative_number = models.CharField(blank=True, null=True, max_length=20)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    billing_name = models.CharField(blank=False, null=False, max_length=150)
    invoice_number = models.CharField(blank=False, null=False, max_length=50)
    serial_number = models.CharField(blank=False, null=False, max_length=50)
    model_number = models.CharField(blank=False, null=False, max_length=50)
    address = models.TextField(blank=False, null=False)
    product_complain = models.TextField(blank=False, null=False)
    reason = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.id    
    
def service_unique_id():    # to create an unique id for Service Request
    return "SVS" + (str(uuid.uuid4().hex)[:9]).upper()

class ServiceRequest(models.Model):
    id = models.CharField(max_length=50, primary_key=True, default=service_unique_id, editable=False)
    customer_name = models.CharField(blank=False, null=False, max_length=150)
    email = models.EmailField(blank=False, null=False, max_length=254)
    application_datetime = models.DateTimeField(auto_now_add=True)    
    alternative_number = models.CharField(blank=True, null=True, max_length=20)
    address_site = models.TextField(blank=False, null=False)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    contact_number = models.CharField(blank=False, null=False, max_length=20)
    serial_number = models.CharField(blank=False, null=False, max_length=50, unique=True)
    model_number = models.CharField(blank=True, null=True, max_length=50)    
    service_description = models.TextField(blank=False, null=False)
    viewed = models.BooleanField(default=False)

    def __str__(self):
        return self.id

class AcceptedService(models.Model):
    id = models.CharField(max_length=50, primary_key=True, editable=False)    
    application_datetime = models.DateTimeField()
    accepted_datetime = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(blank=False, null=False, max_length=150)
    address_site = models.TextField(blank=False, null=False)
    email = models.EmailField(blank=False, null=False, max_length=254)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    contact_number = models.CharField(blank=False, null=False, max_length=20)
    alternative_number = models.CharField(blank=True, null=True, max_length=20)
    serial_number = models.CharField(blank=False, null=False, max_length=50, unique=True)
    model_number = models.CharField(blank=True, null=True, max_length=50)
    service_description = models.TextField(blank=False, null=False)
    remark = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.id

class CompletedService(models.Model):
    id = models.CharField(max_length=50, primary_key=True, editable=False) 
    application_datetime = models.DateTimeField()
    accepted_datetime = models.DateTimeField()
    completion_datetime = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(blank=False, null=False, max_length=150)
    email = models.EmailField(blank=False, null=False, max_length=254)     
    alternative_number = models.CharField(blank=True, null=True, max_length=20)
    address_site = models.TextField(blank=False, null=False)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    contact_number = models.CharField(blank=False, null=False, max_length=20)    
    serial_number = models.CharField(blank=False, null=False, max_length=50)    
    model_number = models.CharField(blank=True, null=True, max_length=50)
    service_description = models.TextField(blank=False, null=False)
    remark = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to="completed service files/", max_length=100, blank=True, null=True)

    def __str__(self):
        return self.id

def repair_unique_id():
    return "REP" + (str(uuid.uuid4().hex)[:9]).upper()

class RepairRequest(models.Model):
    id = models.CharField(max_length=50, primary_key=True, default=repair_unique_id, editable=False)
    customer_name = models.CharField(blank=False, null=False, max_length=150)
    address_customer = models.TextField(blank=False, null=False)
    email_id = models.EmailField(blank=False, null=False, max_length=254)
    application_datetime = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    contact_number = models.CharField(blank=False, null=False, max_length=20)
    alternative_number = models.CharField(blank=True, null=True, max_length=20)
    serial_number = models.CharField(blank=False, null=False, max_length=50, unique=True)
    model_number = models.CharField(blank=False, null=False, max_length=50)
    item_description = models.TextField(blank=False, null=False)
    viewed = models.BooleanField(default=False)

    def __str__(self):
        return self.id

class StartedRepair(models.Model):
    id = models.CharField(max_length=50, primary_key=True, editable=False)    
    application_datetime = models.DateTimeField()
    started_datetime = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(blank=False, null=False, max_length=150)
    address_customer = models.TextField(blank=False, null=False)
    email_id = models.EmailField(blank=False, null=False, max_length=254)    
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    contact_number = models.CharField(blank=False, null=False, max_length=20)
    alternative_number = models.CharField(blank=True, null=True, max_length=20)
    serial_number = models.CharField(blank=False, null=False, max_length=50, unique=True)
    model_number = models.CharField(blank=False, null=False, max_length=50)
    item_description = models.TextField(blank=False, null=False)    

    def __str__(self):
        return self.id
    
class CompletedRepair(models.Model):
    id = models.CharField(max_length=50, primary_key=True, editable=False) 
    application_datetime = models.DateTimeField()
    started_datetime = models.DateTimeField()
    completion_datetime = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(blank=False, null=False, max_length=150)
    address_customer = models.TextField(blank=False, null=False)
    email_id = models.EmailField(blank=False, null=False, max_length=254)    
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    contact_number = models.CharField(blank=False, null=False, max_length=20)
    alternative_number = models.CharField(blank=True, null=True, max_length=20)
    serial_number = models.CharField(blank=False, null=False, max_length=50)
    model_number = models.CharField(blank=False, null=False, max_length=50)
    item_description = models.TextField(blank=False, null=False)    

    def __str__(self):
        return self.id

class RepairReadyToDispatch(models.Model):
    id = models.CharField(max_length=50, primary_key=True, editable=False) 
    application_datetime = models.DateTimeField()
    started_datetime = models.DateTimeField()
    completion_datetime = models.DateTimeField()
    dispatch_ready_datetime = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(blank=False, null=False, max_length=150)
    address_customer = models.TextField(blank=False, null=False)
    email_id = models.EmailField(blank=False, null=False, max_length=254)    
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    contact_number = models.CharField(blank=False, null=False, max_length=20)
    alternative_number = models.CharField(blank=True, null=True, max_length=20)
    serial_number = models.CharField(blank=False, null=False, max_length=50)
    model_number = models.CharField(blank=False, null=False, max_length=50)
    item_description = models.TextField(blank=False, null=False)    
    remark = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to="repair_ready_to_dispatch_files/", max_length=100, blank=True, null=True)

    def __str__(self):
        return self.id