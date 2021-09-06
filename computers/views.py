from rest_framework import generics
from .serializers import ComputersSerializer
from .models import Computers
# Create your views here.


class ComputersList(generics.ListCreateAPIView):
    queryset = Computers.objects.all()
    serializer_class = ComputersSerializer


class ComputersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Computers.objects.all()
    serializer_class = ComputersSerializer
