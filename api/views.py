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
        if self.request.method == 'POST':
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
    
    def delete(self, request):
        ids = request.data.get("ids", [])
        if not ids:
            return Response(
                {"detail": "Nenhum ID fornecido."},
                status=status.HTTP_400_BAD_REQUEST
            )
        deleted, _ = Clothing.objects.filter(id__in=ids).delete()
        if deleted:
            return Response(
                {"detail": f"{deleted} itens deletados com sucesso."},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"detail": "Nenhum item encontrado para os IDs fornecidos."},
                status=status.HTTP_404_NOT_FOUND
            )

