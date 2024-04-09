from django.urls import path
from .views import TumanAPIView, MaktabAPIView, ShaxsAPIView

urlpatterns = [
    path('tumanlar/', TumanAPIView.as_view(), name='tumanlar-list'),
    path('tumanlar/<int:tuman_id>/maktablar/', MaktabAPIView.as_view(), name='maktablar-list'),
    path('shaxslar/', ShaxsAPIView.as_view(), name='shaxslar-list'),
]
