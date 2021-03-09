from django.urls import path
from .views import RealtorListView, RealtorView, TopSellerView

urlpatterns = [
    path('', RealtorListView.as_view(), name='RealtorListView'),
    path('topseller', TopSellerView.as_view(), name='TopSellerView'),
    path('<pk>', RealtorView.as_view(), name='RealtorView'),
]
