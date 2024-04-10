from django.urls import path
from .views import TumanAPIView, MaktabAPIView, ShaxsAPIView

urlpatterns = [
    path('tuman/', TumanAPIView.as_view(), name='tuman-list'),
    path('tuman/<int:tuman_id>/maktab/', MaktabAPIView.as_view(), name='maktab-list'),
    path('tuman/<int:tuman_id>/maktab/<int:maktab_id>/shaxs/', ShaxsAPIView.as_view(), name='shaxs-list'),
]
