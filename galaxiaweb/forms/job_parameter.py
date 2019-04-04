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
    'magnitude_name_1',
    'magnitude_name_2',
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
    'magnitude_name_1': _('Blue band for colour selection'),
    'magnitude_name_2': _('Red band for colour selection'),
    'colour_limit_min': _('Minimum Colour'),
    'colour_limit_max': _('Maximum Colour'),
}

class JobParameterForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super(JobParameterForm, self).__init__(*args, **kwargs)

    class Meta:
        model = JobParameter
        fields = FIELDS
        labels = LABELS
