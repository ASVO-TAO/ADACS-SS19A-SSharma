from __future__ import absolute_import, unicode_literals
import os

import logging

from celery import Celery


logger = logging.getLogger(__name__)

# set the default Django settings module for the Celery. This is where Celery configuration resides
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'galaxiaui.settings.development')

app = Celery('galaxiaui')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# Retrieve task timout limits from environment file
app.conf.update(
    task_soft_time_limit=os.environ['CELERY_TASK_SOFT_TIME_LIMIT'],
    task_time_limit=os.environ['CELERY_TASK_TIME_LIMIT'],
)


@app.task(bind=True)
def debug_task(self):
    logger.debug('Request: {0!r}'.format(self.request))
