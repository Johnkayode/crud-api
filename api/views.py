#API VIews
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.schemas import AutoSchema

from .models import Customer
from .serializers import CustomerSerializer

import coreapi


# List and Create customers
class ListAndCreateCustomers(ListCreateAPIView, PageNumberPagination):


    permission_classes = (AllowAny,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# Get, Update or Delete customers
class GetUpdateDeleteCustomer(RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


