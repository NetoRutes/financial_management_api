from django.db import models
from common.models import Category, PaymentMethod, Base
from core.models import User

class Transaction(Base):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    value =  models.FloatField()
    description = models.CharField(max_length=200)
    date = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='transaction_creator')
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='transaction_owner')
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT)
    num_installments = models.IntegerField(default=1)


class Installment(Base):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    value = models.FloatField()
    due_date = models.DateField()
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f'Installment {self.number} of {self.transaction.description}'
