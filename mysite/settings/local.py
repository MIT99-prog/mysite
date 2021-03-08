from .base import *
import os
import environ
env = environ.Env()

# 環境変数でDJANGO_READ_ENV_FILEをTrueにしておくと.envを読んでくれる。
# よくわからないので外す。
'''
READ_ENV_FILE = env.bool('DJANGO_READ_ENV_FILE', default=False)
if READ_ENV_FILE:
    env_file = str(BASE_DIR.path('.env'))
    env.read_env(env_file)
'''
env.read_env('.env')

# env.read_env('.env')
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

# ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []
# ALLOWED_HOSTS = env('ALLOWED_HOSTS')
ALLOWED_HOSTS = ['localhost', '127.0.0.1','fast-stream-84593.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
        'default' : env.db()
    }


MEDIA_ROOT = os.path.join(BASE_DIR, 'static_collected','media_root')
MEDIA_URL = '/media/'

STATIC＿ROOT = os.path.join(BASE_DIR, 'static_collected', 'static_root')
STATIC_URL = '/static/'
from .base import *
import os
import environ
env = environ.Env()

# 環境変数でDJANGO_READ_ENV_FILEをTrueにしておくと.envを読んでくれる。
# よくわからないので外す。
'''
READ_ENV_FILE = env.bool('DJANGO_READ_ENV_FILE', default=False)
if READ_ENV_FILE:
    env_file = str(BASE_DIR.path('.env'))
    env.read_env(env_file)
'''
env.read_env('.env')

# env.read_env('.env')
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

# ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []
# ALLOWED_HOSTS = env('ALLOWED_HOSTS')
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'https://fast-stream-84593.herokuapp.com']

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