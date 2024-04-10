from rest_framework import generics
from .models import Tuman, Maktab, Shaxs
from .serializers import TumanSerializer, MaktabSerializer, ShaxsSerializer

class TumanAPIView(generics.ListAPIView):
    queryset = Tuman.objects.all()
    serializer_class = TumanSerializer

class MaktabAPIView(generics.ListCreateAPIView):
    serializer_class = MaktabSerializer

    def get_queryset(self):
        tuman_id = self.kwargs['tuman_id']
        return Maktab.objects.filter(tuman_id=tuman_id)

class ShaxsAPIView(generics.ListCreateAPIView):
    serializer_class = ShaxsSerializer

    def get_queryset(self):
        tuman_id = self.kwargs['tuman_id']
        return Shaxs.objects.filter(tuman_id=tuman_id)

    def perform_create(self, serializer):
        tuman_id = self.kwargs['tuman_id']
        serializer.save(tuman_id=tuman_id)
