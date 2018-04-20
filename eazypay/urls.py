from django.contrib import admin
from django.urls import path, include
from eazypay.apps.payments import urls as payment_urls
from eazypay.apps.traffic import urls as traffic_urls

urlpatterns = [
    path('developpers/', admin.site.urls),
    path('payments/',include( payment_urls, namespace='payments')),
    path('traffic/',include( traffic_urls, namespace='traffic')),
]
