# settings/__init__.py

# from mysite.settings.base import *
import os

env_name = os.environ.get('ENV_NAME',default='local')

if env_name == 'prod':
    from mysite.settings.production import *
    print('import production env.')
elif env_name == 'local':
    from mysite.settings.local import *
    print('import local env.')