from .base import *
import os
# import django_heroku
print('Production Environment')

# django_heroku.settings(locals())  # for connect to heroku postgresql

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = [os.environ['SECRET_KEY']]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Configure the domain name using the environment variable
# that Azure automatically creates for us.
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]

# MEDIA_ROOT = os.path.join(BASE_DIR, 'staticfiles','media_root')
# MEDIA_URL = '/media/'

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles', 'static_root')
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static') ]

# DBHOST is only the server name, not the full URL
# hostname = os.environ['DATABASE_URL'] if 'DATABASE_URL' in os.environ else []

# Configure Postgres database; the full username is username@servername,
# which we construct using the DBHOST value.
'''
DATABASES = {
    'default' : os.environ['DATABASE_URL'],
    'ENGINE': 'django.db.backends.postgresql',
}
'''
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=600)
print(db_from_env)
DATABASES = {}
DATABASES['default']=db_from_env

SECURE_HSTS_SECONDS=3600
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
SECURE_HSTS_PRELOAD=True
SECURE_CONTENT_TYPE_NOSNIFF=True
SECURE_BROWSER_XSS_FILTER=True
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
X_FRAME_OPTIONS='DENY'  # all block is 'DENY' Same origin is 'SAMEORIGIN'


