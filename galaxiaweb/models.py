from django.db import models

from .utils.constants import *

# Create your models here.


class JobParameter(models.Model):
    MODEL_FILE_CHOICES = [
        (SHARMA_2011, SHARMA_2011),
        (SHARMA_2019, SHARMA_2019),
    ]

    PHOTO_SYS_1_CHOICES = [
        (PARSEC_1, PARSEC_1),
    ]

    PHOTO_SYS_2_CHOICES = [
        (GAIADR2_TMASS,GAIADR2_TMASS),
        (WISE,WISE),
        (SPITZER,SPITZER),
        (KEPLER,KEPLER),
        (PANSTARR1,PANSTARR1),
        (UBV,UBV),
        (STROEMGREN,STROEMGREN),
        (DENIS,DENIS),
        (TYCHO2,TYCHO2),

    ]

    model_file = models.CharField(choices=MODEL_FILE_CHOICES, max_length=55, blank=False, null=False, default=SHARMA_2019)

    apparent_magnitude_min = models.FloatField(blank=False, null=False, default=-100.0)
    apparent_magnitude_max = models.FloatField(blank=False, null=False, default=14.0)

    photo_sys_1 = models.CharField(choices=PHOTO_SYS_1_CHOICES, max_length=20, blank=False, null=False, default=PARSEC_1)

    photo_sys_2 = models.CharField(choices=PHOTO_SYS_2_CHOICES, max_length=55, blank=False, null=False, default=GAIADR2_TMASS)





