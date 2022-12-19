from django.shortcuts import render
from .models import Venue, Show
from .serializers import VenueSerializer, ShowSerializer
from rest_framework import viewsets

class ShowView(viewsets.ModelViewSet):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

class VenueView(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer