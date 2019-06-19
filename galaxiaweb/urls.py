"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
#from django.contrib.auth.decorators import login_required

from .views import common, job


urlpatterns = [
    path('', common.index, name='index'),
    path('new_job/', job.new_job, name='new_job'),
    path('job_detail/<str:job_key>/', job.job_detail, name='job_detail'),
    path('about/', common.about, name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



