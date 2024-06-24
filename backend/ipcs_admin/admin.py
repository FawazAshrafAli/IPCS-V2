from django.contrib import admin
from .models import *

class TechnicianAdmin(admin.ModelAdmin):
    list_display = [
        "name", "email", "mobile", "department",
        "residential_location"
        ]
admin.site.register(Technician, TechnicianAdmin)

class WarrantyApplicationAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "application_datetime",
        "customer_name",
        "contact_number",
        "email_id",
        "alternative_number",
        "billing_name",
        "invoice_number",
        "serial_number",
        "model_number",        
    ]
admin.site.register(WarrantyApplication, WarrantyApplicationAdmin)

admin.site.register(FinishedWarranty)

class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "customer_name", "email",
        "application_datetime", "alternative_number",
        "address_site", "product",
        "contact_number",
        "serial_number", "service_description"
    ]
admin.site.register(ServiceRequest, ServiceRequestAdmin)

admin.site.register(AcceptedService)

admin.site.register(CompletedService)

admin.site.register(RepairRequest)

admin.site.register(StartedRepair)