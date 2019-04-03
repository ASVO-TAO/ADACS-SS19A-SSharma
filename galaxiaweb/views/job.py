"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django.shortcuts import render
from ..forms.job_parameter import JobParameterForm


def new_job(request):
    """
    Render the new_job view.
    :param request: Django request object.
    :return: Rendered template
    """
    return render(
        request,
        "galaxiaweb/job/new_job.html",
        {'job_parameter_form': JobParameterForm()}
    )