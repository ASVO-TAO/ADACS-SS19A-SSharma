from django.contrib import admin

from .models import JobParameter
# Register your models here.


@admin.register(JobParameter)
class JobParameter(admin.ModelAdmin):
    list_display = ('model_file', 'photo_sys_1', 'photo_sys_2', 'apparent_magnitude_min', 'apparent_magnitude_max',
                    'colour_limit_min', 'colour_limit_max', 'absolute_magnitude_min', 'absolute_magnitude_max',
                    'magnitude_name_1', 'magnitude_name_2', 'magnitude_name', 'geometry_options',
                    'longitude', 'latitude', 'survey_area', 'sample_fraction', 'population_ID', 'warp_flare',
                    'seed','r_max', )
