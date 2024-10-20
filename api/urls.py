from django.urls import path
from api import views

urlpatterns = [
    path('roupas/', views.ClothingView.as_view(), name='clothes'),
    path('roupas/<int:id>/', views.ClothingViewUpdate.as_view(), name='update-clothes'),
]
