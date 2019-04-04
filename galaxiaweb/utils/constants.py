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
    PLACEHOLDER1: PLACEHOLDER1_VALUE,
})
