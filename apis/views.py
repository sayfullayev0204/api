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
        maktab_id = self.kwargs['maktab_id']
        return Shaxs.objects.filter(maktab_id=maktab_id)

    def perform_create(self, serializer):
        maktab_id = self.kwargs['maktab_id']
        serializer.save(maktab_id=maktab_id)
