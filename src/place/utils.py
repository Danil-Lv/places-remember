from datetime import datetime

from slugify import slugify


def make_slug(text):
    return f'{slugify(text)}-{str(int(datetime.timestamp(datetime.today())))}'
