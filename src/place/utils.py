from datetime import datetime

from slugify import slugify


def create_slug(text):
    return f'{slugify(text)}-{str(int(datetime.timestamp(datetime.today())))}'


class BeAuthorRequiredMixin:

    def is_author(self, request, *args, **kwargs):
        a = 1
        b = 2
