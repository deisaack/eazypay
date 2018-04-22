from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('payment', views.PaymentViewset, base_name='payment')

app_name = 'payments'

urlpatterns = [
    path('CheckPayment/<str:transaction_ref_no>/', views.check_payment, name='check_payment'),
    path('EazypayEndpoint/', views.receive_payment, name='receive_payment')
]
urlpatterns+=router.urls
