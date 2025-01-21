from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name="index"),
    path('view_info/<int:id>/', views.view_info, name='view_info'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('delete_employee/<int:id>/', views.delete_employee, name='delete_employee'),
    path('update/<int:id>/', views.update_employee, name='update_employee'), 
]