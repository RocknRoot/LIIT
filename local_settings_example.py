DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': '',
    'USER': '',
    'PASSWORD': '',
    'HOST': '',
  }
}

TIME_ZONE = 'Europe/Paris'
LANGUAGE_CODE = 'en-us'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'DO-SOMETHING-FOR-FUCKS-SAKE'

STATICFILES_DIRS = (
)

TEMPLATE_DIRS = (
)
