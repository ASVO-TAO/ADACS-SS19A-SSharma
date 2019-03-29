from django.contrib import admin

from .models import JobParameter
# Register your models here.


@admin.register(JobParameter)
class JobParameter(admin.ModelAdmin):
    list_display = ('model_file', 'apparent_magnitude_min', 'apparent_magnitude_max')
