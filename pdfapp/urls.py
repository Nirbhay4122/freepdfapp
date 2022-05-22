from socket import NI_NUMERICHOST
from django.urls import path
from .views import bhu, gate, index, jam, nimcet, aimcet, neet, jee

urlpatterns = [
    path('home', index),
    path('bhu', bhu),
    path('jam', jam),
    path('gate', gate),
    path('nimcet', nimcet),
    path('aimcet', aimcet),
    path('neet', neet),
    path('jee', jee),

]
