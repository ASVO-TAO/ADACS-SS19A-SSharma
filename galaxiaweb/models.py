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

    GEOMETRY_OPTIONS =[
        (ALL_SKY,ALL_SKY),
        (PATCH,PATCH),
    ]

    POPULATIONS =[
        (ALL_POP, ALL_POP),
        (THIN_DISK_015, THIN_DISK_015),
        (THIN_DISK_1, THIN_DISK_1),
        (THIN_DISK_2, THIN_DISK_2),
        (THIN_DISK_3, THIN_DISK_3),
        (THIN_DISK_5, THIN_DISK_5),
        (THIN_DISK_7, THIN_DISK_7),
        (THIN_DISK_10, THIN_DISK_10),
        (THICK_DISK, THICK_DISK),
        (STELLAR_HALO, STELLAR_HALO),
        (BULGE, BULGE),
        (BULLOCK, BULLOCK),

    ]

    PLACEHOLDER = [(PLACEHOLDER1,PLACEHOLDER1)]

    ######################### Models

    model_file = models.CharField(choices=MODEL_FILE_CHOICES, max_length=55, blank=False, null=False, default=SHARMA_2019)

    magnitude_name = models.CharField(choices=PLACEHOLDER, max_length=55, blank=False, null=False,
                                        default=PLACEHOLDER1)
    apparent_magnitude_min = models.FloatField(blank=False, null=False, default=-100.0)
    apparent_magnitude_max = models.FloatField(blank=False, null=False, default=14.0)

    photo_sys_1 = models.CharField(choices=PHOTO_SYS_1_CHOICES, max_length=20, blank=False, null=False, default=PARSEC_1)

    photo_sys_2 = models.CharField(choices=PHOTO_SYS_2_CHOICES, max_length=55, blank=False, null=False, default=GAIADR2_TMASS)

    #photo_sys_extra = photo_sys_1+photo_sys_2

    colour_limit_min = models.FloatField(blank=False, null=False, default=-100)
    colour_limit_max = models.FloatField(blank=False, null=False, default=100)

    absolute_magnitude_min = models.FloatField(blank=False, null=False, default=-100.0)
    absolute_magnitude_max = models.FloatField(blank=False, null=False, default=100.0)

    magnitude_name_1 = models.CharField(choices=PLACEHOLDER, max_length=55, blank=False, null=False,
                                  default=PLACEHOLDER1)
    magnitude_name_2 = models.CharField(choices=PLACEHOLDER, max_length=55, blank=False, null=False,
                                        default=PLACEHOLDER1)

    geometry_options = models.CharField(choices=GEOMETRY_OPTIONS, max_length=55, blank=False, null=False,
                                        default=ALL_SKY)

    longitude = models.FloatField(blank=False, null=False, default=0)
    latitude = models.FloatField(blank=False, null=False, default=90)

    survey_area = models.FloatField(blank=False, null=False, default=100)
    sample_fraction = models.FloatField(blank=False, null=False, default=1)

    population_ID = models.CharField(choices=POPULATIONS, max_length=55, blank=False, null=False,
                                        default=ALL_POP)
    warp_flare = models.BooleanField(blank=True, null=False, default=True)
    seed = models.PositiveIntegerField(blank=False, null=False, default=17)
    r_max = models.FloatField(blank=False, null=False, default=1000)