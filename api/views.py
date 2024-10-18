from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClothingSerializer
from .models import Clothing

# Create your views here.
def index(request):
    return render(request, 'index.html')

class ClothingViewSet(viewsets.ModelViewSet):
    clothes = Clothing.objects.all()
    serializer_class = ClothingSerializer