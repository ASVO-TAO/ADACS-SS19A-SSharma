from __future__ import absolute_import, unicode_literals
from celery import shared_task

import subprocess

# register celery worker with Rabbitmq as message queue and rpc(rabbitmq) as backend to check results
# app = Celery('galaxiaweb.utils.tasks', backend='rpc://', broker='pyamqp://guest@localhost//')


# @app.task(bind=True)
@shared_task
def run_galaxia(parameterfilepath):
    result = 'success'
    try:
        subprocess.call(['python', '/home/eman/PycharmProjects/generate-galaxia-output.py', parameterfilepath])

    except Exception as e:
        print(e)
        result = 'fail'
    finally:
        return result
    # '/home/eman/PycharmProjects/ADACS-SS19A-SSharma/files/parameter_files/27-Jun-2019_0638'

# Use celery.task.apply_async(timeout) to wait for the task to run