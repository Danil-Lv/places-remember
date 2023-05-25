from django.shortcuts import render, redirect
from django.views.generic import DetailView

from .forms import PlaceForm
from .models import Place
from .utils import make_slug


def add_place(requests):
    if requests.method == 'GET':
        context = {
            'form': PlaceForm
        }
        return render(requests, template_name='place/html/add_place.html', context=context)

    elif requests.method == 'POST':
        form = PlaceForm(requests.POST)
        if form.is_valid():
            new_place = form.save(commit=False)
            new_place.user = requests.user
            new_place.slug = make_slug(new_place.title)
            new_place.save()
            return redirect('profile')


class PlaceDetailView(DetailView):
    model = Place
    template_name = 'place/html/place.html'
