from django.contrib import admin
from .models import Type, Category, PaymentMethod

admin.site.register(Type)
admin.site.register(Category)
admin.site.register(PaymentMethod)
