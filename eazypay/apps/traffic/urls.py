from  django.urls import path, re_path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('traffic', views.TrafficViewset, base_name='traffic')

app_name = 'traffic'
urlpatterns=[
    path('', include(router.urls)),
]
