from rest_framework import viewsets
from .serializers import InstallmentSerializer, TransactionSerializer
from .models import Installment, Transaction

class InstallmentViewSet(viewsets.ModelViewSet):
    queryset = Installment.objects.all()
    serializer_class = InstallmentSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
