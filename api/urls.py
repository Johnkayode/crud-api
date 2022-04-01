from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from .views import *


schema_view = get_swagger_view(title = 'CRUD API')
schema_view.cls.schema = None

urlpatterns = [
    path('customers/', ListAndCreateCustomers.as_view()),
    path("customers/<int:pk>/", GetUpdateDeleteCustomer.as_view()),
    path('docs/', schema_view),  
]
