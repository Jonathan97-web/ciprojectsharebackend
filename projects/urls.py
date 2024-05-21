from .views import ProjectViewSet
from django.urls import path

urlpatterns = [
    path('', ProjectViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'})),
    path('<int:pk>/', ProjectViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'}))
]