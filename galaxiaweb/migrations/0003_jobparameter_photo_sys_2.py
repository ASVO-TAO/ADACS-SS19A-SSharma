# Generated by Django 2.1.7 on 2019-03-29 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galaxiaweb', '0002_jobparameter_photo_sys_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobparameter',
            name='photo_sys_2',
            field=models.CharField(choices=[('GAIADR2_TMASS', 'GAIADR2_TMASS'), ('WISE', 'WISE'), ('SPITZER', 'SPITZER'), ('KEPLER', 'KEPLER'), ('PANSTARR 1', 'PANSTARR 1'), ('UBV', 'UBV'), ('STROEMGREN', 'STROEMGREN'), ('DENIS', 'DENIS'), ('TYCHO2', 'TYCHO2')], default='GAIADR2_TMASS', max_length=55),
        ),
    ]
