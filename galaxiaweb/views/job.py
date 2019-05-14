"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django.shortcuts import render, redirect
from ..forms.job_parameter import JobParameterForm
from ..models import Job


def new_job(request):
    """
    Render the new_job view.
    :param request: Django request object.
    :return: Rendered template
    """

    if request.method == "POST":
        form = JobParameterForm(request.POST)
        if form.is_valid():
            # form.save(commit=False)
            job = Job.objects.create()
            print('job_id = ' + str(job))
            form.instance.job = job
            form.save(commit=True)
    else:
        form = JobParameterForm()

    return render(
        request,
        "galaxiaweb/job/new_job.html",
        {'job_parameter_form': form}
    )

