from django.urls import path
from allauth.account import views as accountviews


from .views import AddPlaceView, PlaceDetailView, PlaceDeleteView

urlpatterns = [
    path('add_place/', AddPlaceView.as_view(), name='add_place'),
    path('delete/<slug:slug>/', PlaceDeleteView.as_view(), name='delete_place'),
    path('<slug:slug>/', PlaceDetailView.as_view(), name='show_place'),

]
