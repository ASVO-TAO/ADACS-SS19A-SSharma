from django.db import models
from django.core.validators import *
from django.core.exceptions import ValidationError

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

    MAGNITUDE_NAME_CHOICES = [
        (GAIA_G, GAIA_G),
        (GAIA_GBP, GAIA_GBP),
        (GAIA_GRP, GAIA_GRP),
        (TMASS_J, TMASS_J),
        (TMASS_H, TMASS_H),
        (TMASS_KS, TMASS_KS),
        (WISE_W1, WISE_W1),
        (WISE_W2, WISE_W2),
        (WISE_W3, WISE_W3),
        (WISE_W4, WISE_W4),
        (IRAC_36, IRAC_36),
        (IRAC_45, IRAC_45),
        (IRAC_58, IRAC_58),
        (IRAC_80, IRAC_80),
        (MIPS_24, MIPS_24),
        (MIPS_70, MIPS_70),
        (MIPS_160, MIPS_160),
        (TESS_TE, TESS_TE),
        (KEPLER_KE, KEPLER_KE),
        (SDSS_G, SDSS_G),
        (SDSS_R, SDSS_R),
        (SDSS_I, SDSS_I),
        (SDSS_Z, SDSS_Z),
        (KEPLER_DDO51, KEPLER_DDO51),
        (PANS1_G, PANS1_G),
        (PANS1_R, PANS1_R),
        (PANS1_I, PANS1_I),
        (PANS1_Z, PANS1_Z),
        (PANS1_Y, PANS1_Y),
        (PANS1_W, PANS1_Y),
        (UBV_U, UBV_U),
        (UBV_B, UBV_B),
        (UBV_V, UBV_V),
        (UBV_R, UBV_R),
        (UBV_I, UBV_I),
        (UBV_J, UBV_J),
        (UBV_H, UBV_H),
        (UBV_K, UBV_K),
        (STROEMGREN_V1, STROEMGREN_V1),
        (STROEMGREN_U, STROEMGREN_U),
        (STROEMGREN_V, STROEMGREN_V),
        (STROEMGREN_B, STROEMGREN_B),
        (STROEMGREN_Y, STROEMGREN_Y),
        (STROEMGREN_HB_W, STROEMGREN_HB_W),
        (STROEMGREN_HB_N, STROEMGREN_HB_N),
        (DENIS_I, DENIS_I),
        (DENIS_J, DENIS_J),
        (DENIS_KS, DENIS_KS),
        (TYCHO_BT, TYCHO_BT),
        (TYCHO_VT, TYCHO_VT),
    ]

    model_file = models.CharField(choices=MODEL_FILE_CHOICES, max_length=55, blank=False, null=False, default=SHARMA_2019)

    magnitude_name = models.CharField(choices=MAGNITUDE_NAME_CHOICES, max_length=55, blank=False, null=False,
                                        default=GAIA_G)
    apparent_magnitude_min = models.FloatField(blank=False, null=False, default=-100.0)
    apparent_magnitude_max = models.FloatField(blank=False, null=False, default=14.0)

    photo_sys_1 = models.CharField(choices=PHOTO_SYS_1_CHOICES, max_length=20, blank=False, null=False, default=PARSEC_1)

    photo_sys_2 = models.CharField(choices=PHOTO_SYS_2_CHOICES, max_length=55, blank=False, null=False, default=GAIADR2_TMASS)

    #photo_sys_extra = photo_sys_1+photo_sys_2

    colour_limit_min = models.FloatField(blank=False, null=False, default=-100)
    colour_limit_max = models.FloatField(blank=False, null=False, default=100)

    absolute_magnitude_min = models.FloatField(blank=False, null=False, default=-100.0)
    absolute_magnitude_max = models.FloatField(blank=False, null=False, default=100.0)

    magnitude_name_1 = models.CharField(choices=MAGNITUDE_NAME_CHOICES, max_length=55, blank=False, null=False,
                                  default=GAIA_G)
    magnitude_name_2 = models.CharField(choices=MAGNITUDE_NAME_CHOICES, max_length=55, blank=False, null=False,
                                        default=GAIA_GBP)

    geometry_options = models.CharField(choices=GEOMETRY_OPTIONS, max_length=55, blank=False, null=False,
                                        default=ALL_SKY)

    longitude = models.FloatField(blank=False, null=False, default=0,
                                  validators=[MinValueValidator(0), MaxValueValidator(360)]
                                  )
    latitude = models.FloatField(blank=False, null=False, default=90,
                                 validators=[MinValueValidator(-90), MaxValueValidator(90)])

    survey_area = models.FloatField(blank=False, null=False, default=100, validators=[MaxValueValidator(41252)])
    sample_fraction = models.FloatField(blank=False, null=False, default=1, validators=[MinValueValidator(0)])

    population_ID = models.CharField(choices=POPULATIONS, max_length=55, blank=False, null=False,
                                        default=ALL_POP)
    warp_flare = models.BooleanField(blank=True, null=False, default=True)
    seed = models.PositiveIntegerField(blank=False, null=False, default=17, validators=[MinValueValidator(1)])
    r_max = models.FloatField(blank=False, null=False, default=1000, validators=[MinValueValidator(1.0)])
