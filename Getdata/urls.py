from django.urls import path, include
from . import views

urlpatterns = [
    path('<companyname>/', views.send_data, name='company'),
]
