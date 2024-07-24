from rest_framework.routers import DefaultRouter
from .views import InstallmentViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'installments',  InstallmentViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = router.urls