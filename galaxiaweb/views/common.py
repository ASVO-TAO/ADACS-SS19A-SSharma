"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django.shortcuts import render


def index(request):
    """
    Render the index view.
    :param request: Django request object.
    :return: Rendered template
    """
    return render(
        request,
        "galaxiaweb/galaxia.html",
    )


def about(request):
    """
    Render the about view.
    :param request: Django request object.
    :return: Rendered template
    """
    return render(
        request,
        'galaxiaweb/about.html',
    )


def error_404_view(request):
    """
    Render custom 404 page.
    :param request: Django request object.
    :return: Rendered template
    """
    data = {"name": "not used yet"}
    return render(request, 'galaxiaweb/error_404.html', data)