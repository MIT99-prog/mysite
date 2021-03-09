# settings/__init__.py

from .base import *

env_name = os.environ.get('ENV_NAME',default='local')

if env_name == 'prod':
    from .production import *
    print('import production env.')
elif env_name == 'local':
    from .local import *
    print('import local env.')