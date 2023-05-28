from django.urls import path

from .views import index
from ..place.views import PlacesListView

urlpatterns = [
    path('', index, name='main'),
    path('profile/', PlacesListView.as_view(), name='profile'),

]

