from django.urls import path, include
from . import views

urlpatterns = [
    path('<slug:companyname>/', views.send_data, name='company'),
]
