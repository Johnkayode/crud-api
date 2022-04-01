#API VIews
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from .models import Customer
from .serializers import CustomerSerializer


# List and Create customers
class ListAndCreateCustomers(ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# Get, Update or Delete customers
class GetUpdateDeleteCustomer(RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


