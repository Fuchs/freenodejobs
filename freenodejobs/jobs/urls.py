from django.urls import path, re_path, include

from . import feeds, views
from .enums import JobTypeEnum

app_name = 'jobs'

urlpatterns = [
    path('', include('freenodejobs.jobs.jobs_add_edit.urls',
         namespace='add-edit')),

    path('all-jobs', views.view,
         name='view'),
    path('full-time-jobs', views.view,
         {'job_type': JobTypeEnum.FULL_TIME}, name='full-time'),
    path('part-time-jobs', views.view,
         {'job_type': JobTypeEnum.PART_TIME}, name='part-time'),
    path('contract-jobs', views.view,
         {'job_type': JobTypeEnum.CONTRACT}, name='contract'),
    path('volunteer-jobs', views.view,
         {'job_type': JobTypeEnum.VOLUNTEER}, name='volunteer'),

    re_path(r'^job/(?P<prefix>[-a-zA-Z0-9_]+)-(?P<slug>[a-z]{8})$', views.job,
            name='view'),
    re_path(r'^job/(?P<slug>[a-z]{8})$', views.job,
            name='view'),

    path('feed', feeds.AllJobs(),
         name='feed'),
]
