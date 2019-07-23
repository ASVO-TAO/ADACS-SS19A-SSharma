from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.exceptions import SoftTimeLimitExceeded

import os
import subprocess
import time

from django.conf import settings

from .constants import TASK_TIMEOUT, TASK_SUCCESS, TASK_FAIL, TASK_RUNNING

# register celery worker with Rabbitmq as message queue and rpc(rabbitmq) as backend to check results
# app = Celery('galaxiaweb.utils.tasks', backend='rpc://', broker='pyamqp://guest@localhost//')


def check_output_file_generated(outputfilepath):

    while not os.path.exists(outputfilepath):
        print('output file generated')
        return TASK_RUNNING
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
        process = subprocess.Popen(command)

        # Check output file is generated within 5 mins
        result = check_output_file_generated(outputfilepath)
    except SoftTimeLimitExceeded as timeout_err:
        print(timeout_err)
        result = TASK_TIMEOUT
        process.kill()
    except Exception as e:
        print(e)
        result = TASK_FAIL
        process.kill()
    finally:
        return result


# Use celery.task.apply_async(timeout) to wait for the task to run