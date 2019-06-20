"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django.shortcuts import render, redirect, get_object_or_404
from ..forms.job_parameter import JobParameterForm
from ..models import Job, JobParameter


def new_job(request):
    """
    Render the new_job view.
    :param request: Django request object.
    :return: Rendered template
    """

    if request.method == "POST":
        form = JobParameterForm(request.POST)
        if form.is_valid():
            job = Job.objects.create()
            form.instance.job = job
            form.save(commit=True)
            return render(
                request,
                "galaxiaweb/job/job_detail.html",
                {'job': form.instance}
            )
        else:
            return render(
                request,
                "galaxiaweb/job/new_job.html",
                {'job_parameter_form': form}
            )
    else:
        form = JobParameterForm()
        return render(
            request,
            "galaxiaweb/job/new_job.html",
            {'job_parameter_form': form}
        )


def job_detail(request, key):
    job = get_object_or_404(JobParameter, job_key=key)
    return render(request, 'galaxiaweb/job/job_detail.html', {'job': job})
