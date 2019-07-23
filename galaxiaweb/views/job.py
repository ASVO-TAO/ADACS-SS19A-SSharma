"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""
import os

# from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from ..forms.job_parameter import JobParameterForm
from ..models import JobParameter
from ..utils.tasks import run_galaxia
from ..utils.send_emails import send_email


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
            send_email([form.instance.email], job_key, form.instance.parameter_file_url)
            # return HttpResponseRedirect(reverse('job_detail', args=(job_key,)))
            return redirect(reverse("job_detail", args=(job_key,)))
        else:
            # messages.add_message(request, messages.ERROR, 'Please fix errors before proceeding')
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

    if 'job_key' not in request.session:
        request.session['job_key'] = job_key
        request.session['fired'] = False

    job = get_object_or_404(JobParameter, job_key=job_key)
    parameter_file_path = os.path.join(settings.MEDIA_ROOT, job.job_key, job.job_key)
    output_file_path = os.path.join(settings.MEDIA_ROOT, job.job_key, f'galaxia_{job.job_key}')

    #try:
    #    print(request.session['job_key'])
    #    print(request.session['fired'])
    #except:
    #    pass

    if request.session['job_key'] == job_key and not request.session['fired']:
        #result = run_galaxia.delay(parameter_file_path)
        request.session['fired'] = True
        #print('job fired')

    output = None

    if os.path.exists(output_file_path):
        output = job.job_key + f'/galaxia_{job.job_key}'

    return render(request, 'galaxiaweb/job/job_detail.html', {'job': job, 'output': output})
