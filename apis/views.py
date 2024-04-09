from rest_framework import generics
from .models import Tuman, Maktab,Shaxs
from .serializers import TumanSerializer, MaktabSerializer,ShaxsSerializer

class TumanAPIView(generics.ListAPIView):
    queryset = Tuman.objects.all()
    serializer_class = TumanSerializer

class MaktabAPIView(generics.ListCreateAPIView):
    serializer_class = MaktabSerializer

    def get_queryset(self):
        tuman_id = self.kwargs['tuman_id']
        return Maktab.objects.filter(tuman_id=tuman_id)

class ShaxsAPIView(generics.ListAPIView):
    queryset = Shaxs.objects.all()
    serializer_class = ShaxsSerializer
