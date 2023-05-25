from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('src.user.urls')),
    path('admin/', admin.site.urls),
    path('place/', include('src.place.urls')),
    path('accounts/', include('allauth.urls')),


]
