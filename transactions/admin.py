from django.contrib import admin
from .models import Transaction, Installment

admin.site.register(Transaction)
admin.site.register(Installment)