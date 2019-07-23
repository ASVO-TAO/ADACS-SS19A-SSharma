"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""
import os

from django.urls import reverse
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from ..forms.job_parameter import JobParameterForm
from ..models import JobParameter
from ..utils.tasks import run_galaxia, send_success_notification_email, send_timeout_notification_email
from ..utils.constants import TASK_SUCCESS, TASK_TIMEOUT
from ..utils.send_emails import send_email, get_absolute_site_url

def new_job(request):
    """
    Render the new_job view.
    :param request: Django request object.
    :return: Rendered template
    """
    request.session.flush()
    if request.method == "POST":
        form = JobParameterForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            job_key = form.instance.job_key
            url_parameter = get_absolute_site_url(request) + settings.MEDIA_URL + form.instance.parameter_file_url
            url_output = get_absolute_site_url(request) + settings.MEDIA_URL + job_key + '/galaxia_' + job_key
            send_email([form.instance.email], job_key, url_parameter,url_output)

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


def job_detail(request, job_key):

    job = get_object_or_404(JobParameter, job_key=job_key)

    parameter_file_path = os.path.join(settings.MEDIA_ROOT, job.job_key, job.job_key)
    output_file_url = None
    timeout = False

    if job_key not in request.session:
        output_file_path = os.path.join(settings.MEDIA_ROOT, job.job_key, f'galaxia_{job.job_key}.ebf')
        task = run_galaxia.delay(parameter_file_path, output_file_path)
        request.session[job_key] = task.id
    else:
        task = run_galaxia.AsyncResult(request.session[job_key])
        result = task.get()

        if result == TASK_SUCCESS:
            output_file_url = job.job_key + f'/galaxia_{job.job_key}'
            if job.email:
                send_success_notification_email.delay(job.email)

        elif result == TASK_TIMEOUT:
            timeout = True
            if job.email:
                send_timeout_notification_email.delay(job.email)

    return render(request, 'galaxiaweb/job/job_detail.html', {'job': job,
                                                              'timeout': timeout,
                                                              'output': output_file_url})
