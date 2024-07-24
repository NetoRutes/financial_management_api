from rest_framework import serializers
from .models import Category, PaymentMethod, Type

class CategorySeralizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'