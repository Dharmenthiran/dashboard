from django.urls import path
from .import views

urlpatterns=[
    path('', views.login, name='login'),
    path('home',views.dashboard,name='Home'),
    path('mechin',views.mechine,name='Mechine'),
    path('create_mechin',views.createMechine,name='create_Mechine'),
    path('update_mechine/<str:pk>/',views. updateMechine, name='update_Mechine'),
    path('delete_mechin/<str:pk>/',views. deleteMechin, name='delete_Mechin'),
    path('update_delete/',views.update_delete_Mechine, name='update_delete_Mechine'),
]