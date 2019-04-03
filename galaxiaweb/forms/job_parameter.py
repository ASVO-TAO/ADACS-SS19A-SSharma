from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import JobParameter

FIELDS = [
    'model_file',
    'photo_sys_1',
    'photo_sys_2',
    'apparent_magnitude_min',
    'apparent_magnitude_max',
    'absolute_magnitude_min',
    'absolute_magnitude_max',
    'colour_limit_min',
    'colour_limit_max',
]

LABELS = {
    'model_file': _('Model File'),
    'photo_sys_1': _('PhotoSys 1'),
    'photo_sys_2': _('PotoSys 2'),
    'apparent_magnitude_min': _('Minimum Apparent Magnitude'),
    'apparent_magnitude_max': _('Maximum Apparent Magnitude'),
    'absolute_magnitude_min': _('Minimum Absolute Magnitude'),
    'absolute_magnitude_max': _('Maximum Absolute Magnitude'),
}

class JobParameterForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super(JobParameterForm, self).__init__(*args, **kwargs)

    class Meta:
        model = JobParameter
        fields = FIELDS
        labels = LABELS
