from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name="home"),
    path('customer_login/', views.customer_login, name="customer_login"),
    path('customer_signup/', views.customer_signup , name="customer_signup"),
    path('customer_logout/', views.customer_logout, name="customer_logout"),
    path('home/', views.customer_home, name="customer_home"),

    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_forgotten_password/', views.reset_forgotten_password, name='reset_forgotten_password'),
    
    path('request_service/', views.request_service , name="request_service"),
    path('warranty_request/', views.warranty_request , name="warranty_request"),
    path('request_repair/', views.request_repair , name="request_repair"),
    
    path('reset_customer_password/', views.reset_customer_password, name="reset_customer_password"),
    path('customer_account/', views.customer_account, name="customer_account"),
    path('update_customer_info/', views.update_customer_info, name="update_customer_info"),
    path('forgot_id/', views.forgot_id , name="forgot_id"), 

    path('warranty_history/', views.warranty_history , name="warranty_history"),
    path('service_history/', views.service_history , name="service_history"),
    path('repair_history/', views.repair_history , name="repair_history"),
]
