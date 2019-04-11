# Generated by Django 2.1.7 on 2019-04-11 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_hpc_job_controller', '0007_websockettoken_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('hpcjob_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_hpc_job_controller.HpcJob')),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('json_representation', models.TextField(blank=True, null=True)),
            ],
            bases=('django_hpc_job_controller.hpcjob',),
        ),
        migrations.CreateModel(
            name='JobParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_file', models.CharField(choices=[('Sharma 2011', 'Sharma 2011'), ('Sharma 2019', 'Sharma 2019')], default='Sharma 2019', max_length=55)),
                ('magnitude_name', models.CharField(choices=[('gaia_g', 'gaia_g'), ('gaia_gbp', 'gaia_gbp'), ('gaia_grp', 'gaia_grp'), ('tmass_j', 'tmass_j'), ('tmass_h', 'tmass_h'), ('tmass_ks', 'tmass_ks'), ('wise_w1', 'wise_w1'), ('wise_w2', 'wise_w2'), ('wise_w3', 'wise_w3'), ('wise_w4', 'wise_w4'), ('irac_3.6', 'irac_3.6'), ('irac_4.5', 'irac_4.5'), ('irac_5.8', 'irac_5.8'), ('irac_8.0', 'irac_8.0'), ('mips_24', 'mips_24'), ('mips_70', 'mips_70'), ('mips_160', 'mips_160'), ('tess_te', 'tess_te'), ('kepler_ke', 'kepler_ke'), ('sdss_g', 'sdss_g'), ('sdss_r', 'sdss_r'), ('sdss_i', 'sdss_i'), ('sdss_z', 'sdss_z'), ('kepler_ddo51', 'kepler_ddo51'), ('pans1_g', 'pans1_g'), ('pans1_r', 'pans1_r'), ('pans1_i', 'pans1_i'), ('pans1_z', 'pans1_z'), ('pans1_y', 'pans1_y'), ('pans1_w', 'pans1_y'), ('ubv_u', 'ubv_u'), ('ubv_b', 'ubv_b'), ('ubv_v', 'ubv_v'), ('ubv_r', 'ubv_r'), ('ubv_i', 'ubv_i'), ('ubv_j', 'ubv_j'), ('ubv_h', 'ubv_h'), ('ubv_k', 'ubv_k'), ('stroemgren_v1', 'stroemgren_v1'), ('stroemgren_u', 'stroemgren_u'), ('stroemgren_v', 'stroemgren_v'), ('stroemgren_b', 'stroemgren_b'), ('stroemgren_y', 'stroemgren_y'), ('stroemgren_hb_w', 'stroemgren_hb_w'), ('stroemgren_hb_n', 'stroemgren_hb_n'), ('denis_i', 'denis_i'), ('denis_j', 'denis_j'), ('denis_ks', 'denis_ks'), ('tycho_bt', 'tycho_bt'), ('tycho_vt', 'tycho_vt')], default='gaia_g', max_length=55)),
                ('apparent_magnitude_min', models.FloatField(default=-100.0)),
                ('apparent_magnitude_max', models.FloatField(default=14.0)),
                ('photo_sys_1', models.CharField(choices=[('parsec1', 'parsec1')], default='parsec1', max_length=20)),
                ('photo_sys_2', models.CharField(choices=[('GAIADR2_TMASS', 'GAIADR2_TMASS'), ('WISE', 'WISE'), ('SPITZER', 'SPITZER'), ('KEPLER', 'KEPLER'), ('PANSTARR 1', 'PANSTARR 1'), ('UBV', 'UBV'), ('STROEMGREN', 'STROEMGREN'), ('DENIS', 'DENIS'), ('TYCHO2', 'TYCHO2')], default='GAIADR2_TMASS', max_length=55)),
                ('colour_limit_min', models.FloatField(default=-100)),
                ('colour_limit_max', models.FloatField(default=100)),
                ('absolute_magnitude_min', models.FloatField(default=-100.0)),
                ('absolute_magnitude_max', models.FloatField(default=100.0)),
                ('magnitude_name_1', models.CharField(choices=[('gaia_g', 'gaia_g'), ('gaia_gbp', 'gaia_gbp'), ('gaia_grp', 'gaia_grp'), ('tmass_j', 'tmass_j'), ('tmass_h', 'tmass_h'), ('tmass_ks', 'tmass_ks'), ('wise_w1', 'wise_w1'), ('wise_w2', 'wise_w2'), ('wise_w3', 'wise_w3'), ('wise_w4', 'wise_w4'), ('irac_3.6', 'irac_3.6'), ('irac_4.5', 'irac_4.5'), ('irac_5.8', 'irac_5.8'), ('irac_8.0', 'irac_8.0'), ('mips_24', 'mips_24'), ('mips_70', 'mips_70'), ('mips_160', 'mips_160'), ('tess_te', 'tess_te'), ('kepler_ke', 'kepler_ke'), ('sdss_g', 'sdss_g'), ('sdss_r', 'sdss_r'), ('sdss_i', 'sdss_i'), ('sdss_z', 'sdss_z'), ('kepler_ddo51', 'kepler_ddo51'), ('pans1_g', 'pans1_g'), ('pans1_r', 'pans1_r'), ('pans1_i', 'pans1_i'), ('pans1_z', 'pans1_z'), ('pans1_y', 'pans1_y'), ('pans1_w', 'pans1_y'), ('ubv_u', 'ubv_u'), ('ubv_b', 'ubv_b'), ('ubv_v', 'ubv_v'), ('ubv_r', 'ubv_r'), ('ubv_i', 'ubv_i'), ('ubv_j', 'ubv_j'), ('ubv_h', 'ubv_h'), ('ubv_k', 'ubv_k'), ('stroemgren_v1', 'stroemgren_v1'), ('stroemgren_u', 'stroemgren_u'), ('stroemgren_v', 'stroemgren_v'), ('stroemgren_b', 'stroemgren_b'), ('stroemgren_y', 'stroemgren_y'), ('stroemgren_hb_w', 'stroemgren_hb_w'), ('stroemgren_hb_n', 'stroemgren_hb_n'), ('denis_i', 'denis_i'), ('denis_j', 'denis_j'), ('denis_ks', 'denis_ks'), ('tycho_bt', 'tycho_bt'), ('tycho_vt', 'tycho_vt')], default='gaia_g', max_length=55)),
                ('magnitude_name_2', models.CharField(choices=[('gaia_g', 'gaia_g'), ('gaia_gbp', 'gaia_gbp'), ('gaia_grp', 'gaia_grp'), ('tmass_j', 'tmass_j'), ('tmass_h', 'tmass_h'), ('tmass_ks', 'tmass_ks'), ('wise_w1', 'wise_w1'), ('wise_w2', 'wise_w2'), ('wise_w3', 'wise_w3'), ('wise_w4', 'wise_w4'), ('irac_3.6', 'irac_3.6'), ('irac_4.5', 'irac_4.5'), ('irac_5.8', 'irac_5.8'), ('irac_8.0', 'irac_8.0'), ('mips_24', 'mips_24'), ('mips_70', 'mips_70'), ('mips_160', 'mips_160'), ('tess_te', 'tess_te'), ('kepler_ke', 'kepler_ke'), ('sdss_g', 'sdss_g'), ('sdss_r', 'sdss_r'), ('sdss_i', 'sdss_i'), ('sdss_z', 'sdss_z'), ('kepler_ddo51', 'kepler_ddo51'), ('pans1_g', 'pans1_g'), ('pans1_r', 'pans1_r'), ('pans1_i', 'pans1_i'), ('pans1_z', 'pans1_z'), ('pans1_y', 'pans1_y'), ('pans1_w', 'pans1_y'), ('ubv_u', 'ubv_u'), ('ubv_b', 'ubv_b'), ('ubv_v', 'ubv_v'), ('ubv_r', 'ubv_r'), ('ubv_i', 'ubv_i'), ('ubv_j', 'ubv_j'), ('ubv_h', 'ubv_h'), ('ubv_k', 'ubv_k'), ('stroemgren_v1', 'stroemgren_v1'), ('stroemgren_u', 'stroemgren_u'), ('stroemgren_v', 'stroemgren_v'), ('stroemgren_b', 'stroemgren_b'), ('stroemgren_y', 'stroemgren_y'), ('stroemgren_hb_w', 'stroemgren_hb_w'), ('stroemgren_hb_n', 'stroemgren_hb_n'), ('denis_i', 'denis_i'), ('denis_j', 'denis_j'), ('denis_ks', 'denis_ks'), ('tycho_bt', 'tycho_bt'), ('tycho_vt', 'tycho_vt')], default='gaia_gbp', max_length=55)),
                ('geometry_options', models.CharField(choices=[('All Sky', 'All Sky'), ('Circular Patch', 'Circular Patch')], default='All Sky', max_length=55)),
                ('longitude', models.FloatField(default=0)),
                ('latitude', models.FloatField(default=90)),
                ('survey_area', models.FloatField(default=100)),
                ('sample_fraction', models.FloatField(default=1)),
                ('population_ID', models.CharField(choices=[('All thin/thick disk, halo and bulge populations', 'All thin/thick disk, halo and bulge populations'), ('Thin Disk <0.15 Gyr', 'Thin Disk <0.15 Gyr'), ('Thin Disk  0.15-1 Gyr', 'Thin Disk  0.15-1 Gyr'), ('Thin Disk  1-2 Gyr', 'Thin Disk  1-2 Gyr'), ('Thin Disk  2-3 Gyr', 'Thin Disk  2-3 Gyr'), ('Thin Disk  3-5 Gyr', 'Thin Disk  3-5 Gyr'), ('Thin Disk  5-7 Gyr', 'Thin Disk  5-7 Gyr'), ('Thin Disk  7-10 Gyr', 'Thin Disk  7-10 Gyr'), ('Thick Disk', 'Thick Disk'), ('Stellar Halo', 'Stellar Halo'), ('Bulge', 'Bulge'), ('Bullock & Johnston stellar halos', 'Bullock & Johnston stellar halos')], default='All thin/thick disk, halo and bulge populations', max_length=55)),
                ('warp_flare', models.BooleanField(blank=True, default=True)),
                ('seed', models.PositiveIntegerField(default=17)),
                ('r_max', models.FloatField(default=1000)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galaxiaweb.Job')),
            ],
        ),
    ]
