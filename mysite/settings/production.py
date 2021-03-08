from .base import *
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = [os.environ['SECRET_KEY']]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Configure the domain name using the environment variable
# that Azure automatically creates for us.
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]

MEDIA_ROOT = os.path.join(BASE_DIR, 'static_collected','media_root')
MEDIA_URL = '/media/'

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_ROOT = os.path.join(BASE_DIR, 'static_collected', 'static_root')
STATIC_URL = '/static/'
STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static') ]

# DBHOST is only the server name, not the full URL
# hostname = os.environ['DATABASE_URL'] if 'DATABASE_URL' in os.environ else []

# Configure Postgres database; the full username is username@servername,
# which we construct using the DBHOST value.
DATABASES = {
    'default' : os.environ['DATABASE_URL'] 
}
