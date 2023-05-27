from django.urls import path

from allauth.account.views import logout
from allauth.socialaccount.providers.google.views import oauth2_login as google_login, \
    oauth2_callback as google_callback
from allauth.socialaccount.providers.vk.views import oauth2_login as vk_login, oauth2_callback as vk_callback

urlpatterns = [
    path('logout/', logout, name="account_logout"),
    path(r'vk/login/', vk_login, name="vk_login"),
    path(r'vk/login/callback/', vk_callback, name="vk_callback"),
    path(r'google/login/', google_login, name="google_login"),
    path(r'google/login/callback/', google_callback, name="google_callback"),
]
