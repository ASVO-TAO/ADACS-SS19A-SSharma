"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

# from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
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
            job_key = form.instance.job_key
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
    job = get_object_or_404(JobParameter, job_key=job_key)
    return render(request, 'galaxiaweb/job/job_detail.html', {'job': job})
