from __future__ import absolute_import, unicode_literals
from celery import shared_task, Task
from celery.exceptions import SoftTimeLimitExceeded
from celery.worker.request import Request

import os
import glob
import subprocess

from django.conf import settings

from .constants import TASK_TIMEOUT, TASK_SUCCESS, TASK_FAIL
from .send_emails import send_email


def cleanup_timeout_task(outputfilepath):

    try:
        dirname = os.path.dirname(outputfilepath)
        print(f'Cleaning up {dirname}')
        tmpfiles = glob.glob(os.path.join(dirname, '*galaxia_*ebf.tmp*'))
        for f in tmpfiles:
            if os.path.isfile(f):
                os.remove(f)
    except Exception as e:
        print(e)


def check_output_file_generated(outputfilepath):

    created = False
    while not created:
        created = os.path.exists(outputfilepath)
    # print('output file generated')
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
        cleanup_timeout_task(outputfilepath)
        print(timeout_err)
        result = TASK_TIMEOUT
    except Exception as e:
        print(e)
        result = TASK_FAIL
    finally:
        return result


@shared_task
def send_notification_email(jobstate, address=None, jobKey=None, parameterFileURL=None, outputFileURL=None):
    print(f'Run Galaxia: {jobstate}')
    if address:
        send_email([address], jobKey, parameterFileURL, outputFileURL, jobstate)
    else:
        print('No email provided')
