from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import JobParameter

FIELDS = [
    'model_file',
    'photo_sys_1',
    'photo_sys_2',
    'magnitude_name',
    'apparent_magnitude_min',
    'apparent_magnitude_max',
    'absolute_magnitude_min',
    'absolute_magnitude_max',
    'magnitude_name_1',
    'magnitude_name_2',
    'colour_limit_min',
    'colour_limit_max',
    'geometry_options',
    'longitude',
    'latitude',
    'survey_area',
    'sample_fraction',
    'population_ID',
    'warp_flare',
    'seed',
    'r_max',
]

LABELS = {
    'model_file': _('Model File'),
    'photo_sys_1': _('PhotoSys 1'),
    'photo_sys_2': _('PotoSys 2'),
    'magnitude_name': _('Photometric selection band'),
    'apparent_magnitude_min': _('Minimum Apparent Magnitude'),
    'apparent_magnitude_max': _('Maximum Apparent Magnitude'),
    'absolute_magnitude_min': _('Minimum Absolute Magnitude'),
    'absolute_magnitude_max': _('Maximum Absolute Magnitude'),
    'magnitude_name_1': _('Blue band for colour selection'),
    'magnitude_name_2': _('Red band for colour selection'),
    'colour_limit_min': _('Minimum Colour'),
    'colour_limit_max': _('Maximum Colour'),
    'geometry_options': _('Survey Geometry'),
    'longitude': _('Longitude [degrees]'),
    'latitude': _('Latitude [degrees]'),
    'survey_area': _('Survey Area [squared degrees]'),
    'sample_fraction': _('Stellar Sampling Fraction'),
    'population_ID': _('Population to generate'),
    'warp_flare': _('Thin disk warp and flare'),
    'seed': _('Random seed'),
    'r_max': _('Maximum radial distance [kpc]'),
}

WIDGETS = {
    'model_file': forms.Select(attrs={'class': 'form-control'}),
    'photo_sys_1': forms.Select(attrs={'class': 'form-control'}),
    'photo_sys_2': forms.Select(attrs={'class': 'form-control'}),
    'magnitude_name': forms.Select(attrs={'class': 'form-control'}),
    'apparent_magnitude_min': forms.NumberInput(attrs={'class': 'form-control'}),
    'apparent_magnitude_max': forms.NumberInput(attrs={'class': 'form-control'}),
    'absolute_magnitude_min': forms.NumberInput(attrs={'class': 'form-control'}),
    'absolute_magnitude_max': forms.NumberInput(attrs={'class': 'form-control'}),
    'magnitude_name_1': forms.Select(attrs={'class': 'form-control'}),
    'magnitude_name_2': forms.Select(attrs={'class': 'form-control'}),
    'colour_limit_min': forms.NumberInput(attrs={'class': 'form-control'}),
    'colour_limit_max': forms.NumberInput(attrs={'class': 'form-control'}),
    'geometry_options': forms.Select(attrs={'class': 'form-control'}),
    'longitude': forms.NumberInput(attrs={'class': 'form-control'}),
    'latitude': forms.NumberInput(attrs={'class': 'form-control'}),
    'survey_area': forms.NumberInput(attrs={'class': 'form-control'}),
    'sample_fraction': forms.NumberInput(attrs={'class': 'form-control'}),
    'population_ID': forms.Select(attrs={'class': 'form-control'}),
    'warp_flare': forms.CheckboxInput(attrs={'class': 'form-check-input ml-2 mt-2'}),
    'seed': forms.NumberInput(attrs={'class': 'form-control'}),
    'r_max': forms.NumberInput(attrs={'class': 'form-control'}),

}


class JobParameterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(JobParameterForm, self).__init__(*args, **kwargs)

    class Meta:
        model = JobParameter
        fields = FIELDS
        labels = LABELS
        widgets = WIDGETS
