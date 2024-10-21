from django.urls import path, include
from api import views
from rest_framework import routers

app_name = 'api'

route = routers.DefaultRouter()

route.register(r'roupas', views.ClothingViewSet, )

urlpatterns = [
    path('', include(route.urls), name='view-clothes'),
    path('roupas/', views.ClothingView.as_view(), name='clothes'),
    path('roupas/<int:id>/', views.ClothingViewUpdate.as_view(), name='update-clothes'),
]
