from django.urls import path
from .views import TumanAPIView, MaktabAPIView, ShaxsAPIView

urlpatterns = [
    path('tuman/', TumanAPIView.as_view(), name='tumanlar'),
    path('tuman/<int:tuman_id>/maktab/', MaktabAPIView.as_view(), name='maktablar'),
    path('tuman/<int:tuman_id>/shaxs/', ShaxsAPIView.as_view(), name='shaxslar'),
]
