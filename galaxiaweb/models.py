from django.db import models

from .utils.constants import *

# Create your models here.


class JobParameter(models.Model):
    MODEL_FILE_CHOICES = [
        (SHARMA_2011, SHARMA_2011),
        (SHARMA_2019, SHARMA_2019),
    ]
    model_file = models.CharField(choices=MODEL_FILE_CHOICES, max_length=55, blank=False, null=False, default=SHARMA_2019)

    apparent_magnitude_min = models.FloatField(blank=False, null=False, default=-100.0)
    apparent_magnitude_max = models.FloatField(blank=False, null=False, default=14.0)