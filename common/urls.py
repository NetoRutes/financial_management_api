from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, PaymentMethodViewSet, TypeViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'payment_methods', PaymentMethodViewSet)
router.register(r'types', TypeViewSet)

urlpatterns = router.urls