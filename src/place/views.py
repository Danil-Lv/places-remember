from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView, View

from .forms import PlaceForm
from .models import Place
from .utils import create_slug, BeAuthorRequiredMixin


class AddPlaceView(LoginRequiredMixin, View):
    login_url = reverse_lazy('main')

    def get(self, request):
        context = {
            'form': PlaceForm
        }
        return render(request, template_name='place/html/add_place.html', context=context)

    def post(self, request):
        form = PlaceForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.slug = create_slug(form.cleaned_data['title'])
            form.save()
            return redirect('profile')
        else:
            context = {
                'form': PlaceForm(request.POST)
            }
            return render(request, template_name='place/html/add_place.html', context=context)


class PlaceDetailView(
    LoginRequiredMixin,
    BeAuthorRequiredMixin,
    DetailView
):
    """Display of location"""
    model = Place
    template_name = 'place/html/place.html'
    login_url = reverse_lazy('main')


class PlaceDeleteView(
    LoginRequiredMixin,
    BeAuthorRequiredMixin,
    DeleteView
):
    """Deleting a place"""
    model = Place
    success_url = reverse_lazy('profile')
    login_url = reverse_lazy('main')

    def get_queryset(self):
        queryset = Place.objects.get(slug=self.kwargs['slug'])
        return super().get_queryset()
