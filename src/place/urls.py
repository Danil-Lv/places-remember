from django.urls import path

from .views import add_place, PlaceDetailView

urlpatterns = [
    path('add_place/', add_place, name='add_place'),
    path('<slug:slug>/', PlaceDetailView.as_view(), name='show_place'),

]
