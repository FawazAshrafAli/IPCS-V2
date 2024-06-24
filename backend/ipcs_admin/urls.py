from django.urls import path
from . import views

urlpatterns = [    
    path('', views.admin_login, name="login"),
    path('admin_home/', views.home, name="admin_home"),
    path('logout/', views.admin_logout, name="logout"),
    path('reset_password/', views.reset_password, name="reset_password"),

    path('forgot_admin_password/', views.forgot_admin_password, name='forgot_admin_password'),
    path('reset_forgotten_admin_password/', views.reset_forgotten_admin_password, name='reset_forgotten_admin_password'),

    # clients
    path('clients/', views.list_clients, name="clients"),
    path('add_client/', views.add_client, name="add_client"),
    path('client/<pk>', views.detail_client, name="client"),
    path('update_client/<pk>', views.update_client, name="update_client"),    
    path('delete_client/<pk>', views.delete_client, name="delete_client"),

    # product
    path('products/', views.list_products, name="products"),
    path('add_product/', views.add_product, name="add_product"),
    path('product/<pk>', views.detail_product, name="product"),
    path('update_product/<pk>', views.update_product, name="update_product"),    
    path('delete_product/<pk>', views.delete_product, name="delete_product"),

    # admin warranty
    path('warranty_applications/', views.list_warranty_applications, name="warranty_applications"),
    path('warranty_applications_to_excel/', views.warranty_applications_to_excel, name="warranty_applications_to_excel"),
    path('warranty_application/<pk>', views.detail_warranty_application, name="warranty_application"),
    path('hard_delete_warranty_application/<pk>', views.hard_delete_warranty_application, name="hard_delete_warranty_application"),

    path('complete_warranty/<pk>', views.complete_warranty, name="complete_warranty"),    
    
    path('finished_warranties/', views.list_finished_warranties, name="finished_warranties"),
    path('finished_warranties_to_excel/', views.finished_warranties_to_excel, name="finished_warranties_to_excel"),
    path('finished_warranty/<pk>', views.detail_finished_warranty, name="finished_warranty"),
    path('delete_finished_warranty/<pk>', views.delete_finished_warranty, name="delete_finished_warranty"),
    path('hard_delete_finished_warranty/<pk>', views.hard_delete_finished_warranty, name="hard_delete_finished_warranty"),
    
    path('reject_warranty/<pk>', views.reject_warranty, name="reject_warranty"),    
    
    path('rejected_warranties/', views.list_rejected_warranties, name="rejected_warranties"),
    path('rejected_warranties_to_excel/', views.rejected_warranties_to_excel, name="rejected_warranties_to_excel"),
    path('rejected_warranty/<pk>', views.detail_rejected_warranty, name="rejected_warranty"),
    path('delete_rejected_warranty/<pk>', views.delete_rejected_warranty, name="delete_rejected_warranty"),
    path('hard_delete_rejected_warranty/<pk>', views.hard_delete_rejected_warranty, name="hard_delete_rejected_warranty"),

    # admin technician
    path('add_technician/', views.add_technician, name="add_technician"),
    path('technicians/', views.list_technicians, name="technicians"),
    path('technician/<pk>', views.detail_technician, name="technician"),
    path('update_technician/<pk>', views.update_technician, name="update_technician"),
    path('delete_technician/<pk>', views.delete_technician, name="delete_technician"),

    # admin service
    path('service_requests/', views.list_service_requests , name="service_requests"),
    path('service_requests_to_excel/', views.service_requests_to_excel , name="service_requests_to_excel"),
    path('service_request/<pk>', views.detail_service_request , name="service_request"),
    path('hard_delete_service_request/<pk>', views.hard_delete_service_request, name="hard_delete_service_request"),

    path('accept_service/<pk>', views.accept_service , name="accept_service"),

    path('accepted_services/', views.list_accepted_services , name="accepted_services"),
    path('accepted_services_to_excel/', views.accepted_services_to_excel , name="accepted_services_to_excel"),
    path('accepted_service/<pk>', views.detail_accepted_service , name="accepted_service"),    
    path('delete_accepted_service/<pk>', views.delete_accepted_service , name="delete_accepted_service"),
    path('hard_delete_accepted_service/<pk>', views.hard_delete_accepted_service, name="hard_delete_accepted_service"),
    
    path('complete_service/<pk>', views.complete_service, name="complete_service"),
    
    path('completed_services/', views.list_completed_services, name="completed_services"),
    path('completed_services_to_excel/', views.completed_services_to_excel, name="completed_services_to_excel"),
    path('completed_service/<pk>', views.detail_completed_service, name="completed_service"),
    path('complete_service_file_update/<pk>', views.complete_service_file_update, name="complete_service_file_update"),
    path('delete_completed_service/<pk>', views.delete_completed_service , name="delete_completed_service"),
    path('hard_delete_completed_service/<pk>', views.hard_delete_completed_service, name="hard_delete_completed_service"),
    
    # admin repair
    path('repair_requests/', views.list_repair_requests , name="repair_requests"),
    path('repair_requests_to_excel/', views.repair_requests_to_excel , name="repair_requests_to_excel"),
    path('repair_request/<pk>', views.detail_repair_request , name="repair_request"),
    path('hard_delete_repair_request/<pk>', views.hard_delete_repair_request, name="hard_delete_repair_request"),

    path('start_repair/<pk>', views.start_repair , name="start_repair"),    

    path('started_repairs/', views.list_started_repairs , name="started_repairs"),
    path('started_repairs_to_excel/', views.started_repairs_to_excel , name="started_repairs_to_excel"),
    path('started_repair/<pk>', views.detail_started_repair , name="started_repair"),
    path('delete_started_repair/<pk>', views.delete_started_repair , name="delete_started_repair"),
    path('hard_delete_started_repair/<pk>', views.hard_delete_started_repair, name="hard_delete_started_repair"),

    path('complete_repair/<pk>', views.complete_repair , name="complete_repair"),

    path('completed_repairs/', views.list_completed_repairs , name="completed_repairs"),
    path('completed_repairs_to_excel/', views.completed_repairs_to_excel , name="completed_repairs_to_excel"),    
    path('completed_repair/<pk>', views.detail_completed_repair , name="completed_repair"),
    path('delete_completed_repair/<pk>', views.delete_completed_repair , name="delete_completed_repair"),
    path('hard_delete_completed_repair/<pk>', views.hard_delete_completed_repair, name="hard_delete_completed_repair"),
    
    path('set_repair_ready_to_dispatch/<pk>', views.set_repair_ready_to_dispatch , name="set_repair_ready_to_dispatch"),

    path('repairs_ready_to_dispatch', views.list_repairs_ready_to_dispatch , name="repairs_ready_to_dispatch"),
    path('repairs_ready_to_dispatch_to_excel', views.repairs_ready_to_dispatch_to_excel , name="repairs_ready_to_dispatch_to_excel"),
    path('repair_ready_to_dispatch/<pk>', views.detail_repair_ready_to_dispatch , name="repair_ready_to_dispatch"),
    path('update_repair_ready_to_dispatch_file/<pk>', views.update_repair_ready_to_dispatch_file , name="update_repair_ready_to_dispatch_file"),
    path('delete_repair_ready_to_dispatch/<pk>', views.delete_repair_ready_to_dispatch , name="delete_repair_ready_to_dispatch"),
    path('hard_delete_repair_ready_to_dispatch/<pk>', views.hard_delete_repair_ready_to_dispatch, name="hard_delete_repair_ready_to_dispatch"),


    path('mark_as_viewed_service/<pk>', views.mark_as_viewed_service, name="mark_as_viewed_service"),
    path('mark_as_unread_service/<pk>', views.mark_as_unread_service, name="mark_as_unread_service"),

    path('mark_as_viewed_repair/<pk>', views.mark_as_viewed_repair, name="mark_as_viewed_repair"),
    path('mark_as_unread_repair/<pk>', views.mark_as_unread_repair, name="mark_as_unread_repair"),

    path('mark_as_viewed_warranty/<pk>', views.mark_as_viewed_warranty, name="mark_as_viewed_warranty"),
    path('mark_as_unread_warranty/<pk>', views.mark_as_unread_warranty, name="mark_as_unread_warranty"),

]

