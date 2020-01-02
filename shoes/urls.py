from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include
from shoes import models, views
from rest_framework import routers

# admin.site.register(models.Manufacturer)
# admin.site.register(models.ShoeType)
# admin.site.register(models.ShoeColor)
# admin.site.register(models.Shoe)


router = routers.DefaultRouter()
router.register(r'shoe', views.ShoeViewSet)
router.register(r'manufacturer', views.ManufacturerViewSet)
router.register(r'shoetype', views.ShoeTypeViewSet)
router.register(r'shoecolor', views.ShoeColorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls))
]