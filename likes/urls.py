from .views import LikeViewSet
from django.urls import path
urlpatterns = [
    path('', LikeViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'})),
]