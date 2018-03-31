from django.contrib import admin
from django.urls import path, include
from eazypay.apps.payments import urls as payment_urls

urlpatterns = [
    path('developpers/', admin.site.urls),
    path('payments/',include( payment_urls, namespace='payments')),
]
