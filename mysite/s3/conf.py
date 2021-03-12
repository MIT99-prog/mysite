# aws/conf.py

from pathlib import Path
import os
import environ

DEFAULT_FILE_STORAGE = 'mysite.s3.utils.MediaRootS3BotoStorage'
# <project-name> = Django プロジェクト名
STATICFILES_STORAGE = 'mysite.s3.utils.StaticRootS3BotoStorage'
# <project-name> = Django プロジェクト名

# get AWS_ACCESS_KEY and AWS_SECRET_ACCESS_KEY
if os.environ.get('ENV_NAME') == 'local':
    env = environ.Env()
    READ_ENV_FILE = os.getenv('DJANGO_READ_ENV_FILE')
    if READ_ENV_FILE:
        env_file = os.path.join(Path(__file__).resolve().parent.parent.parent,'.env')
        env.read_env(env_file)
        AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')  # 環境変数を指定（ローカル）
        AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')  # 環境変数を指定（ローカル）
    else:
        print('Cannot read env values DJANGO_READ_ENV_FILE= ', str(READ_ENV_FILE))
    
else:
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')  # 環境変数を指定
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')  # 環境変数を指定
print('got AWS_ACCESS_KEY!')

AWS_STORAGE_BUCKET_NAME = 'mydatabucket001'  # Amazon S3 のバケット名
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',  # キャッシュの有効期限（最長期間）= 1日
}
AWS_QUERYSTRING_AUTH = False  # URLからクエリパラメータを削除

AWS_S3_URL = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = 'https://%s/%s/' % (AWS_S3_URL, 'media')
STATIC_URL = 'https://%s/%s/' % (AWS_S3_URL, 'static')
print('MEDIA_URL = ',MEDIA_URL)
print('STATIC_URL = ',STATIC_URL)