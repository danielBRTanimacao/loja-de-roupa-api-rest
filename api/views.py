from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import ClothingSerializer
from .models import Clothing

# Create your views here.
class ClothingView(APIView):
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.request.method in ['POST', 'DELETE']:
            return [IsAuthenticated()]
        return super().get_permissions()

    def get(self, request):
        clothes = Clothing.objects.all()
        serializer = ClothingSerializer(clothes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ClothingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
class ClothingViewUpdate(ClothingView):
    def get(self, request, id):
        clothes = get_object_or_404(Clothing, pk=id)
        serializer = ClothingSerializer(clothes)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        clothing = get_object_or_404(Clothing, pk=id)
        name = clothing.name
        clothing.delete()
        return Response({'message': f'Book deleted "{name}"'}, status=status.HTTP_204_NO_CONTENT)
