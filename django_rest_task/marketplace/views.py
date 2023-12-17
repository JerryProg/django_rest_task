from rest_framework.views import APIView, Response, status
from rest_framework import generics, permissions
from .serializers import MarketplaceSerializer
from .models import MarketplaceModel
from django.shortcuts import get_object_or_404

# Create your views here.
class MarketpAPIView(APIView):
    permission_classes=[permissions.IsAuthenticated
                        ]    
    def post(self, request):
        data = request.data
        serializer = MarketplaceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        item = get_object_or_404(MarketplaceModel.objects.all(), pk=pk)
        serializer = MarketplaceSerializer(item, data=request.data)

        if serializer.is_valid():
            serializer.save()
            #response = {"response" : "Elemento actualizado"}
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def delete(self, request, pk, format=None):
        item = get_object_or_404(MarketplaceModel.objects.all(), pk=pk)
        item.delete()
        response = {"response" : "success, el elemento ha sido borrado"}
        return Response(response, status=status.HTTP_204_NO_CONTENT)
    

class MarketpRetrieveView(generics.RetrieveAPIView):
    queryset = MarketplaceModel.objects.all()
    serializer_class = MarketplaceSerializer


class MarketpListView(generics.ListAPIView):
    queryset = MarketplaceModel.objects.all()
    serializer_class = MarketplaceSerializer