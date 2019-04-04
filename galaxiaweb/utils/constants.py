SHARMA_2011 = 'Sharma 2011'
SHARMA_2011_VALUE = 'Model/population_parameters_mptd.ebf'
SHARMA_2019 = 'Sharma 2019'
SHARMA_2019_VALUE = 'Model/population_parameters_mrtd5.ebf'
PARSEC_1 = 'parsec1'
PARSEC_1_VALUE = 'parsec1'
GAIADR2_TMASS = 'GAIADR2_TMASS'
GAIADR2_TMASS_VALUE = ['gaia_g','gaia_gbp','gaia_grp','tmass_j','tmass_h','tmass_ks']
WISE = 'WISE'
WISE_VALUE = ['wise_w1','wise_w2','wise_w3','wise_w4']
SPITZER = 'SPITZER'
SPITZER_VALUE = ['irac_3.6', 'irac_4.5','irac_5.8','irac_8.0', 'mips_24', 'mips_70','mips_160']
KEPLER = 'KEPLER'
KEPLER_VALUE = ['tess_te','kepler_ke','sdss_g','sdss_r','sdss_i','sdss_z','kepler_ddo51']
PANSTARR1 = 'PANSTARR 1'
PANSTARR1_VALUE = ['pans1_g','pans1_r','pans1_i','pans1_z','pans1_y','pans1_w']
UBV = 'UBV'
UBV_VALUE =  ['ubv_u','ubv_b','ubv_v','ubv_r','ubv_i','ubv_j','ubv_h','ubv_k']
STROEMGREN = 'STROEMGREN'
STROEMGREN_VALUE=['stroemgren_v1','stroemgren_u','stroemgren_v','stroemgren_b','stroemgren_y','stroemgren_hb_w','stroemgren_hb_n']
DENIS='DENIS'
DENIS_VALUE= ['denis_i','denis_j','denis_ks']
TYCHO2 = 'TYCHO2'
TYCHO2_VALUE = ['tycho_bt','tycho_vt']
ALL_SKY = 'All Sky'
ALL_SKY_VALUE = 0
PATCH = 'Circular Patch'
PATCH_VALUE = 1
ALL_POP='All thin/thick disk, halo and bulge populations'
ALL_POP_VALUE=-1
THIN_DISK_015='Thin Disk <0.15 Gyr'
THIN_DISK_015_VALUE=0
THIN_DISK_1='Thin Disk  0.15-1 Gyr'
THIN_DISK_2='Thin Disk  1-2 Gyr'
THIN_DISK_3='Thin Disk  2-3 Gyr'
THIN_DISK_5='Thin Disk  3-5 Gyr'
THIN_DISK_7='Thin Disk  5-7 Gyr'
THIN_DISK_10='Thin Disk  7-10 Gyr'
THICK_DISK='Thick Disk'
STELLAR_HALO='Stellar Halo'
THIN_DISK_1_VALUE = 1
THIN_DISK_2_VALUE = 2
THIN_DISK_3_VALUE = 3
THIN_DISK_5_VALUE = 4
THIN_DISK_7_VALUE = 5
THIN_DISK_10_VALUE = 6
THICK_DISK_VALUE = 7
STELLAR_HALO_VALUE = 8
BULGE='Bulge'
BULGE_VALUE =9
BULLOCK='Bullock & Johnston stellar halos'
BULLOCK_VALUE=10


PLACEHOLDER1 = 'Placeholder'
PLACEHOLDER1_VALUE = 'Placeholder'

NAME_VALUES = dict()

NAME_VALUES.update({
    SHARMA_2019: SHARMA_2019_VALUE,
    SHARMA_2011: SHARMA_2011_VALUE,
    PARSEC_1: PARSEC_1_VALUE,
    GAIADR2_TMASS:GAIADR2_TMASS_VALUE,
    WISE:WISE_VALUE,
    SPITZER: SPITZER_VALUE,
    KEPLER: KEPLER_VALUE,
    PANSTARR1: PANSTARR1_VALUE,
    UBV: UBV_VALUE,
    STROEMGREN: STROEMGREN_VALUE,
    DENIS: DENIS_VALUE,
    TYCHO2: TYCHO2_VALUE,
    ALL_SKY: ALL_SKY_VALUE,
    PATCH: PATCH_VALUE,
    PLACEHOLDER1: PLACEHOLDER1_VALUE,
    ALL_POP: ALL_POP_VALUE,
    THIN_DISK_015: THIN_DISK_015_VALUE,
    THIN_DISK_1:THIN_DISK_1_VALUE,
    THIN_DISK_2:THIN_DISK_2_VALUE,
    THIN_DISK_3: THIN_DISK_3_VALUE,
    THIN_DISK_5: THIN_DISK_5_VALUE,
    THIN_DISK_7: THIN_DISK_7_VALUE,
    THIN_DISK_10: THIN_DISK_10_VALUE,
    THICK_DISK: THICK_DISK_VALUE,
    STELLAR_HALO: STELLAR_HALO_VALUE,
    BULGE: BULGE_VALUE,
    BULLOCK: BULLOCK_VALUE,
})
