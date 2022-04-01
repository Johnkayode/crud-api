from rest_framework import serializers, generics, status

from .models import Customer



class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = (
            "id",
            "first_name", 
            "last_name", 
            "email", 
            "city", 
            "state", 
            "phone_number"
        )
