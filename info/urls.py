from django.conf.urls import url
from django.conf.urls import include
from rest_framework import routers

from . import views
from .views import InfoViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('info', views.InfoViewSet)



urlpatterns = [

    url(r'', include(router.urls)),



]