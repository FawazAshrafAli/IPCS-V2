from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import Http404
from django.contrib import messages
from django.utils import timezone
from .models import *
from ipcs_admin.models import*
from django.db import IntegrityError
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied, SuspiciousOperation
from django.contrib.auth.decorators import user_passes_test
from ipcs_admin.views import admin_login
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
import random
from django.core.mail import EmailMessage
import mimetypes
from django.views.decorators.cache import never_cache


def not_superuser(user):
    return user.is_authenticated and not user.is_superuser

def generate_otp():
    generated_otp = ''.join(str(random.randint(0, 9)) for _ in range(6))
    return generated_otp

@never_cache
def customer_login(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        return redirect(customer_home)
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            if not user.is_superuser:
                login(request,user)
                return redirect(customer_home)
            else:
                messages.warning(request, "Redirected to admin login page")
                return redirect(admin_login)
        else:
            messages.error(request,"Username or Password is incorrect")
            return redirect(customer_login)
    return render(request, 'customer_sign_in.html')

@never_cache
def forgot_password(request):
    if request.method == "POST":
        username = request.POST.get("email")
        try:
            user = get_object_or_404(User, username = username)
            otp = generate_otp()
            try:
                customer_otp_object = get_object_or_404(CustomerOtp, email = username)
                customer_otp_object.otp = otp
                customer_otp_object.save()
            except Http404:
                CustomerOtp.objects.create(
                    email = username, 
                    otp = otp
                )            
                
            subject = "Reset Password OTP."
            message = f"OTP for resetting your account password is "            
            html_content = render_to_string('customer_email_templates/forgot_password.html', {
                'subject': subject,
                'message': message,
                "email_subject": subject,
                "email_content": message,
                "otp": otp,
                })            
                    

            email = EmailMessage(
                subject=subject,
                body=html_content,
                from_email="ipcshelpyou@gmail.com",
                to=[str(user.username)]
            )
                        

            # Set the content type of the email to 'text/html'
            email.content_subtype = 'html'

            # Send the email
            email.send()

            return redirect(reset_forgotten_password)
        except Http404:
            messages.error(request, "Invalid email id.")
            return redirect(customer_login)

@never_cache
def reset_forgotten_password(request):    
    context = {}
    if request.method == "POST":
        otp = request.POST.get("otp")
        new_password = request.POST.get("new_password")
        repeat_password = request.POST.get("repeat_password")
        if otp:
            try:
                customer_otp_object = get_object_or_404(CustomerOtp, otp = otp)
                if timezone.now() < customer_otp_object.created_time + timedelta(minutes=5):
                    try:
                        user = get_object_or_404(User, username = customer_otp_object.email)
                        username = user.username               
                        user = User.objects.filter(username = username).first()
                        if user is not None:
                            if new_password == repeat_password:
                                user.set_password(new_password)
                                messages.success(request, "Password updated successfully.")
                                user.save()
                                logout(request)
                                return redirect(customer_login)
                            else:
                                messages.warning(request, "New passwords do not match.")
                                return redirect(reset_forgotten_password)
                        else:
                            messages.error(request, "Invalid User.")
                            return redirect(customer_login)
                    except Http404:
                        messages.error("Invalid user.")
                        return redirect(customer_login)
                else:
                    messages.error(request, "OTP timed out.")
                    return redirect(customer_login)
            except Http404:
                messages.error(request, "Invalid OTP.")
                return redirect(reset_forgotten_password)
        else:
            messages.error(request, "OTP cannot be empty.")
            return redirect(reset_forgotten_password)
    return render(request, 'reset_forgotten_password.html', context)    

@user_passes_test(not_superuser, login_url=customer_login)
@never_cache
def customer_logout(request):    
    logout(request)
    return redirect(home)
    
@never_cache
def customer_signup(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        return redirect(customer_home)
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        if password == repeat_password:
            try:
                Customer.objects.create(name=name, email=email, phone=phone)
                User.objects.create_user(username=email, password=password)
                messages.success(request, "Sign Up successfull.")
                return redirect(customer_login)    
            except IntegrityError:
                messages.warning(request,'Account already exists!')
                return redirect(customer_login)
        else:
            messages.error(request, "Passwords do not match.")
            return redirect(customer_signup)
    return render(request, 'customer_signup.html')

@user_passes_test(not_superuser, login_url=customer_login)
@never_cache
def reset_customer_password(request):    
    context = {}
    try:
        customer = get_object_or_404(Customer, email = request.user.username)
        context.update({"customer": customer})
    except Http404:
        pass
    if request.method == "POST":
        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")
        repeat_password = request.POST.get("repeat_password")
        username = request.user.username
        user = authenticate(request, username = username, password = current_password)
        if user is not None:
            if new_password == repeat_password:
                user.set_password(new_password)
                messages.success(request, "Password updated successfully.")
                user.save()
                logout(request)
                return redirect(customer_login)
            else:
                messages.warning(request, "New passwords do not match.")
                return redirect(reset_customer_password)
        else:
            messages.error(request, "Invalid current password.")
            return redirect(reset_customer_password)
    return render(request, 'secured/reset_customer_password.html', context)    

@user_passes_test(not_superuser, login_url=customer_login)    
@never_cache
def customer_account(request):    
    context = {}
    try:
        customer = get_object_or_404(Customer, email = request.user.username)
        context.update({"customer": customer})
    except Http404:
        messages.error(request, "Unauthorized user.")
        return redirect(customer_login)
    return render(request, 'secured/account.html', context)    

@user_passes_test(not_superuser, login_url=customer_login)    
@never_cache
def update_customer_info(request):    
    try:
        if request.method == "POST":
            image = request.FILES.get("image")
            name = request.POST.get("name")
            phone = request.POST.get("phone")
            try:
                customer = get_object_or_404(Customer, email = request.user.username)
                customer.name = name
                customer.phone = phone
                if image:
                    customer.photo = image
                customer.save()
                return redirect(customer_account)
            except Http404:
                messages.error(request, "Unauthorized user.")
                return redirect(customer_login)
    except PermissionDenied:
        return redirect(customer_account)
    except SuspiciousOperation:
        return redirect(customer_account)       

@user_passes_test(not_superuser, login_url=customer_login)
@never_cache
def customer_home(request):
    context = {}
    try:
        customer = get_object_or_404(Customer, email = request.user.username)
        context.update({"customer": customer})
    except Http404:
        pass  
    return render(request, 'secured/customer_home.html', context)

@csrf_exempt
@never_cache
def home(request):
    context = {}
    clients = Client.objects.all()
    context.update({"clients": clients})
    products = Product.objects.all().exclude(name = "Other Products").order_by('name')
    context.update({
        "products": products,
        "first_8_products": products[:8],
        "next_10_products": products[8:18],
        })
    if request.user:
        try:
            customer = get_object_or_404(Customer, email = request.user.username)
            context.update({"customer": customer})
        except Http404:
            pass
    # warranty start

    finished_warranties = False
    rejected_warranties = False
    warranty_application = False    
               
    completed_services = False
    service_request = False
    accepted_service = False

    repair_ready_to_dispatches = False
    completed_repairs = False
    repair_request = False
    started_repair = False

    try:
        if request.method == "POST":
            id = request.POST.get("id")
            if id != "" and " " not in str(id):
                context.update({"id": id})
                
                if str(id).startswith("WTY"):
                    try:
                        warranty_application = get_object_or_404(WarrantyApplication, id = id)                            
                        context.update({"warranty_application": warranty_application})
                    except Http404:
                        pass
                    try:
                        finished_warranties = get_list_or_404(FinishedWarranty, id = id)
                        context.update({"finished_warranties": finished_warranties})
                    except Http404:
                        pass
                    try:
                        rejected_warranties = get_list_or_404(RejectedWarranty, id = id)
                        context.update({"rejected_warranties": rejected_warranties})
                    except Http404:
                        pass
                else:  
                    try:
                        warranty_application = get_object_or_404(WarrantyApplication, serial_number = id)
                        context.update({"warranty_application": warranty_application})
                    except Http404:
                        pass
                    try:
                        finished_warranties = get_list_or_404(FinishedWarranty, serial_number = id)
                        context.update({"finished_warranties": finished_warranties})
                    except Http404:
                        pass
                    try:
                        rejected_warranties = get_list_or_404(RejectedWarranty, serial_number = id)
                        context.update({"rejected_warranties": rejected_warranties})
                    except Http404:
                        pass
            
                if str(id).startswith("SVS"):                    
                    try:
                        service_request = get_object_or_404(ServiceRequest, id = id)                        
                        context.update({
                            "service_request": service_request,                            
                            })
                    except Http404:
                        pass
                    try:
                        accepted_service = get_object_or_404(AcceptedService, id = id)
                        context.update({"accepted_service": accepted_service})
                    except Http404:
                        pass                        
                    try:
                        completed_services = get_list_or_404(CompletedService, id = id)                        
                        context.update({
                            "completed_services": completed_services,                            
                            })
                    except Http404:
                        pass
                else:                    
                    try:
                        service_request = get_object_or_404(ServiceRequest, serial_number = id)                        
                        context.update({
                            "service_request": service_request,                            
                            })
                    except Http404:
                        pass
                    try:
                        accepted_service = get_object_or_404(AcceptedService, serial_number = id)
                        context.update({"accepted_service": accepted_service})
                    except Http404:
                        pass
                    try:
                        completed_services = get_list_or_404(CompletedService, serial_number = id)                                                
                        context.update({
                            "completed_services": completed_services,                            
                            })
                    except Http404:
                        pass
                
                if str(id).startswith("REP"):
                    try:
                        repair_request = get_object_or_404(RepairRequest, id = id)
                        context.update({"repair_request": repair_request})
                    except Http404:
                        pass
                    try:
                        started_repair = get_object_or_404(StartedRepair, id = id)
                        context.update({"started_repair": started_repair})
                    except Http404:
                        pass                        
                    try:
                        completed_repairs = get_list_or_404(CompletedRepair, id = id)                                                
                        context.update({"completed_repairs": completed_repairs})
                    except Http404:
                        pass
                    try:
                        repair_ready_to_dispatches = get_list_or_404(RepairReadyToDispatch, id = id)
                        context.update({"repair_ready_to_dispatches": repair_ready_to_dispatches})
                    except Http404:
                        pass
                else:
                    try:
                        repair_request = get_object_or_404(RepairRequest, serial_number = id)
                        context.update({
                            "repair_request": repair_request})
                    except Http404:
                        pass                                                                                           
                    try:
                        started_repair = get_object_or_404(StartedRepair, serial_number = id)
                        context.update({"started_repair": started_repair})
                    except Http404:
                        pass
                    try:
                        completed_repairs = get_list_or_404(CompletedRepair, serial_number = id)
                        context.update({"completed_repairs": completed_repairs})
                    except Http404:
                        pass
                    try:
                        repair_ready_to_dispatches = get_list_or_404(RepairReadyToDispatch, serial_number = id)
                        context.update({"repair_ready_to_dispatches": repair_ready_to_dispatches})
                    except Http404:
                        pass
                        

    except SuspiciousOperation:
        return render(request, 'home.html', context)
    
    except PermissionDenied:
        return render(request, 'home.html', context)
    return render(request, 'home.html', context)
    

@csrf_exempt
@never_cache
def forgot_id(request):
    if request.method == 'POST':

        warranty_applications = False        
        finished_warranties = False
        rejected_warranties = False
                
        service_requests = False
        accepted_services = False
        completed_services = False                

        repair_requests = False
        started_repairs = False
        completed_repairs = False
        repairs_ready_to_dispatch = False
            
        email = request.POST.get("email")

        try: 
            get_object_or_404(Customer, email = email)
            application = False

            try:
                warranty_applications = get_list_or_404(WarrantyApplication, email_id = email)
                application = True
            except Http404:
                pass                

            try:
                finished_warranties = get_list_or_404(FinishedWarranty, email_id = email)
                application = True
            except Http404:
                pass

            try:
                rejected_warranties = get_list_or_404(RejectedWarranty, email_id = email)
                application = True
            except Http404:
                pass

            try:
                service_requests = get_list_or_404(ServiceRequest, email = email)
                application = True
            except Http404:
                pass

            try:
                accepted_services = get_list_or_404(AcceptedService, email = email)
                application = True
            except Http404:
                pass

            try:
                completed_services = get_list_or_404(CompletedService, email = email)
                application = True
            except Http404:
                pass                

            try:
                repair_requests = get_list_or_404(RepairRequest, email_id = email)
                application = True
            except Http404:
                pass

            try:
                started_repairs = get_list_or_404(StartedRepair, email_id = email)
                application = True
            except Http404:
                pass  

            try:
                completed_repairs = get_list_or_404(CompletedRepair, email_id = email)
                application = True
            except Http404:
                pass

            try:
                repairs_ready_to_dispatch = get_list_or_404(RepairReadyToDispatch, email_id = email)
                application = True
            except Http404:
                pass                
                    
            subject = "Your Product Details and IDs."
            message = f"Your product details are as follows."
            html_content = render_to_string('customer_email_templates/forgot_id.html', {
                'subject': subject,
                'message': message,
                "email_content": message,
                "application": application,
                "warranty_applications": warranty_applications,
                "finished_warranties": finished_warranties,
                "rejected_warranties": rejected_warranties,
                "service_requests": service_requests,
                "accepted_services": accepted_services,
                "completed_services": completed_services,
                "repair_requests": repair_requests,
                "started_repairs": started_repairs,
                "completed_repairs": completed_repairs,
                "repairs_ready_to_dispatch": repairs_ready_to_dispatch,
                })            
                    

            email = EmailMessage(
                subject=subject,
                body=html_content,
                from_email="ipcshelpyou@gmail.com",
                to=[str(email)]
            )
                        

            # Set the content type of the email to 'text/html'
            email.content_subtype = 'html'

            # Send the email
            email.send()

            messages.success(request, "Please check your mail.")
            return redirect(home)
        
    
        except Http404:
            messages.error(request, "Invalid email id.")
            return redirect(home)
    return render(request, 'home.html')

@never_cache
def warranty_request(request):
    context = {}
    clients = Client.objects.all()
    context.update({"clients": clients})
    products = Product.objects.all().exclude(name="Other Products").order_by('name')
    context.update({
        "products": products,
        "first_8_products": products[:8],
        "next_10_products": products[8:18]
        })
    if request.user:
        try:            
            customer = get_object_or_404(Customer, email = request.user.username)
            context.update({"customer": customer})
        except Http404:
            pass
    if request.method == "POST":
        customer_name = request.POST.get("customer_name")
        contact_number = request.POST.get("contact_number")
        email_id = request.POST.get("email_id")
        alternative_number = request.POST.get("alternative_number")
        product = request.POST.get("product")
        try:
            product = get_object_or_404(Product, name = product)
        except Http404:
            if product == "Other Products":
                Product.objects.create(name = product)
                product = get_object_or_404(Product, name = product)
            else:
                messages.error(request, "Invalid product selected.")
                return redirect(warranty_request) 
        except ValueError:
            if product == "Other Products" :
                Product.objects.create(name = product)
                product = get_object_or_404(Product, name = product)
            else:
                messages.error(request, "Invalid product selected.")
                return redirect(warranty_request)            
        billing_name = request.POST.get("billing_name")
        invoice_number = request.POST.get("invoice_number")
        serial_number = request.POST.get("serial_number")
        try:
            get_object_or_404(WarrantyApplication, serial_number = serial_number)
            messages.error(request, "Warranty application has been already submitted.")
            return render(request, 'warranty_request.html', context)
        except Http404:
            pass                
        model_number = request.POST.get("model_number")
        address_customer = request.POST.get("address_customer")
        product_complain = request.POST.get("product_complain")

        current_date = timezone.now()
        last_finished_date = False
        last_rejected_date = False
        last_claimed_date = False
        try:
            last_finished_date = FinishedWarranty.objects.filter(serial_number = serial_number).latest('finished_datetime').finished_datetime
        except:
            pass
        try:
            last_rejected_date = RejectedWarranty.objects.filter(serial_number = serial_number).latest('rejected_datetime').rejected_datetime
        except:
            pass
        if last_finished_date and last_rejected_date:
            if  last_finished_date > last_rejected_date:
                last_claimed_date = last_finished_date
            else:
                last_claimed_date = last_rejected_date
        elif last_finished_date:
            last_claimed_date = last_finished_date
        elif last_rejected_date:
            last_claimed_date = last_rejected_date
        if last_claimed_date:
            available_claimable_date = last_claimed_date + timedelta(days = 30)
            if current_date < available_claimable_date:                
                messages.warning(request, f"The next warranty claimable date will be on or after {available_claimable_date.strftime('%d-%B-%Y')}")
                return render(request, 'warranty_request.html', context)

        try:
            warranty_application = WarrantyApplication.objects.create(            
                customer_name = customer_name,
                contact_number = contact_number,
                email_id = email_id,
                alternative_number = alternative_number,
                product = product,
                billing_name = billing_name,
                invoice_number = invoice_number,
                serial_number = serial_number,
                model_number = model_number,
                address = address_customer,
                product_complain = product_complain
                )
            messages.success(request, "Successfully applied for warranty claim. Submittion mail has been forwarded to your email.")
                                            

            subject = "Warranty Request Submission"
            message = "Warranty Application has been submitted."                           
            html_content = render_to_string('customer_email_templates/warranty_request_submission.html', {
            'subject': subject,
            'message': message,
            "email_subject": subject,
            "email_content": message,
            "id": warranty_application.id,
            "product": warranty_application.product,
            "serial_number": warranty_application.serial_number,
            "model_number": warranty_application.model_number,
            "billing_name": warranty_application.billing_name,
            "invoice_number": warranty_application.invoice_number,
            "product_complain": warranty_application.product_complain,
            "customer_name": warranty_application.customer_name,
            "email": warranty_application.email_id,
            "contact_number": warranty_application.contact_number,
            "address": warranty_application.address,
            "alternative_number": warranty_application.alternative_number
            })            

            email = EmailMessage(
                subject=subject,
                body=html_content,
                from_email="ipcshelpyou@gmail.com",
                to=[str(warranty_application.email_id)]
            )
                        

            # Set the content type of the email to 'text/html'
            email.content_subtype = 'html'

            # Send the email
            email.send()
            
            return redirect(warranty_request)        
        except IntegrityError:
            messages.error(request, "Warranty application has been already submitted.")
            return redirect(warranty_request)
    return render(request, 'warranty_request.html', context)

@never_cache
def request_service(request):
    context = {}
    clients = Client.objects.all()
    context.update({"clients": clients})
    products = Product.objects.all().exclude(name="Other Products").order_by('name')
    context.update({
        "products": products,
        "first_8_products": products[:8],
        "next_10_products": products[8:18],
        })
    if request.user:
        try:
            customer = get_object_or_404(Customer, email = request.user.username)
            context.update({"customer": customer})
        except Http404:
            pass
    if request.method == "POST":
        customer_name = request.POST.get("customer_name")
        contact_number = request.POST.get("contact_number")
        email_id = request.POST.get("email_id")
        alternative_number = request.POST.get("alternative_number")
        product = request.POST.get("product")
        serial_number = request.POST.get("serial_number")
        try:
            get_object_or_404(ServiceRequest, serial_number = serial_number)
            messages.error(request, "Service request has been already submitted.")
            return render(request, 'service_request.html', context)
        except Http404:
            pass
        try:
            get_object_or_404(AcceptedService, serial_number = serial_number)
            messages.error(request, "Service request has been already submitted .")
            return render(request, 'service_request.html', context)
        except Http404:
            pass
        model_number = request.POST.get("model_number")
        address_customer = request.POST.get("address_customer")
        service_description = request.POST.get("service_description")
        try:
            product = get_object_or_404(Product, name = product)
        except Http404:
            if product == "Other Products" :
                Product.objects.create(name = product)
                product = get_object_or_404(Product, name = product)
            else:
                messages.error(request, "Invalid product selected.")
                return redirect(request_service)
        except ValueError:
            if product == "Other Products" :
                Product.objects.create(name = product)
                product = get_object_or_404(Product, name = product)
            else:
                messages.error(request, "Invalid product selected.")
                return redirect(request_service)
        
        current_date = timezone.now()
        last_serviced_date = False
        try:
            last_serviced_date = CompletedService.objects.filter(serial_number = serial_number).latest('completion_datetime').completion_datetime
        except:
            pass
        if last_serviced_date:
            available_service_date = last_serviced_date + timedelta(days = 30)
            if current_date < available_service_date:                
                messages.warning(request, f"The next service will only be available on or after {available_service_date.strftime('%d-%B-%Y')}")
                return render(request, 'service_request.html', context)

        try:
            service_request = ServiceRequest.objects.create(
                customer_name = customer_name,
                contact_number = contact_number,
                email = email_id,
                alternative_number = alternative_number,
                address_site = address_customer,
                product = product,                
                serial_number = serial_number,
                model_number = model_number,
                service_description = service_description,
            )
            messages.success(request, "Service request submitted successfully. Submittion mail has been forwarded to your email.")

            subject = "Service Request Submission"
            message = "Service Request has been submitted."            
            html_content = render_to_string('customer_email_templates/service_request_submissionl.html', {
                'subject': subject,
                'message': message,
                "email_subject": subject,
                "email_content": message,
                "id": service_request.id,
                "product": service_request.product,
                "serial_number": service_request.serial_number,
                "model_number": service_request.model_number,                
                "service_description": service_request.service_description,
                "customer_name": service_request.customer_name,
                "email": service_request.email,
                "contact_number": service_request.contact_number,
                "alternative_number": service_request.alternative_number,
                "address": service_request.address_site
                })            
                    

            email = EmailMessage(
                subject=subject,
                body=html_content,
                from_email="ipcshelpyou@gmail.com",
                to=[str(service_request.email)]
            )
                        

            # Set the content type of the email to 'text/html'
            email.content_subtype = 'html'

            # Send the email
            email.send()

            return redirect(request_service)        
        except IntegrityError:
            messages.error(request, "Service application has been already submitted.")
            return redirect(request_service)                    
        except Exception as e:
            print(f"Error: {e}")
            return redirect(request_service)
    
    return render(request, 'service_request.html', context)    

@never_cache
def request_repair(request):
    context = {}
    clients = Client.objects.all()
    context.update({"clients": clients})
    products = Product.objects.all().exclude(name="Other Products").order_by('name')
    context.update({
        "products": products,
        "first_8_products": products[:8],
        "next_10_products": products[8:18],
        })
    if request.user:
        try:
            customer = get_object_or_404(Customer, email = request.user.username)
            context.update({"customer": customer})
        except Http404:
            pass
    
    if request.method == "POST":
        customer_name = request.POST.get("customer_name")
        alternative_number = request.POST.get("alternative_number")
        address_customer = request.POST.get("address_customer")
        email_id = request.POST.get("email_id")
        product = request.POST.get("product")
        contact_number = request.POST.get("contact_number")
        serial_number = request.POST.get("serial_number")        
        model_number = request.POST.get("model_number")
        item_description = request.POST.get("item_description")
        try:
            product = get_object_or_404(Product, name = product)
        except Http404:
            if product == "Other Products" :
                Product.objects.create(name = product)
                product = get_object_or_404(Product, name = product)
            else:
                messages.error(request, "Invalid product selected.")
                return redirect(request_repair)
        except ValueError:
            if product == "Other Products" :
                Product.objects.create(name = product)
                product = get_object_or_404(Product, name = product)
            else:
                messages.error(request, "Invalid product selected.")
                return redirect(request_repair)

        try:
            get_object_or_404(RepairRequest, serial_number = serial_number)
            messages.error(request, "Repair request has been already submitted.")
            return render(request, 'repair_request.html', context)
        except Http404:
            pass
        try:
            get_object_or_404(StartedRepair, serial_number = serial_number)
            messages.error(request, "Repair request has been already submitted.")
            return render(request, 'repair_request.html', context)
        except Http404:
            pass
        try:
            get_object_or_404(CompletedRepair, serial_number = serial_number)
            messages.error(request, "Repair request has been already submitted.")
            return render(request, 'repair_request.html', context)
        except Http404:
            pass

        current_date = timezone.now()
        last_repaired_date = False
        try:
            last_repaired_date = RepairReadyToDispatch.objects.filter(serial_number = serial_number).latest('dispatch_ready_datetime').dispatch_ready_datetime
        except:
            pass
        if last_repaired_date:
            available_repair_date = last_repaired_date + timedelta(days = 90)
            if current_date < available_repair_date:                
                messages.warning(request, f"The next repair will only be available on or after {available_repair_date.strftime('%d-%B-%Y')}")
                return render(request, 'repair_request.html', context)
        try:
            repair_request = RepairRequest.objects.create(
                customer_name = customer_name,
                alternative_number = alternative_number,
                address_customer = address_customer,
                email_id = email_id,
                product = product,
                contact_number = contact_number,
                serial_number = serial_number,
                model_number = model_number,
                item_description = item_description,                
            )            

            subject = "Repair Request Submission"
            message = "Repair Request has been submitted."            
            html_content = render_to_string('customer_email_templates/repair_request_submission.html', {
                'subject': subject,
                'message': message,
                "email_subject": subject,
                "email_content": message,
                "id": repair_request.id,
                "product": repair_request.product,
                "serial_number": repair_request.serial_number,
                "model_number": repair_request.model_number,                
                "repair_description": repair_request.item_description,
                "customer_name": repair_request.customer_name,
                "email": repair_request.email_id,
                "contact_number": repair_request.contact_number,
                "alternative_number": repair_request.alternative_number,
                "address": repair_request.address_customer
                })
                    

            email = EmailMessage(
                subject=subject,
                body=html_content,
                from_email="ipcshelpyou@gmail.com",
                to=[str(repair_request.email_id)]
            )
                        

            # Set the content type of the email to 'text/html'
            email.content_subtype = 'html'

            # Send the email
            email.send()

            messages.success(request, "Repair request submitted successfully. Submittion mail has been forwarded to your email.")             

            return redirect(request_repair)
        except IntegrityError:
            messages.warning(request, "Repair request has been already submitted.")
            return render(request, 'repair_request.html', context)
        except Exception as e:
            print(e)
            return render(request, 'repair_request.html', context)
    
    return render(request, 'repair_request.html', context)

@user_passes_test(not_superuser, login_url=customer_login)
@never_cache
def warranty_history(request):
    context = {}    
    try:
        customer = get_object_or_404(Customer, email = request.user.username)
        context.update({"customer": customer})
    except Http404:
        pass  
    username = request.user.username
    finished_warranties = False
    rejected_warranties = False    
    warranty_applications = False

    try:
        finished_warranties = get_list_or_404(FinishedWarranty, email_id = username)
        context.update({"finished_warranties" : finished_warranties})
    except Http404:
        pass

    try:
        rejected_warranties = get_list_or_404(RejectedWarranty, email_id = username)
        context.update({"rejected_warranties" : rejected_warranties})
    except Http404:
        pass    

    try:
        warranty_applications = get_list_or_404(WarrantyApplication, email_id = username)
        context.update({"warranty_applications" : warranty_applications})
    except Http404:
        pass

    return render(request, 'secured/warranty_history.html', context)    

@user_passes_test(not_superuser, login_url=customer_login)
@never_cache
def service_history(request):
    context = {}    
    try:
        customer = get_object_or_404(Customer, email = request.user.username)
        context.update({"customer": customer})
    except Http404:
        pass  
    username = request.user.username    
    completed_services = False
    accepted_services = False
    service_requests = False

    try:
        completed_services = get_list_or_404(CompletedService, email = username)
        context.update({"completed_services" : completed_services})
    except Http404:
        pass

    try:
        accepted_services = get_list_or_404(AcceptedService, email = username)
        context.update({"accepted_services" : accepted_services})
    except Http404:
        pass

    try:
        service_requests = get_list_or_404(ServiceRequest, email = username)
        context.update({"service_requests" : service_requests})
    except Http404:
        pass

    return render(request, 'secured/service_history.html', context)    

@user_passes_test(not_superuser, login_url=customer_login)
@never_cache
def repair_history(request):
    context = {}    
    try:
        customer = get_object_or_404(Customer, email = request.user.username)
        context.update({"customer": customer})
    except Http404:
        pass  
    username = request.user.username
    completed_repairs = False
    started_repairs = False
    repair_requests = False
    repair_ready_to_dispatches = False

    try:
        repair_ready_to_dispatches = get_list_or_404(RepairReadyToDispatch, email_id = username)
        context.update({"repair_ready_to_dispatches" : repair_ready_to_dispatches})
    except Http404:
        pass

    try:
        completed_repairs = get_list_or_404(CompletedRepair, email_id = username)
        context.update({"completed_repairs" : completed_repairs})
    except Http404:
        pass

    try:
        started_repairs = get_list_or_404(StartedRepair, email_id = username)
        context.update({"started_repairs" : started_repairs})
    except Http404:
        pass

    try:
        repair_requests = get_list_or_404(RepairRequest, email_id = username)
        context.update({"repair_requests" : repair_requests})
    except Http404:
        pass

    return render(request, 'secured/repair_history.html', context)    
