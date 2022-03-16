from django.urls import path
from . import views

urlpatterns = [
    path('api/DATABASE', views.ListingList.as_view(), name='listing_list'),
    path('api/DATABASE/<int:pk>', views.ListingDetail.as_view(), name='listing_detail'),
]
