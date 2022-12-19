from rest_framework import serializers
from .models import Venue, Show

class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = '__all__'

class VenueSerializer(serializers.ModelSerializer):
    shows = ShowSerializer(
      many = True,
      read_only = True
    )
    class Meta:
        model = Venue
        fields = '__all__'