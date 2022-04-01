from django.urls import path
from .views import *

urlpatterns = [
    path('customers/', ListAndCreateCustomers.as_view()),
    path("customers/<int:pk>/", GetUpdateDeleteCustomer.as_view()),    
]
