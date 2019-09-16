from __future__ import absolute_import, unicode_literals
from celery import shared_task, Task
from celery.exceptions import SoftTimeLimitExceeded, TaskRevokedError

import os
import glob
import subprocess

from django.conf import settings

from .constants import TASK_TIMEOUT, TASK_SUCCESS, TASK_FAIL , TASK_FAIL_OTHER
from .send_emails import send_email


def cleanup_timeout_task(outputfilepath):
    """
    Cleans up temp files in case the job didn't end successfully
    :param outputfilepath: path where outfile exists
    :return:
    """
    try:
        # get output directory name
        dirname = os.path.dirname(outputfilepath)
        print(f'Cleaning up {dirname}')
        # get list of temp files in the output directory
        tmpfiles = glob.glob(os.path.join(dirname, '*galaxia_*ebf.tmp*'))
        # delete files
        for f in tmpfiles:
            if os.path.isfile(f):
                os.remove(f)
    except Exception as e:
        print(e)


def check_output_file_generated(outputfilepath):
    """
    Check if the job finished successfully by checking that output file is created
    This will keep running until file is created or timeout otherwise
    :param outputfilepath: full path of output file
    :return:
    """
    created = False
    # keep checking until output file is generated
    while not created:
        created = os.path.exists(outputfilepath)
    return TASK_SUCCESS


@shared_task
def run_galaxia(parameterfilepath, outputfilepath):
    """
    Celery task to launch galaxia job as a system call
    :param parameterfilepath: full path to parameter file
    :param outputfilepath: full path of output file to be generated
    :return: TASK_SUCCESS if job finished successfully
            OR TASK_TIMEOUT if job exceeded preset timeout limit
    """
    result = None
    try:
        # Grabbing galaxia run command from settings (as a list)
        command = settings.RUN_GALAXIA_COMMAND
        # Adding the parameter file path as a command argument
        command.append(parameterfilepath)
        # run galaxia a system call
        subprocess.call(command)
        # Check output file is generated within preset Celery soft timeout limit
        result = check_output_file_generated(outputfilepath)

    except SoftTimeLimitExceeded as timeout_err:
        # If job timed out, clean up output directory
        cleanup_timeout_task(outputfilepath)
        print(timeout_err)
        result = TASK_TIMEOUT

    except Exception as e:
        # return fail code if galaxia job failed for someother reason
        print(e)
        result = TASK_FAIL
    # An example of adding in another error (would need to go above Exception above)
    except TaskRevokedError as revoked_err:
        print(revoked_err)
        result = TASK_FAIL_OTHER
    finally:
        return result


@shared_task
def send_notification_email(jobstate, address=None, jobKey=None, parameterFileURL=None, outputFileURL=None):
    """
    Celery task to send notification email based on task state. This task runs automatically after run_galaxia task ends
    :param jobstate: preset by run_galaxia task
    :param address: email address to send email to
    :param jobKey: job key
    :param parameterFileURL: parameter file URL to appear in the email
    :param outputFileURL: output file URL to appear in the email
    :return:
    """
    print(f'Run Galaxia: {jobstate}')
    # send email only if address was submitted
    if address:
        send_email([address], jobKey, parameterFileURL, outputFileURL, jobstate)
    else:
        print('No email provided')
