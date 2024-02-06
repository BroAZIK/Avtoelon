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
        

    def put(self, request: Request, pk: int, mk: str) -> Response:
        data = request.data
        task = index.objects.get(user_id=pk)
        index_instance = index.objects.get(user_id=pk)
        serializer = IndexSerializer(task, data=data)
        try:
            if mk == "index_Labo":
                index_instance.index_Labo = data.get(f'{mk}', index_instance.index_Labo)
                index_instance.stage = data.get('stage', index_instance.stage)
                index_instance.save()
                return Response({'message': 'Ma\'lumot muvaffaqiyatli o\'zgartirildi.'}, status=200)
            if mk == "index_Damas":
                index_instance.index_Damas = data.get(f'{mk}', index_instance.index_Damas)
                index_instance.stage = data.get('stage', index_instance.stage)
                index_instance.save()
                return Response({'message': 'Ma\'lumot muvaffaqiyatli o\'zgartirildi.'}, status=200)
            if mk == "index_Spark":
                index_instance.index_Spark = data.get(f'{mk}', index_instance.index_Spark)
                index_instance.stage = data.get('stage', index_instance.stage)
                index_instance.save()
                return Response({'message': 'Ma\'lumot muvaffaqiyatli o\'zgartirildi.'}, status=200)
            if mk == "index_Nexia":
                index_instance.index_Nexia = data.get(f'{mk}', index_instance.index_Nexia)
                index_instance.stage = data.get('stage', index_instance.stage)
                index_instance.save()
                return Response({'message': 'Ma\'lumot muvaffaqiyatli o\'zgartirildi.'}, status=200)
            if mk == "index_Cobalt":
                index_instance.index_Cobalt = data.get(f'{mk}', index_instance.index_Cobalt)
                index_instance.stage = data.get('stage', index_instance.stage)
                index_instance.save()
                return Response({'message': 'Ma\'lumot muvaffaqiyatli o\'zgartirildi.'}, status=200)
            if mk == "index_Gentra":
                index_instance.index_Gentra = data.get(f'{mk}', index_instance.index_Gentra)
                index_instance.stage = data.get('stage', index_instance.stage)
                index_instance.save()
                return Response({'message': 'Ma\'lumot muvaffaqiyatli o\'zgartirildi.'}, status=200)
            if mk == "index_Matiz":
                index_instance.index_Matiz = data.get(f'{mk}', index_instance.index_Matiz)
                index_instance.stage = data.get('stage', index_instance.stage)
                index_instance.save()
                return Response({'message': 'Ma\'lumot muvaffaqiyatli o\'zgartirildi.'}, status=200)
            if mk == "index_Lacetti":
                index_instance.index_Lacetti = data.get(f'{mk}', index_instance.index_Lacetti)
                index_instance.stage = data.get('stage', index_instance.stage)
                index_instance.save()
                return Response({'message': 'Ma\'lumot muvaffaqiyatli o\'zgartirildi.'}, status=200)
            if mk == "index_Onix":
                index_instance.index_Onix = data.get(f'{mk}', index_instance.index_Onix)
                index_instance.stage = data.get('stage', index_instance.stage)
                index_instance.save()
                return Response({'message': 'Ma\'lumot muvaffaqiyatli o\'zgartirildi.'}, status=200)
            if mk == "index_Monza":
                index_instance.index_Monza = data.get(f'{mk}', index_instance.index_Monza)
                index_instance.stage = data.get('stage', index_instance.stage)
                index_instance.save()
                return Response({'message': 'Ma\'lumot muvaffaqiyatli o\'zgartirildi.'}, status=200)
            if mk == "index_Equinox":
                index_instance.index_Equinox = data.get(f'{mk}', index_instance.index_Equinox)
                index_instance.stage = data.get('stage', index_instance.stage)
                index_instance.save()
                return Response({'message': 'Ma\'lumot muvaffaqiyatli o\'zgartirildi.'}, status=200)
            if mk == "index_Tracker":
                index_instance.index_Tracker = data.get(f'{mk}', index_instance.index_Tracker)
                index_instance.stage = data.get('stage', index_instance.stage)
                index_instance.save()
                return Response({'message': 'Ma\'lumot muvaffaqiyatli o\'zgartirildi.'}, status=200)
            if mk == "index_Malibu1":
                index_instance.index_Malibu = data.get(f'{mk}', index_instance.index_Malibu)
                index_instance.stage = data.get('stage', index_instance.stage)
                index_instance.save()
                return Response({'message': 'Ma\'lumot muvaffaqiyatli o\'zgartirildi.'}, status=200)
            if mk == "index_Malibu2":
                index_instance.index_Malibu2 = data.get(f'{mk}', index_instance.index_Malibu2)
                index_instance.stage = data.get('stage', index_instance.stage)
                index_instance.save()
                return Response({'message': 'Ma\'lumot muvaffaqiyatli o\'zgartirildi.'}, status=200)

            else:
                index_instance.stage = data.get('stage', index_instance.stage)
                index_instance.save()
                return Response({'message': 'Ma\'lumot muvaffaqiyatli o\'zgartirildi.'}, status=200)

        except index.DoesNotExist:
            return Response({'error': 'Bunday user_id li ma\'lumot topilmadi.'}, status=404)

        except Exception as e:
            return Response({'error': str(e)}, status=400)   

    def delete(self, request: Request, pk: int) -> Response:
        index.objects.get(user_id=pk).delete()

        return Response({'message': 'deleted.'}, status=status.HTTP_200_OK)