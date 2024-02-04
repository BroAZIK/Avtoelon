from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics
from .models import *
from .serializers import *

class Usersview(APIView):
    def get(self, request: Request):
        index_var = users.objects.all()

        serializer = usersSerializer(index_var, many=True)
        return Response(serializer.data)
    
    def post(self, request: Request):
        data = request.data
        serializer = usersSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    def get(self, request: Request, pk):
        try:
            user = users.objects.get(user_id=pk)
        except users.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        serializer = usersSerializer(user)
        return Response(serializer.data)
    