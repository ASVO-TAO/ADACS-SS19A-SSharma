# Generated by Django 2.1.7 on 2019-04-09 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galaxiaweb', '0010_auto_20190408_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobparameter',
            name='magnitude_name',
            field=models.CharField(choices=[('gaia_g', 'gaia_g'), ('gaia_gbp', 'gaia_gbp'), ('gaia_grp', 'gaia_grp'), ('tmass_j', 'tmass_j'), ('tmass_h', 'tmass_h'), ('tmass_ks', 'tmass_ks'), ('wise_w1', 'wise_w1'), ('wise_w2', 'wise_w2'), ('wise_w3', 'wise_w3'), ('wise_w4', 'wise_w4'), ('irac_3.6', 'irac_3.6'), ('irac_4.5', 'irac_4.5'), ('irac_5.8', 'irac_5.8'), ('irac_8.0', 'irac_8.0'), ('mips_24', 'mips_24'), ('mips_70', 'mips_70'), ('mips_160', 'mips_160'), ('tess_te', 'tess_te'), ('kepler_ke', 'kepler_ke'), ('sdss_g', 'sdss_g'), ('sdss_r', 'sdss_r'), ('sdss_i', 'sdss_i'), ('sdss_z', 'sdss_z'), ('kepler_ddo51', 'kepler_ddo51'), ('pans1_g', 'pans1_g'), ('pans1_r', 'pans1_r'), ('pans1_i', 'pans1_i'), ('pans1_z', 'pans1_z'), ('pans1_y', 'pans1_y'), ('pans1_w', 'pans1_y'), ('ubv_u', 'ubv_u'), ('ubv_b', 'ubv_b'), ('ubv_v', 'ubv_v'), ('ubv_r', 'ubv_r'), ('ubv_i', 'ubv_i'), ('ubv_j', 'ubv_j'), ('ubv_h', 'ubv_h'), ('ubv_k', 'ubv_k'), ('stroemgren_v1', 'stroemgren_v1'), ('stroemgren_u', 'stroemgren_u'), ('stroemgren_v', 'stroemgren_v'), ('stroemgren_b', 'stroemgren_b'), ('stroemgren_y', 'stroemgren_y'), ('stroemgren_hb_w', 'stroemgren_hb_w'), ('stroemgren_hb_n', 'stroemgren_hb_n'), ('denis_i', 'denis_i'), ('denis_j', 'denis_j'), ('denis_ks', 'denis_ks'), ('tycho_bt', 'tycho_bt'), ('tycho_vt', 'tycho_vt')], default='gaia_g', max_length=55),
        ),
        migrations.AlterField(
            model_name='jobparameter',
            name='magnitude_name_1',
            field=models.CharField(choices=[('gaia_g', 'gaia_g'), ('gaia_gbp', 'gaia_gbp'), ('gaia_grp', 'gaia_grp'), ('tmass_j', 'tmass_j'), ('tmass_h', 'tmass_h'), ('tmass_ks', 'tmass_ks'), ('wise_w1', 'wise_w1'), ('wise_w2', 'wise_w2'), ('wise_w3', 'wise_w3'), ('wise_w4', 'wise_w4'), ('irac_3.6', 'irac_3.6'), ('irac_4.5', 'irac_4.5'), ('irac_5.8', 'irac_5.8'), ('irac_8.0', 'irac_8.0'), ('mips_24', 'mips_24'), ('mips_70', 'mips_70'), ('mips_160', 'mips_160'), ('tess_te', 'tess_te'), ('kepler_ke', 'kepler_ke'), ('sdss_g', 'sdss_g'), ('sdss_r', 'sdss_r'), ('sdss_i', 'sdss_i'), ('sdss_z', 'sdss_z'), ('kepler_ddo51', 'kepler_ddo51'), ('pans1_g', 'pans1_g'), ('pans1_r', 'pans1_r'), ('pans1_i', 'pans1_i'), ('pans1_z', 'pans1_z'), ('pans1_y', 'pans1_y'), ('pans1_w', 'pans1_y'), ('ubv_u', 'ubv_u'), ('ubv_b', 'ubv_b'), ('ubv_v', 'ubv_v'), ('ubv_r', 'ubv_r'), ('ubv_i', 'ubv_i'), ('ubv_j', 'ubv_j'), ('ubv_h', 'ubv_h'), ('ubv_k', 'ubv_k'), ('stroemgren_v1', 'stroemgren_v1'), ('stroemgren_u', 'stroemgren_u'), ('stroemgren_v', 'stroemgren_v'), ('stroemgren_b', 'stroemgren_b'), ('stroemgren_y', 'stroemgren_y'), ('stroemgren_hb_w', 'stroemgren_hb_w'), ('stroemgren_hb_n', 'stroemgren_hb_n'), ('denis_i', 'denis_i'), ('denis_j', 'denis_j'), ('denis_ks', 'denis_ks'), ('tycho_bt', 'tycho_bt'), ('tycho_vt', 'tycho_vt')], default='gaia_g', max_length=55),
        ),
        migrations.AlterField(
            model_name='jobparameter',
            name='magnitude_name_2',
            field=models.CharField(choices=[('gaia_g', 'gaia_g'), ('gaia_gbp', 'gaia_gbp'), ('gaia_grp', 'gaia_grp'), ('tmass_j', 'tmass_j'), ('tmass_h', 'tmass_h'), ('tmass_ks', 'tmass_ks'), ('wise_w1', 'wise_w1'), ('wise_w2', 'wise_w2'), ('wise_w3', 'wise_w3'), ('wise_w4', 'wise_w4'), ('irac_3.6', 'irac_3.6'), ('irac_4.5', 'irac_4.5'), ('irac_5.8', 'irac_5.8'), ('irac_8.0', 'irac_8.0'), ('mips_24', 'mips_24'), ('mips_70', 'mips_70'), ('mips_160', 'mips_160'), ('tess_te', 'tess_te'), ('kepler_ke', 'kepler_ke'), ('sdss_g', 'sdss_g'), ('sdss_r', 'sdss_r'), ('sdss_i', 'sdss_i'), ('sdss_z', 'sdss_z'), ('kepler_ddo51', 'kepler_ddo51'), ('pans1_g', 'pans1_g'), ('pans1_r', 'pans1_r'), ('pans1_i', 'pans1_i'), ('pans1_z', 'pans1_z'), ('pans1_y', 'pans1_y'), ('pans1_w', 'pans1_y'), ('ubv_u', 'ubv_u'), ('ubv_b', 'ubv_b'), ('ubv_v', 'ubv_v'), ('ubv_r', 'ubv_r'), ('ubv_i', 'ubv_i'), ('ubv_j', 'ubv_j'), ('ubv_h', 'ubv_h'), ('ubv_k', 'ubv_k'), ('stroemgren_v1', 'stroemgren_v1'), ('stroemgren_u', 'stroemgren_u'), ('stroemgren_v', 'stroemgren_v'), ('stroemgren_b', 'stroemgren_b'), ('stroemgren_y', 'stroemgren_y'), ('stroemgren_hb_w', 'stroemgren_hb_w'), ('stroemgren_hb_n', 'stroemgren_hb_n'), ('denis_i', 'denis_i'), ('denis_j', 'denis_j'), ('denis_ks', 'denis_ks'), ('tycho_bt', 'tycho_bt'), ('tycho_vt', 'tycho_vt')], default='gaia_gbp', max_length=55),
        ),
    ]
