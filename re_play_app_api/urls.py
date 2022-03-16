from django.urls import path
from . import views

urlpatterns = [
    path('api/listings', views.ListingList.as_view(), name='listing_list'),
    path('api/listing/<int:pk>', views.ListingDetail.as_view(), name='listing_detail'),
]
