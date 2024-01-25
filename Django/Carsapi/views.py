from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics
from .models import *
from .serializers import *

class Laboview(APIView):
    def get(self, request: Request):
        avto = Labo.objects.all()

        serializer = LaboSerializer(avto, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        data = request.data
        serializer = LaboSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Sparkview(APIView):
    def get(self, request: Request):
        avto = Spark.objects.all()

        serializer = SparkSerializer(avto, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        data = request.data
        serializer = SparkSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Damasview(APIView):
    def get(self, request: Request):
        avto = Damas.objects.all()

        serializer = DamasSerializer(avto, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        data = request.data
        serializer = DamasSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Nexiaview(APIView):
    def get(self, request: Request):
        avto = Nexia.objects.all()

        serializer = NexiaSerializer(avto, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        data = request.data
        serializer = NexiaSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Cobaltview(APIView):
    def get(self, request: Request):
        avto = Cobalt.objects.all()

        serializer = CobaltSerializer(avto, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        data = request.data
        serializer = CobaltSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Gentraview(APIView):
    def get(self, request: Request):
        avto = Gentra.objects.all()

        serializer = GentraSerializer(avto, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        data = request.data
        serializer = GentraSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Lacettiview(APIView):
    def get(self, request: Request):
        avto = Lacetti.objects.all()

        serializer = LacettiSerializer(avto, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        data = request.data
        serializer = LacettiSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Malibuview(APIView):
    def get(self, request: Request):
        avto = Malibu.objects.all()

        serializer = MalibuSerializer(avto, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        data = request.data
        serializer = MalibuSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Malibu2view(APIView):
    def get(self, request: Request):
        avto = Malibu2.objects.all()

        serializer = Malibu2Serializer(avto, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        data = request.data
        serializer = MalibuSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Equinoxview(APIView):
    def get(self, request: Request):
        avto = Equinox.objects.all()

        serializer = EquinoxSerializer(avto, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        data = request.data
        serializer = EquinoxSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Monzaview(APIView):
    def get(self, request: Request):
        avto = Monza.objects.all()

        serializer = MonzaSerializer(avto, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        data = request.data
        serializer = MonzaSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Matizview(APIView):
    def get(self, request: Request):
        avto = Matiz.objects.all()

        serializer = MatizSerializer(avto, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        data = request.data
        serializer = MatizSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Onixview(APIView):
    def get(self, request: Request):
        avto = Onix.objects.all()

        serializer = OnixSerializer(avto, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        data = request.data
        serializer = OnixSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Trackerview(APIView):
    def get(self, request: Request):
        avto = Tracker.objects.all()

        serializer = TrackerSerializer(avto, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        data = request.data
        serializer = TrackerSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








