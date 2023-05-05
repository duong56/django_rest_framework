from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls))
]