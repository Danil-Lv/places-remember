from datetime import datetime

from django.shortcuts import redirect
from slugify import slugify


def create_slug(text):
    return f'{slugify(text)}-{str(int(datetime.timestamp(datetime.today())))}'


class AuthorPermissionMixin:
    def has_permissions(self):
        return self.get_object().user == self.request.user

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            return redirect('profile')
        return super().dispatch(request, *args, **kwargs)
