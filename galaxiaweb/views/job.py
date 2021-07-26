"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""
import os
import logging

# from django.http import HttpResponse
from django.urls import reverse
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from ..forms.job_parameter import JobParameterForm
from ..models import JobParameter
from ..utils.tasks import run_galaxia, send_notification_email
from ..utils.constants import TASK_SUCCESS, TASK_TIMEOUT, TASK_FAIL, TASK_FAIL_OTHER
from ..utils.send_emails import send_email, get_absolute_site_url

logger = logging.getLogger(__name__)

def new_job(request):
    """
    Render the new_job view.
    :param request: Django request object.
    :return: Rendered template
    """
    try:

        request.session.flush()
        if request.method == "POST":
            form = JobParameterForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                job_key = form.instance.job_key

                return redirect(reverse("job_detail", args=(job_key,)))
            else:
                messages.error(request, 'Please fix errors before proceeding')
                return render(
                    request,
                    "galaxiaweb/job/new_job.html",
                    {'job_parameter_form': form}
                )

        form = JobParameterForm()
        return render(
            request,
            "galaxiaweb/job/new_job.html",
            {'job_parameter_form': form}
        )

    except Exception as exp:
        logger.exception(f"Unexpected error: {exp}", exc_info=1)
        raise


def job_detail(request, job_key):
    """
    Render the job_details view
    :param request: Django request object
    :param job_key: job unique key
    :return: Rendered template
    """
    try:
        # get job from database using job_key
        job = get_object_or_404(JobParameter, job_key=job_key)

        # form parameter file path
        parameter_file_path = os.path.join(settings.MEDIA_ROOT, job.job_key, 'galaxia_param')
        output_file_url = None
        error_code = 0

        result = None
        # parameter and output file URL's as they appear in email notification
        url_parameter = get_absolute_site_url(request) + settings.MEDIA_URL + job.parameter_file_url
        url_output = get_absolute_site_url(request) + settings.MEDIA_URL + job_key + '/galaxia_output.ebf'

        # saves job information to session if it's not there yet
        # this runs when first loading job_detail view
        if job_key not in request.session:
            output_file_path = os.path.join(settings.MEDIA_ROOT, job.job_key, 'galaxia_output.ebf')
            # run galaxia as a Celery task
            task = run_galaxia.apply_async((parameter_file_path, output_file_path),
                                           link=send_notification_email.s(address=job.email,
                                                                          jobKey=job.job_key,
                                                                          parameterFileURL=url_parameter,
                                                                          outputFileURL=url_output))
            # save celery task id in session using job_key as the key
            request.session[job_key] = task.id

        # when page is reloaded, reload job_detail view without running the task again (same job)
        else:
            # retrieve task using task id saved in session
            task = run_galaxia.AsyncResult(request.session[job_key])
            # get task result
            result = task.get()
            # set output file url if the job succeeded, otherwise it will be None
            if result == TASK_SUCCESS:
                output_file_url = job.job_key + '/galaxia_output.ebf'
            # Updating error codes according to task state to display proper text in template
            elif result == TASK_TIMEOUT:
                error_code = 2

            elif result == TASK_FAIL:
                error_code = 1
            # example of another failure/error type
            elif result == TASK_FAIL_OTHER:
                error_code = 3

        return render(request, 'galaxiaweb/job/job_detail.html', {'job': job,
                                                                  'error_code': error_code,
                                                                  'output': output_file_url})
    except Exception as exp:
        logger.exception(f"Unexpected error: {exp}", exc_info=1)
        raise

def job_detail(request, job_key):
    """
    Render the job_details view
    :param request: Django request object
    :param job_key: job unique key
    :return: Rendered template
    """
    try:
        # get job from database using job_key
        job = get_object_or_404(JobParameter, job_key=job_key)

        # form parameter file path
        parameter_file_path = os.path.join(settings.MEDIA_ROOT, job.job_key, 'galaxia_param')
        output_file_url = None
        error_code = 0

        result = None
        # parameter and output file URL's as they appear in email notification
        url_parameter = get_absolute_site_url(request) + settings.MEDIA_URL + job.parameter_file_url
        url_output = get_absolute_site_url(request) + settings.MEDIA_URL + job_key + '/galaxia_output.ebf'

        # saves job information to session if it's not there yet
        # this runs when first loading job_detail view
        if job_key not in request.session:
            output_file_path = os.path.join(settings.MEDIA_ROOT, job.job_key, 'galaxia_output.ebf')
            # run galaxia as a Celery task
            task = run_galaxia.apply_async((parameter_file_path, output_file_path),
                                           link=send_notification_email.s(address=job.email,
                                                                          jobKey=job.job_key,
                                                                          parameterFileURL=url_parameter,
                                                                          outputFileURL=url_output))
            # save celery task id in session using job_key as the key
            request.session[job_key] = task.id

        # when page is reloaded, reload job_detail view without running the task again (same job)
        else:
            # retrieve task using task id saved in session
            task = run_galaxia.AsyncResult(request.session[job_key])
            # get task result
            result = task.get()
            # set output file url if the job succeeded, otherwise it will be None
            if result == TASK_SUCCESS:
                output_file_url = job.job_key + '/galaxia_output.ebf'
            # Updating error codes according to task state to display proper text in template
            elif result == TASK_TIMEOUT:
                error_code = 2

            elif result == TASK_FAIL:
                error_code = 1
            # example of another failure/error type
            elif result == TASK_FAIL_OTHER:
                error_code = 3

        return render(request, 'galaxiaweb/job/job_detail.html', {'job': job,
                                                                  'error_code': error_code,
                                                                  'output': output_file_url})
    except Exception as exp:
        logger.exception(f"Unexpected error: {exp}", exc_info=1)
        raise
