import os.path
import random
import string

from django.conf import settings

def random_filename_generator(size=16, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

def random_filename_upload(basedir):
        upload_transform_func(basedir)
        return upload_transform_func

def upload_transform_func(filename):
        fn, ext = os.path.splitext(filename)
        while True:
                newname = random_filename_generator() + ext
                path = os.path.join(filename, newname)
                if not os.path.isfile(os.path.join(settings.MEDIA_ROOT, path)):
                        break
        return path
