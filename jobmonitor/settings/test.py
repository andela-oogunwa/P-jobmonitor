from base import *

DEBUG = True

TEMPLATE_DEBUG = True

SECRET_KEY = '^3q)6-fi&mq%8@)gym5i%3hxvxnaywl2=+(t53h_q#co($^h2u'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}