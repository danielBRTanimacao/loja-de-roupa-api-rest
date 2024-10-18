from django.urls import path
from api import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/roupas', views.ClothingView.as_view(), name='clothes'),
]
