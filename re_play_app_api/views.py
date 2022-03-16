from rest_framework import generics
from .serializers import ListingSerializer
from .models import Listing

class ListingList(generics.ListCreateAPIView):
    queryset = Listing.objects.all().order_by('id')
    serializer_class = ListingSerializer

class ListingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all().order_by('id')
    serializer_class = ListingSerializer
