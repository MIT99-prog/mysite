from .base import *
import os
import environ
print('Local Environment')
env = environ.Env()

# 環境変数でDJANGO_READ_ENV_FILEをTrueにしておくと.envを読んでくれる。
# READ_ENV_FILE = env.bool('DJANGO_READ_ENV_FILE', default=False)
# READ_ENV_FILE = env.bool('DJANGO_READ_ENV_FILE')
READ_ENV_FILE = os.getenv('DJANGO_READ_ENV_FILE')
if READ_ENV_FILE:
    env_file = os.path.join(BASE_DIR,'.env')
    env.read_env(env_file)
else:
    print('Cannot read env values DJANGO_READ_ENV_FILE= ', str(READ_ENV_FILE))


# env.read_env('.env')
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []
# ALLOWED_HOSTS = env('ALLOWED_HOSTS')
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'cryptic-lowlands-93359.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
        'default' : env.db()
    }


MEDIA_ROOT = os.path.join(BASE_DIR, 'static_collected','media_root')
MEDIA_URL = '/media/'

STATIC＿ROOT = os.path.join(BASE_DIR, 'static_collected', 'static_root')
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
'''
SECURE_HSTS_SECONDS=0
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
SECURE_HSTS_PRELOAD=True
SECURE_CONTENT_TYPE_NOSNIFF=True
SECURE_BROWSER_XSS_FILTER=True
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
X_FRAME_OPTIONS='DENY'
'''
