from django.urls import path
from .import views

urlpatterns = [
    
    path("info/",views.order_form,name='inquary_form'),
    path("show_info/",views.show_order,name='show_info'),
    path("info_update/<int:id>/",views.update_order,name='update_info'),
    path("info_delete/<int:id>/",views.delete_order,name='delete_info'),

]