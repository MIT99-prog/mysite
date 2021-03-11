#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    # syspath control
    # sys.path.append('F:\Django\mysite')
    # sys.path.append('F:\Django\mysite\mysite\\aws')
    # print('Syspath = ',sys.path)

    """Run administrative tasks."""
    if os.environ.get('ENV_NAME') == 'prod':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', "mysite.settings.production")
        print('setdefault production.py')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', "mysite.settings.local")
        print('setdefault local.py')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
