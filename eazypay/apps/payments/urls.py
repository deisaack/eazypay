from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('payment', views.PaymentViewset, base_name='payment')

app_name = 'payments'

urlpatterns = [
    path('EazypayEndpoint/', views.receive_paument, name='receive_payment')
]
urlpatterns+=router.urls