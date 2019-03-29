from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import JobParameter

FIELDS = [
    'model_file',
    'photo_sys_1',
    'apparent_magnitude_min',
    'apparent_magnitude_max',
]

LABELS = {
    'model_file': _('Model File'),
    'photo_sys_1': _('PhotoSys 1'),
    'apparent_magnitude_min': _('Minimum Apparent Magnitude'),
    'apparent_magnitude_max': _('Maximum Apparent Magnitude'),

}

class JobParameterForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super(JobParameterForm, self).__init__(*args, **kwargs)

    class Meta:
        model = JobParameter
        fields = FIELDS
        labels = LABELS
