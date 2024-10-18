from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ClothingSerializer
from .models import Clothing

# Create your views here.
def index(request):
    return render(request, 'index.html')

class ClothingView(APIView):
    def get(self, request):
        clothes = Clothing.objects.all()
        serializer = ClothingSerializer(clothes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

