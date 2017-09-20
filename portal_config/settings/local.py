from portal_config.settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='8#$2x^j8q6(na26f0#5tfad=3&#7a%!!2^mkmqxu9$-p=n*!)9')

DEBUG = env.bool('DJANGO_DEBUG', default=True)