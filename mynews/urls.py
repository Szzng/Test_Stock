from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'api/mynews'

router = DefaultRouter()
router.register(r'', views.MyNewsViewSet, basename='mynews')

urlpatterns = [
    path('', include(router.urls)),
]