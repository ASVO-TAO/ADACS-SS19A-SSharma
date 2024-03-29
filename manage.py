#!/usr/bin/env python
import os
import sys
from os.path import join, dirname

from dotenv import load_dotenv

# load environment file before django settings
dotenv_path = join(dirname(__file__), 'env.env')
load_dotenv(dotenv_path)

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'galaxiaui.settings.production')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
