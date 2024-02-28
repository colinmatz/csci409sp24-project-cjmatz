from django.shortcuts import render
from rest_framework import viewsets
from .models import Vessel, VesselSchedule, BillOfLading, Container
from .serializers import VesselSerializer, VesselScheduleSerializer, BillOfLadingSerializer, containerSerializer

# Create your views here.

class VesselViewSet(viewsets.ModelViewSet):
    queryset = Vessel.objects.all()
    serializer_class = VesselSerializer

class VesselScheduleViewSet(viewsets.ModelViewSet):
    queryset = VesselSchedule.objects.all()
    serializer_class = VesselScheduleSerializer

class BillOfLadingViewSet(viewsets.ModelViewSet):
    queryset = BillOfLading.objects.all()
    serializer_class = BillOfLadingSerializer

class ContainerViewSet(viewsets.ModelViewSet):
    queryset = Container.objects.all()
    serializer_class = containerSerializer
