from api import views
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('cityapi' , views.city_api , basename="city_base")
router.register('adminapi' , views.admin_api , basename="admin_base")
router.register('majorapi' , views.major_api , basename="major_base")

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
