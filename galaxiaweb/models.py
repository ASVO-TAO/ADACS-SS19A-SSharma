import uuid
import os
from django.db import models
from django.core.validators import *
# from django.core.files.base import File, ContentFile
# from django.core.files.storage import FileSystemStorage
from django.utils.timezone import datetime
from django.conf import settings

from django_hpc_job_controller.models import HpcJob

from .utils.constants import *


# Create your models here.
class Job(HpcJob):
    """
    Job model extending HpcJob
    """
    creation_time = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    json_representation = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.pk)

    def as_json(self):
        return dict(
            id=self.id,
            value=dict(
                creation_time=self.creation_time.strftime('%d %b %Y %I:%m %p'),
            ),
        )


class JobParameter(models.Model):
    MODEL_FILE_CHOICES = [
        (SHARMA_2011, SHARMA_2011),
        (SHARMA_2019, SHARMA_2019),
    ]

    PHOTO_SYS_1_CHOICES = [
        (PARSEC_1, PARSEC_1),
    ]

    PHOTO_SYS_2_CHOICES = [
        (GAIADR2_TMASS, GAIADR2_TMASS),
        (WISE, WISE),
        (SPITZER, SPITZER),
        (KEPLER, KEPLER),
        (PANSTARR1, PANSTARR1),
        (UBV, UBV),
        (STROEMGREN, STROEMGREN),
        (DENIS, DENIS),
        (TYCHO2, TYCHO2),

    ]

    GEOMETRY_OPTIONS = [
        (ALL_SKY, ALL_SKY),
        (PATCH, PATCH),
    ]

    POPULATIONS = [
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

    job = models.ForeignKey(Job, on_delete=models.CASCADE, blank=False, null=False)

    model_file = models.CharField(choices=MODEL_FILE_CHOICES, max_length=55, blank=False, null=False,
                                  default=SHARMA_2019)

    magnitude_name = models.CharField(choices=MAGNITUDE_NAME_CHOICES, max_length=55, blank=False, null=False,
                                      default=GAIA_G)
    apparent_magnitude_min = models.FloatField(blank=False, null=False, default=-100.0)
    apparent_magnitude_max = models.FloatField(blank=False, null=False, default=14.0)

    photo_sys_1 = models.CharField(choices=PHOTO_SYS_1_CHOICES, max_length=20, blank=False, null=False,
                                   default=PARSEC_1)

    photo_sys_2 = models.CharField(choices=PHOTO_SYS_2_CHOICES, max_length=55, blank=False, null=False,
                                   default=GAIADR2_TMASS)

    # photo_sys_extra = photo_sys_1+photo_sys_2

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

    population_ID = models.CharField(choices=POPULATIONS, max_length=55, blank=False, null=False, default=ALL_POP)
    warp_flare = models.BooleanField(blank=True, null=False, default=True)

    job_key = models.CharField(max_length=100, null=False, blank=False, unique=True, default=uuid.uuid4)

    seed = models.PositiveIntegerField(blank=False, null=False, default=17, validators=[MinValueValidator(1)])
    r_max = models.FloatField(blank=False, null=False, default=1000, validators=[MinValueValidator(1.0)])

    email = models.CharField(blank=True, null=False, max_length=254, validators=[validate_email])

    parameter_file_url = models.CharField(null=True, default=None, max_length=100)

    parameters = models.BinaryField(default=None, null=True)

    def save(self, *args, **kwargs):

        self.job_key = datetime.now().strftime('%d-%b-%Y_%H%M')
        self.save_parameter_file(self.to_params_dict())
        super().save(*args, **kwargs)

    def to_params_dict(self):

        params_dict = dict()
        params_dict['outputFile'] = f"galaxia_{self.job_key}"
        params_dict['modelFile'] = NAME_VALUES[self.model_file]
        params_dict['codeDataDir'] = settings.GALAXIA_CODE_DATA_DIR
        params_dict['outputDir'] = './'
        params_dict['photoSys'] = '{}/{}'.format(NAME_VALUES[self.photo_sys_1], NAME_VALUES[self.photo_sys_2])
        params_dict['magcolorNames'] = '{},{},{}'.format(NAME_VALUES[self.magnitude_name],
                                                         NAME_VALUES[self.magnitude_name_1],
                                                         NAME_VALUES[self.magnitude_name_2])
        params_dict['appMagLimits[0]'] = self.apparent_magnitude_min
        params_dict['appMagLimits[1]'] = self.apparent_magnitude_max
        params_dict['absMagLimits[0]'] = self.absolute_magnitude_min
        params_dict['absMagLimits[1]'] = self.absolute_magnitude_max
        params_dict['colorLimits[0]'] = self.colour_limit_min
        params_dict['colorLimits[1]'] = self.colour_limit_max
        params_dict['geometryOption'] = NAME_VALUES[self.geometry_options]
        params_dict['longitude'] = self.longitude
        params_dict['latitude'] = self.latitude
        params_dict['starType'] = '0'
        params_dict['photoError'] = '0'
        params_dict['surveyArea'] = self.survey_area
        params_dict['fSample'] = self.sample_fraction
        params_dict['popID'] = NAME_VALUES[self.population_ID]
        params_dict['warpFlareOn'] = '1' if self.warp_flare else '0'
        params_dict['seed'] = self.seed
        params_dict['r_max'] = self.r_max

        return params_dict

    def save_parameter_file(self, params_dict):

        content_list = [f"{key.ljust(40)}{value}" for (key, value) in params_dict.items()]
        # content_list = [f"{key:<40}{value}" for (key, value) in params_dict.items()]
        content = "\n".join(content_list)
        content += "\n"

        storage_location = os.path.join(settings.MEDIA_ROOT, self.job_key)

        if not os.path.exists(storage_location):
            os.makedirs(storage_location)

        parameter_file_path = os.path.join(storage_location, self.job_key)

        print(storage_location)
        print(parameter_file_path)

        with open(parameter_file_path, 'w') as f:
            # myfile = File(f)
            f.write(content)
            f.writelines('\n')

        # storage_location = os.path.join(settings.MEDIA_ROOT, settings.PARAMETER_FILES_DIR)
        # file = ContentFile(content)
        # fs = FileSystemStorage(location=storage_location)
        # fs.save(str(self.job_key), file)
        self.parameter_file_url = self.job_key + "/" + self.job_key
        self.parameters = bytes(content, encoding='utf-8')






