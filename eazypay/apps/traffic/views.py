from django.shortcuts import render
from rest_framework import viewsets
from .models import Traffic
from . import serializers as sz
from . import filters as ft
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from eazypay.apps.traffic.models import Traffic

class TrafficViewset(viewsets.ModelViewSet):
    queryset = Traffic.objects.all()
    order_fields = ('created',)
    ordering = ('-created',)
    serializer_class = sz.TrafficSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)


