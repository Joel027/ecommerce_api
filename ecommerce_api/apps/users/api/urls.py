from django.urls import path
from apps.users.api.api import user_api_views , user_detail_api_view


urlpatterns = [
    path('',user_api_views, name='usuario_api'),
    path('<int:pk>/',user_detail_api_view, name='usuario_detail_api'),
]