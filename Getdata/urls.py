from django.urls import path, include
from . import views

urlpatterns = [
    path('webhook/<companyname>/', views.send_data, name='company'),
]
