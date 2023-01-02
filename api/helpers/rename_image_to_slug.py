from operator import concat
import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible


@deconstructible
class RenameImageToSlug(object):

    def __init__(self, sub_path):
        self.path = 'images/' + sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        if hasattr(instance, 'slug'):
            filename = '{}.{}'.format(instance.slug, ext)
        else:
            filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(self.path, filename)
