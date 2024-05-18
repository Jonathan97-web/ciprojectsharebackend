from django.urls import path
from .views import ProfileViewSet

urlpatterns = [
    path('', ProfileViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/', ProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]