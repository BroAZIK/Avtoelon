from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics
from .models import *
from .serializers import *

class Indexview(APIView):
    def get(self, request: Request):
        index_var = index.objects.all()

        serializer = IndexSerializer(index_var, many=True)
        return Response(serializer.data)
    
    def post(self, request: Request):
        data = request.data
        serializer = IndexSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Indexdetailview(APIView):
    def get(self, request: Request, pk: int):
        lndex = index.objects.get(user_id=pk)
        try:
            serializer = IndexSerializer(lndex)
            return Response(serializer.data)
        except lndex.DoesNotExist:
            return Response({"error": "User not found"}, status=404)
        

    def put(self, request: Request, pk: int) -> Response:
        data = request.data
        task = index.objects.get(user_id=pk)
        serializer = IndexSerializer(task, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)       
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int) -> Response:
        index.objects.get(user_id=pk).delete()

        return Response({'message': 'deleted.'}, status=status.HTTP_200_OK)