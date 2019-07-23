from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.exceptions import SoftTimeLimitExceeded

import os
import subprocess

from django.conf import settings

from .constants import TASK_TIMEOUT, TASK_SUCCESS, TASK_FAIL, TASK_RUNNING

# register celery worker with Rabbitmq as message queue and rpc(rabbitmq) as backend to check results
# app = Celery('galaxiaweb.utils.tasks', backend='rpc://', broker='pyamqp://guest@localhost//')


def check_output_file_generated(outputfilepath):

    created = False
    while not created:
        created = os.path.exists(outputfilepath)
    print('output file generated')
    return TASK_SUCCESS


@shared_task
def run_galaxia(parameterfilepath, outputfilepath):

    result = None
    try:
        # Grabbing galaxia run command from settings (as a list)
        command = settings.RUN_GALAXIA_COMMAND
        # Adding the parameter file path as a command argument
        command.append(parameterfilepath)
        # run galaxia on a separate thread
        subprocess.call(command)
        # Check output file is generated within 5 mins
        result = check_output_file_generated(outputfilepath)

    except SoftTimeLimitExceeded as timeout_err:
        print(timeout_err)
        result = TASK_TIMEOUT
    except Exception as e:
        print(e)
        result = TASK_FAIL
    finally:
        return result


@shared_task
def send_success_notification_email(address=None):
    if address:
        print(f'Success Email sent to: {address}')
    else:
        print('No email provided')


@shared_task
def send_timeout_notification_email(address=None):
    if address:
        print(f'Timeout Email sent to: {address}')
    else:
        print('No email provided')