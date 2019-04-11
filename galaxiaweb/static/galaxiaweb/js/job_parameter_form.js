
let ready = $(document).ready(function() {
    // photo_sys_2 hide/show options on change.

    $('#id_magnitude_name option').addClass('magnitude_name');
    $('#id_magnitude_name_1 option').addClass('magnitude_name_1');
    $('#id_magnitude_name_2 option').addClass('magnitude_name_2');

    photo_sys_2_onChange();
    update_all_sky_and_circular_patch();


    $('body').on('change', '#id_photo_sys_2',
        function() {

            photo_sys_2_onChange();

        })
        .on('change', '#id_geometry_options',
        function() {

            update_all_sky_and_circular_patch();

        });



    function photo_sys_2_onChange(){
        let photosys2 = $('#id_photo_sys_2').find(":selected").text();
            update_magnitude_name_list(photosys2);
            update_blue_color_band_list(photosys2);
            update_red_color_band_list(photosys2)
    }
    function update_magnitude_name_list(photo_sys_2_value) {

        $('.magnitude_name').prop('hidden', true);

        if (photo_sys_2_value === 'GAIADR2_TMASS') {

            $('#id_magnitude_name option[value="gaia_g"]').prop({'hidden': false, 'selected': true});
            $('#id_magnitude_name option[value="gaia_gbp"]').prop('hidden', false);
            $('#id_magnitude_name option[value="gaia_grp"]').prop('hidden', false);
            $('#id_magnitude_name option[value="tmass_j"]').prop('hidden', false);
            $('#id_magnitude_name option[value="tmass_h"]').prop('hidden', false);
            $('#id_magnitude_name option[value="tmass_ks"]').prop('hidden', false);

        } else if (photo_sys_2_value === 'WISE') {

            $('#id_magnitude_name option[value="wise_w1"]').prop({'hidden': false, 'selected': true});
            $('#id_magnitude_name option[value="wise_w2"]').prop('hidden', false);
            $('#id_magnitude_name option[value="wise_w3"]').prop('hidden', false);
            $('#id_magnitude_name option[value="wise_w4"]').prop('hidden', false);

        } else if (photo_sys_2_value === 'SPITZER') {

            $('#id_magnitude_name option[value="irac_3.6"]').prop({'hidden': false, 'selected': true});
            $('#id_magnitude_name option[value="irac_4.5"]').prop('hidden', false);
            $('#id_magnitude_name option[value="irac_5.8"]').prop('hidden', false);
            $('#id_magnitude_name option[value="irac_8.0"]').prop('hidden', false);
            $('#id_magnitude_name option[value="mips_24"]').prop('hidden', false);
            $('#id_magnitude_name option[value="mips_70"]').prop('hidden', false);
            $('#id_magnitude_name option[value="mips_160"]').prop('hidden', false);

        } else if (photo_sys_2_value === 'KEPLER') {

            $('#id_magnitude_name option[value="tess_te"]').prop({'hidden': false, 'selected': true});
            $('#id_magnitude_name option[value="kepler_ke"]').prop('hidden', false);
            $('#id_magnitude_name option[value="sdss_g"]').prop('hidden', false);
            $('#id_magnitude_name option[value="sdss_r"]').prop('hidden', false);
            $('#id_magnitude_name option[value="sdss_i"]').prop('hidden', false);
            $('#id_magnitude_name option[value="sdss_z"]').prop('hidden', false);
            $('#id_magnitude_name option[value="kepler_ddo51"]').prop('hidden', false);

        } else if (photo_sys_2_value === 'PANSTARR 1') {

            // PANSTARR 1
            $('#id_magnitude_name option[value="pans1_g"]').prop({'hidden': false, 'selected': true});
            $('#id_magnitude_name option[value="pans1_r"]').prop('hidden', false);
            $('#id_magnitude_name option[value="pans1_i"]').prop('hidden', false);
            $('#id_magnitude_name option[value="pans1_z"]').prop('hidden', false);
            $('#id_magnitude_name option[value="pans1_y"]').prop('hidden', false);
            $('#id_magnitude_name option[value="pans1_w"]').prop('hidden', false);

        } else if (photo_sys_2_value === 'UBV') {

            // UBV
            $('#id_magnitude_name option[value="ubv_u"]').prop({'hidden': false, 'selected': true});
            $('#id_magnitude_name option[value="ubv_b"]').prop('hidden', false);
            $('#id_magnitude_name option[value="ubv_v"]').prop('hidden', false);
            $('#id_magnitude_name option[value="ubv_r"]').prop('hidden', false);
            $('#id_magnitude_name option[value="ubv_i"]').prop('hidden', false);
            $('#id_magnitude_name option[value="ubv_j"]').prop('hidden', false);
            $('#id_magnitude_name option[value="ubv_h"]').prop('hidden', false);
            $('#id_magnitude_name option[value="ubv_k"]').prop('hidden', false);

        } else if (photo_sys_2_value === 'STROEMGREN') {

            // STROEMGREN
            $('#id_magnitude_name option[value="stroemgren_v1"]').prop({'hidden': false, 'selected': true});
            $('#id_magnitude_name option[value="stroemgren_u"]').prop('hidden', false);
            $('#id_magnitude_name option[value="stroemgren_v"]').prop('hidden', false);
            $('#id_magnitude_name option[value="stroemgren_b"]').prop('hidden', false);
            $('#id_magnitude_name option[value="stroemgren_y"]').prop('hidden', false);
            $('#id_magnitude_name option[value="stroemgren_hb_w"]').prop('hidden', false);
            $('#id_magnitude_name option[value="stroemgren_hb_n"]').prop('hidden', false);

        } else if (photo_sys_2_value === 'DENIS') {

            // DENIS
            $('#id_magnitude_name option[value="denis_i"]').prop({'hidden': false, 'selected': true});
            $('#id_magnitude_name option[value="denis_j"]').prop('hidden', false);
            $('#id_magnitude_name option[value="denis_ks"]').prop('hidden', false);

        } else if (photo_sys_2_value === 'TYCHO2') {

            // TYCHO2
            $('#id_magnitude_name option[value="tycho_bt"]').prop({'hidden': false, 'selected': true});
            $('#id_magnitude_name option[value="tycho_vt"]').prop('hidden', false);
        }

        // if (photo_sys_2_value === 'GAIADR2_TMASS');
        // {
        //     $('#id_magnitude_name option[value="gaia_g"]').prop({'hidden': false, 'selected': true});
        //     $('#id_magnitude_name option[value="gaia_gbp"]').prop({'hidden': false});
        //     $('#id_magnitude_name option[value="gaia_grp"]').prop({'hidden': false});
        //     $('#id_magnitude_name option[value="tmass_j"]').prop({'hidden': false});
        //     $('#id_magnitude_name option[value="tmass_h"]').prop({'hidden': false});
        //     $('#id_magnitude_name option[value="tmass_ks"]').prop({'hidden': false});
        //
        //     $('#id_magnitude_name option[value="wise_w1"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="wise_w2"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="wise_w3"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="wise_w4"]').prop('hidden', true);
        //
        //     $('#id_magnitude_name option[value="irac_3.6"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="irac_4.5"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="irac_5.8"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="irac_8.0"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="mips_24"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="mips_70"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="mips_160"]').prop('hidden', true);
        //
        //     $('#id_magnitude_name option[value="tess_te"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="kepler_ke"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="sdss_g"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="sdss_r"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="sdss_i"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="sdss_z"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="kepler_ddo51"]').prop('hidden', true);
        //
        //     $('#id_magnitude_name option[value="pans1_g"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_r"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_i"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_z"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_y"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_w"]').prop('hidden', true);
        //
        //     $('#id_magnitude_name option[value="ubv_u"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_b"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_v"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_r"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_i"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_j"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_h"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_k"]').prop('hidden', true);
        //
        //     $('#id_magnitude_name option[value="stroemgren_v1"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_u"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_v"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_b"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_y"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_hb_w"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_hb_n"]').prop('hidden', true);
        //
        //     $('#id_magnitude_name option[value="denis_i"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="denis_j"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="denis_ks"]').prop('hidden', true);
        //
        //     $('#id_magnitude_name option[value="tycho_bt"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="tycho_vt"]').prop('hidden', true);
        // }
        // else if(photo_sys_2_value === 'WISE'){
        //
        //     $('#id_magnitude_name option[value="gaia_g"]').prop({'hidden': true});
        //     $('#id_magnitude_name option[value="gaia_gbp"]').prop({'hidden': true});
        //     $('#id_magnitude_name option[value="gaia_grp"]').prop({'hidden': true});
        //     $('#id_magnitude_name option[value="tmass_j"]').prop({'hidden': true});
        //     $('#id_magnitude_name option[value="tmass_h"]').prop({'hidden': true});
        //     $('#id_magnitude_name option[value="tmass_ks"]').prop({'hidden': true});
        //
        //     $('#id_magnitude_name option[value="wise_w1"]').prop({'hidden': false, 'selected': true});
        //     $('#id_magnitude_name option[value="wise_w2"]').prop('hidden', false);
        //     $('#id_magnitude_name option[value="wise_w3"]').prop('hidden', false);
        //     $('#id_magnitude_name option[value="wise_w4"]').prop('hidden', false);
        //
        //     $('#id_magnitude_name option[value="irac_3.6"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="irac_4.5"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="irac_5.8"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="irac_8.0"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="mips_24"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="mips_70"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="mips_160"]').prop('hidden', true);
        //
        //     $('#id_magnitude_name option[value="tess_te"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="kepler_ke"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="sdss_g"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="sdss_r"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="sdss_i"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="sdss_z"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="kepler_ddo51"]').prop('hidden', true);
        //
        //     $('#id_magnitude_name option[value="pans1_g"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_r"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_i"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_z"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_y"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_w"]').prop('hidden', true);
        //
        //     $('#id_magnitude_name option[value="ubv_u"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_b"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_v"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_r"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_i"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_j"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_h"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_k"]').prop('hidden', true);
        //
        //     $('#id_magnitude_name option[value="stroemgren_v1"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_u"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_v"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_b"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_y"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_hb_w"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_hb_n"]').prop('hidden', true);
        //
        //     $('#id_magnitude_name option[value="denis_i"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="denis_j"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="denis_ks"]').prop('hidden', true);
        //
        //     $('#id_magnitude_name option[value="tycho_bt"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="tycho_vt"]').prop('hidden', true);
        // }
        // else if(photo_sys_2_value === 'SPITZER'){
        //
        //     $('#id_magnitude_name option[value="gaia_g"]').prop({'hidden': true});
        //     $('#id_magnitude_name option[value="gaia_gbp"]').prop({'hidden': true});
        //     $('#id_magnitude_name option[value="gaia_grp"]').prop({'hidden': true});
        //     $('#id_magnitude_name option[value="tmass_j"]').prop({'hidden': true});
        //     $('#id_magnitude_name option[value="tmass_h"]').prop({'hidden': true});
        //     $('#id_magnitude_name option[value="tmass_ks"]').prop({'hidden': true});
        //
        //     $('#id_magnitude_name option[value="wise_w1"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="wise_w2"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="wise_w3"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="wise_w4"]').prop('hidden', true);
        //
        //     $('#id_magnitude_name option[value="irac_3.6"]').prop({'hidden': false, 'selected': true});
        //     $('#id_magnitude_name option[value="irac_4.5"]').prop('hidden', false);
        //     $('#id_magnitude_name option[value="irac_5.8"]').prop('hidden', false);
        //     $('#id_magnitude_name option[value="irac_8.0"]').prop('hidden', false);
        //     $('#id_magnitude_name option[value="mips_24"]').prop('hidden', false);
        //     $('#id_magnitude_name option[value="mips_70"]').prop('hidden', false);
        //     $('#id_magnitude_name option[value="mips_160"]').prop('hidden', false);
        //
        //     $('#id_magnitude_name option[value="tess_te"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="kepler_ke"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="sdss_g"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="sdss_r"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="sdss_i"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="sdss_z"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="kepler_ddo51"]').prop('hidden', true);
        //
        //     $('#id_magnitude_name option[value="pans1_g"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_r"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_i"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_z"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_y"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_w"]').prop('hidden', true);
        //
        //     $('#id_magnitude_name option[value="ubv_u"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_b"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_v"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_r"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_i"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_j"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_h"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_k"]').prop('hidden', true);
        //
        //     $('#id_magnitude_name option[value="stroemgren_v1"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_u"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_v"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_b"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_y"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_hb_w"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_hb_n"]').prop('hidden', true);
        //
        //     $('#id_magnitude_name option[value="denis_i"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="denis_j"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="denis_ks"]').prop('hidden', true);
        //
        //     $('#id_magnitude_name option[value="tycho_bt"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="tycho_vt"]').prop('hidden', true);
        // }
        // else if(photo_sys_2_value === 'KEPLER'){
        //
        //     $('#id_magnitude_name option[value="gaia_g"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="gaia_gbp"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="gaia_grp"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="tmass_j"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="tmass_h"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="tmass_ks"]').prop('hidden', true);
        //
        //     $('#id_magnitude_name option[value="wise_w1"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="wise_w2"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="wise_w3"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="wise_w4"]').prop('hidden', true);
        //
        //     $('#id_magnitude_name option[value="irac_3.6"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="irac_4.5"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="irac_5.8"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="irac_8.0"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="mips_24"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="mips_70"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="mips_160"]').prop('hidden', true);
        //
        //     $('#id_magnitude_name option[value="tess_te"]').prop({'hidden': false, 'selected': true});
        //     $('#id_magnitude_name option[value="kepler_ke"]').prop('hidden', false);
        //     $('#id_magnitude_name option[value="sdss_g"]').prop('hidden', false);
        //     $('#id_magnitude_name option[value="sdss_r"]').prop('hidden', false);
        //     $('#id_magnitude_name option[value="sdss_i"]').prop('hidden', false);
        //     $('#id_magnitude_name option[value="sdss_z"]').prop('hidden', false);
        //     $('#id_magnitude_name option[value="kepler_ddo51"]').prop('hidden', false);
        //
        //     $('#id_magnitude_name option[value="pans1_g"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_r"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_i"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_z"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_y"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_w"]').prop('hidden', true);
        //
        //     $('#id_magnitude_name option[value="ubv_u"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_b"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_v"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_r"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_i"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_j"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_h"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_k"]').prop('hidden', true);
        //
        //     $('#id_magnitude_name option[value="stroemgren_v1"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_u"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_v"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_b"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_y"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_hb_w"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_hb_n"]').prop('hidden', true);
        //
        //     $('#id_magnitude_name option[value="denis_i"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="denis_j"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="denis_ks"]').prop('hidden', true);
        //
        //     $('#id_magnitude_name option[value="tycho_bt"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="tycho_vt"]').prop('hidden', true);
        // }
        // else if(photo_sys_2_value === 'PANSTARR 1'){
        //
        //     // GAIADR2_TMASS
        //     $('#id_magnitude_name option[value="gaia_g"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="gaia_gbp"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="gaia_grp"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="tmass_j"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="tmass_h"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="tmass_ks"]').prop('hidden', true);
        //
        //     // WISE
        //     $('#id_magnitude_name option[value="wise_w1"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="wise_w2"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="wise_w3"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="wise_w4"]').prop('hidden', true);
        //
        //     // SPITZER
        //     $('#id_magnitude_name option[value="irac_3.6"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="irac_4.5"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="irac_5.8"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="irac_8.0"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="mips_24"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="mips_70"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="mips_160"]').prop('hidden', true);
        //
        //     // KEPLER
        //     $('#id_magnitude_name option[value="tess_te"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="kepler_ke"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="sdss_g"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="sdss_r"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="sdss_i"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="sdss_z"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="kepler_ddo51"]').prop('hidden', true);
        //
        //     // PANSTARR 1
        //     $('#id_magnitude_name option[value="pans1_g"]').prop({'hidden': false, 'selected': true});
        //     $('#id_magnitude_name option[value="pans1_r"]').prop('hidden', false);
        //     $('#id_magnitude_name option[value="pans1_i"]').prop('hidden', false);
        //     $('#id_magnitude_name option[value="pans1_z"]').prop('hidden', false);
        //     $('#id_magnitude_name option[value="pans1_y"]').prop('hidden', false);
        //     $('#id_magnitude_name option[value="pans1_w"]').prop('hidden', false);
        //
        //     // UBV
        //     $('#id_magnitude_name option[value="ubv_u"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_b"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_v"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_r"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_i"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_j"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_h"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_k"]').prop('hidden', true);
        //
        //     // STROEMGREN
        //     $('#id_magnitude_name option[value="stroemgren_v1"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_u"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_v"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_b"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_y"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_hb_w"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_hb_n"]').prop('hidden', true);
        //
        //     // DENIS
        //     $('#id_magnitude_name option[value="denis_i"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="denis_j"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="denis_ks"]').prop('hidden', true);
        //
        //     // TYCHO2
        //     $('#id_magnitude_name option[value="tycho_bt"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="tycho_vt"]').prop('hidden', true);
        // }
        // else if(photo_sys_2_value === 'UBV'){
        //
        //     // GAIADR2_TMASS
        //     $('#id_magnitude_name option[value="gaia_g"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="gaia_gbp"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="gaia_grp"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="tmass_j"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="tmass_h"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="tmass_ks"]').prop('hidden', true);
        //
        //     // WISE
        //     $('#id_magnitude_name option[value="wise_w1"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="wise_w2"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="wise_w3"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="wise_w4"]').prop('hidden', true);
        //
        //     // SPITZER
        //     $('#id_magnitude_name option[value="irac_3.6"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="irac_4.5"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="irac_5.8"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="irac_8.0"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="mips_24"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="mips_70"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="mips_160"]').prop('hidden', true);
        //
        //     // KEPLER
        //     $('#id_magnitude_name option[value="tess_te"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="kepler_ke"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="sdss_g"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="sdss_r"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="sdss_i"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="sdss_z"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="kepler_ddo51"]').prop('hidden', true);
        //
        //     // PANSTARR 1
        //     $('#id_magnitude_name option[value="pans1_g"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_r"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_i"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_z"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_y"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_w"]').prop('hidden', true);
        //
        //     // UBV
        //     $('#id_magnitude_name option[value="ubv_u"]').prop({'hidden': false, 'selected': true});
        //     $('#id_magnitude_name option[value="ubv_b"]').prop('hidden', false);
        //     $('#id_magnitude_name option[value="ubv_v"]').prop('hidden', false);
        //     $('#id_magnitude_name option[value="ubv_r"]').prop('hidden', false);
        //     $('#id_magnitude_name option[value="ubv_i"]').prop('hidden', false);
        //     $('#id_magnitude_name option[value="ubv_j"]').prop('hidden', false);
        //     $('#id_magnitude_name option[value="ubv_h"]').prop('hidden', false);
        //     $('#id_magnitude_name option[value="ubv_k"]').prop('hidden', false);
        //
        //     // STROEMGREN
        //     $('#id_magnitude_name option[value="stroemgren_v1"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_u"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_v"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_b"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_y"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_hb_w"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_hb_n"]').prop('hidden', true);
        //
        //     // DENIS
        //     $('#id_magnitude_name option[value="denis_i"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="denis_j"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="denis_ks"]').prop('hidden', true);
        //
        //     // TYCHO2
        //     $('#id_magnitude_name option[value="tycho_bt"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="tycho_vt"]').prop('hidden', true);
        // }
        // else if(photo_sys_2_value === 'STROEMGREN'){
        //
        //     // GAIADR2_TMASS
        //     $('#id_magnitude_name option[value="gaia_g"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="gaia_gbp"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="gaia_grp"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="tmass_j"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="tmass_h"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="tmass_ks"]').prop('hidden', true);
        //
        //     // WISE
        //     $('#id_magnitude_name option[value="wise_w1"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="wise_w2"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="wise_w3"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="wise_w4"]').prop('hidden', true);
        //
        //     // SPITZER
        //     $('#id_magnitude_name option[value="irac_3.6"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="irac_4.5"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="irac_5.8"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="irac_8.0"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="mips_24"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="mips_70"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="mips_160"]').prop('hidden', true);
        //
        //     // KEPLER
        //     $('#id_magnitude_name option[value="tess_te"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="kepler_ke"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="sdss_g"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="sdss_r"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="sdss_i"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="sdss_z"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="kepler_ddo51"]').prop('hidden', true);
        //
        //     // PANSTARR 1
        //     $('#id_magnitude_name option[value="pans1_g"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_r"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_i"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_z"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_y"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_w"]').prop('hidden', true);
        //
        //     // UBV
        //     $('#id_magnitude_name option[value="ubv_u"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_b"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_v"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_r"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_i"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_j"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_h"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_k"]').prop('hidden', true);
        //
        //     // STROEMGREN
        //     $('#id_magnitude_name option[value="stroemgren_v1"]').prop({'hidden': false, 'selected': true});
        //     $('#id_magnitude_name option[value="stroemgren_u"]').prop('hidden', false);
        //     $('#id_magnitude_name option[value="stroemgren_v"]').prop('hidden', false);
        //     $('#id_magnitude_name option[value="stroemgren_b"]').prop('hidden', false);
        //     $('#id_magnitude_name option[value="stroemgren_y"]').prop('hidden', false);
        //     $('#id_magnitude_name option[value="stroemgren_hb_w"]').prop('hidden', false);
        //     $('#id_magnitude_name option[value="stroemgren_hb_n"]').prop('hidden', false);
        //
        //     // DENIS
        //     $('#id_magnitude_name option[value="denis_i"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="denis_j"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="denis_ks"]').prop('hidden', true);
        //
        //     // TYCHO2
        //     $('#id_magnitude_name option[value="tycho_bt"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="tycho_vt"]').prop('hidden', true);
        // }
        // else if(photo_sys_2_value === 'DENIS'){
        //
        //     // GAIADR2_TMASS
        //     $('#id_magnitude_name option[value="gaia_g"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="gaia_gbp"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="gaia_grp"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="tmass_j"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="tmass_h"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="tmass_ks"]').prop('hidden', true);
        //
        //     // WISE
        //     $('#id_magnitude_name option[value="wise_w1"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="wise_w2"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="wise_w3"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="wise_w4"]').prop('hidden', true);
        //
        //     // SPITZER
        //     $('#id_magnitude_name option[value="irac_3.6"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="irac_4.5"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="irac_5.8"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="irac_8.0"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="mips_24"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="mips_70"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="mips_160"]').prop('hidden', true);
        //
        //     // KEPLER
        //     $('#id_magnitude_name option[value="tess_te"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="kepler_ke"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="sdss_g"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="sdss_r"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="sdss_i"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="sdss_z"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="kepler_ddo51"]').prop('hidden', true);
        //
        //     // PANSTARR 1
        //     $('#id_magnitude_name option[value="pans1_g"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_r"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_i"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_z"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_y"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_w"]').prop('hidden', true);
        //
        //     // UBV
        //     $('#id_magnitude_name option[value="ubv_u"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_b"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_v"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_r"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_i"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_j"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_h"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_k"]').prop('hidden', true);
        //
        //     // STROEMGREN
        //     $('#id_magnitude_name option[value="stroemgren_v1"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_u"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_v"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_b"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_y"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_hb_w"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_hb_n"]').prop('hidden', true);
        //
        //     // DENIS
        //     $('#id_magnitude_name option[value="denis_i"]').prop({'hidden': false, 'selected': true});
        //     $('#id_magnitude_name option[value="denis_j"]').prop('hidden', false);
        //     $('#id_magnitude_name option[value="denis_ks"]').prop('hidden', false);
        //
        //     // TYCHO2
        //     $('#id_magnitude_name option[value="tycho_bt"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="tycho_vt"]').prop('hidden', true);
        // }
        // else if(photo_sys_2_value === 'TYCHO2'){
        //
        //     // GAIADR2_TMASS
        //     $('#id_magnitude_name option[value="gaia_g"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="gaia_gbp"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="gaia_grp"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="tmass_j"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="tmass_h"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="tmass_ks"]').prop('hidden', true);
        //
        //     // WISE
        //     $('#id_magnitude_name option[value="wise_w1"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="wise_w2"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="wise_w3"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="wise_w4"]').prop('hidden', true);
        //
        //     // SPITZER
        //     $('#id_magnitude_name option[value="irac_3.6"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="irac_4.5"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="irac_5.8"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="irac_8.0"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="mips_24"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="mips_70"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="mips_160"]').prop('hidden', true);
        //
        //     // KEPLER
        //     $('#id_magnitude_name option[value="tess_te"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="kepler_ke"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="sdss_g"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="sdss_r"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="sdss_i"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="sdss_z"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="kepler_ddo51"]').prop('hidden', true);
        //
        //     // PANSTARR 1
        //     $('#id_magnitude_name option[value="pans1_g"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_r"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_i"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_z"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_y"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="pans1_w"]').prop('hidden', true);
        //
        //     // UBV
        //     $('#id_magnitude_name option[value="ubv_u"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_b"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_v"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_r"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_i"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_j"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_h"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="ubv_k"]').prop('hidden', true);
        //
        //     // STROEMGREN
        //     $('#id_magnitude_name option[value="stroemgren_v1"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_u"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_v"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_b"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_y"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_hb_w"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="stroemgren_hb_n"]').prop('hidden', true);
        //
        //     // DENIS
        //     $('#id_magnitude_name option[value="denis_i"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="denis_j"]').prop('hidden', true);
        //     $('#id_magnitude_name option[value="denis_ks"]').prop('hidden', true);
        //
        //     // TYCHO2
        //     $('#id_magnitude_name option[value="tycho_bt"]').prop({'hidden': false, 'selected': true});
        //     $('#id_magnitude_name option[value="tycho_vt"]').prop('hidden', false);
        // }

    }

    function update_blue_color_band_list(photo_sys_2_value) {

        $('.magnitude_name_1').prop('hidden', true);

        if (photo_sys_2_value === 'GAIADR2_TMASS') {

            $('#id_magnitude_name_1 option[value="gaia_g"]').prop({'hidden': false, 'selected': true});
            $('#id_magnitude_name_1 option[value="gaia_gbp"]').prop('hidden', false);
            $('#id_magnitude_name_1 option[value="gaia_grp"]').prop('hidden', false);
            $('#id_magnitude_name_1 option[value="tmass_j"]').prop('hidden', false);
            $('#id_magnitude_name_1 option[value="tmass_h"]').prop('hidden', false);
            $('#id_magnitude_name_1 option[value="tmass_ks"]').prop('hidden', false);

        } else if (photo_sys_2_value === 'WISE') {

            $('#id_magnitude_name_1 option[value="wise_w1"]').prop({'hidden': false, 'selected': true});
            $('#id_magnitude_name_1 option[value="wise_w2"]').prop('hidden', false);
            $('#id_magnitude_name_1 option[value="wise_w3"]').prop('hidden', false);
            $('#id_magnitude_name_1 option[value="wise_w4"]').prop('hidden', false);

        } else if (photo_sys_2_value === 'SPITZER') {

            $('#id_magnitude_name_1 option[value="irac_3.6"]').prop({'hidden': false, 'selected': true});
            $('#id_magnitude_name_1 option[value="irac_4.5"]').prop('hidden', false);
            $('#id_magnitude_name_1 option[value="irac_5.8"]').prop('hidden', false);
            $('#id_magnitude_name_1 option[value="irac_8.0"]').prop('hidden', false);
            $('#id_magnitude_name_1 option[value="mips_24"]').prop('hidden', false);
            $('#id_magnitude_name_1 option[value="mips_70"]').prop('hidden', false);
            $('#id_magnitude_name_1 option[value="mips_160"]').prop('hidden', false);

        } else if (photo_sys_2_value === 'KEPLER') {

            $('#id_magnitude_name_1 option[value="tess_te"]').prop({'hidden': false, 'selected': true});
            $('#id_magnitude_name_1 option[value="kepler_ke"]').prop('hidden', false);
            $('#id_magnitude_name_1 option[value="sdss_g"]').prop('hidden', false);
            $('#id_magnitude_name_1 option[value="sdss_r"]').prop('hidden', false);
            $('#id_magnitude_name_1 option[value="sdss_i"]').prop('hidden', false);
            $('#id_magnitude_name_1 option[value="sdss_z"]').prop('hidden', false);
            $('#id_magnitude_name_1 option[value="kepler_ddo51"]').prop('hidden', false);

        } else if (photo_sys_2_value === 'PANSTARR 1') {

            // PANSTARR 1
            $('#id_magnitude_name_1 option[value="pans1_g"]').prop({'hidden': false, 'selected': true});
            $('#id_magnitude_name_1 option[value="pans1_r"]').prop('hidden', false);
            $('#id_magnitude_name_1 option[value="pans1_i"]').prop('hidden', false);
            $('#id_magnitude_name_1 option[value="pans1_z"]').prop('hidden', false);
            $('#id_magnitude_name_1 option[value="pans1_y"]').prop('hidden', false);
            $('#id_magnitude_name_1 option[value="pans1_w"]').prop('hidden', false);

        } else if (photo_sys_2_value === 'UBV') {

            // UBV
            $('#id_magnitude_name_1 option[value="ubv_u"]').prop({'hidden': false, 'selected': true});
            $('#id_magnitude_name_1 option[value="ubv_b"]').prop('hidden', false);
            $('#id_magnitude_name_1 option[value="ubv_v"]').prop('hidden', false);
            $('#id_magnitude_name_1 option[value="ubv_r"]').prop('hidden', false);
            $('#id_magnitude_name_1 option[value="ubv_i"]').prop('hidden', false);
            $('#id_magnitude_name_1 option[value="ubv_j"]').prop('hidden', false);
            $('#id_magnitude_name_1 option[value="ubv_h"]').prop('hidden', false);
            $('#id_magnitude_name_1 option[value="ubv_k"]').prop('hidden', false);

        } else if (photo_sys_2_value === 'STROEMGREN') {

            // STROEMGREN
            $('#id_magnitude_name_1 option[value="stroemgren_v1"]').prop({'hidden': false, 'selected': true});
            $('#id_magnitude_name_1 option[value="stroemgren_u"]').prop('hidden', false);
            $('#id_magnitude_name_1 option[value="stroemgren_v"]').prop('hidden', false);
            $('#id_magnitude_name_1 option[value="stroemgren_b"]').prop('hidden', false);
            $('#id_magnitude_name_1 option[value="stroemgren_y"]').prop('hidden', false);
            $('#id_magnitude_name_1 option[value="stroemgren_hb_w"]').prop('hidden', false);
            $('#id_magnitude_name_1 option[value="stroemgren_hb_n"]').prop('hidden', false);

        } else if (photo_sys_2_value === 'DENIS') {

            // DENIS
            $('#id_magnitude_name_1 option[value="denis_i"]').prop({'hidden': false, 'selected': true});
            $('#id_magnitude_name_1 option[value="denis_j"]').prop('hidden', false);
            $('#id_magnitude_name_1 option[value="denis_ks"]').prop('hidden', false);

        } else if (photo_sys_2_value === 'TYCHO2') {

            // TYCHO2
            $('#id_magnitude_name_1 option[value="tycho_bt"]').prop({'hidden': false, 'selected': true});
            $('#id_magnitude_name_1 option[value="tycho_vt"]').prop('hidden', false);
        }
    }

    function update_red_color_band_list(photo_sys_2_value) {

        $('.magnitude_name_2').prop('hidden', true);

        if (photo_sys_2_value === 'GAIADR2_TMASS') {

            $('#id_magnitude_name_2 option[value="gaia_g"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="gaia_gbp"]').prop({'hidden': false, 'selected': true});
            $('#id_magnitude_name_2 option[value="gaia_grp"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="tmass_j"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="tmass_h"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="tmass_ks"]').prop('hidden', false);

        } else if (photo_sys_2_value === 'WISE') {

            $('#id_magnitude_name_2 option[value="wise_w1"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="wise_w2"]').prop({'hidden': false, 'selected': true});
            $('#id_magnitude_name_2 option[value="wise_w3"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="wise_w4"]').prop('hidden', false);

        } else if (photo_sys_2_value === 'SPITZER') {

            $('#id_magnitude_name_2 option[value="irac_3.6"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="irac_4.5"]').prop({'hidden': false, 'selected': true});
            $('#id_magnitude_name_2 option[value="irac_5.8"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="irac_8.0"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="mips_24"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="mips_70"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="mips_160"]').prop('hidden', false);

        } else if (photo_sys_2_value === 'KEPLER') {

            $('#id_magnitude_name_2 option[value="tess_te"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="kepler_ke"]').prop({'hidden': false, 'selected': true});
            $('#id_magnitude_name_2 option[value="sdss_g"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="sdss_r"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="sdss_i"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="sdss_z"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="kepler_ddo51"]').prop('hidden', false);

        } else if (photo_sys_2_value === 'PANSTARR 1') {

            // PANSTARR 1
            $('#id_magnitude_name_2 option[value="pans1_g"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="pans1_r"]').prop({'hidden': false, 'selected': true});
            $('#id_magnitude_name_2 option[value="pans1_i"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="pans1_z"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="pans1_y"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="pans1_w"]').prop('hidden', false);

        } else if (photo_sys_2_value === 'UBV') {

            // UBV
            $('#id_magnitude_name_2 option[value="ubv_u"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="ubv_b"]').prop({'hidden': false, 'selected': true});
            $('#id_magnitude_name_2 option[value="ubv_v"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="ubv_r"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="ubv_i"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="ubv_j"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="ubv_h"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="ubv_k"]').prop('hidden', false);

        } else if (photo_sys_2_value === 'STROEMGREN') {

            // STROEMGREN
            $('#id_magnitude_name_2 option[value="stroemgren_v1"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="stroemgren_u"]').prop({'hidden': false, 'selected': true});
            $('#id_magnitude_name_2 option[value="stroemgren_v"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="stroemgren_b"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="stroemgren_y"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="stroemgren_hb_w"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="stroemgren_hb_n"]').prop('hidden', false);

        } else if (photo_sys_2_value === 'DENIS') {

            // DENIS
            $('#id_magnitude_name_2 option[value="denis_i"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="denis_j"]').prop({'hidden': false, 'selected': true});
            $('#id_magnitude_name_2 option[value="denis_ks"]').prop('hidden', false);

        } else if (photo_sys_2_value === 'TYCHO2') {

            // TYCHO2
            $('#id_magnitude_name_2 option[value="tycho_bt"]').prop('hidden', false);
            $('#id_magnitude_name_2 option[value="tycho_vt"]').prop({'hidden': false, 'selected': true});
        }
    }
    function update_all_sky_and_circular_patch(){
        $('#id_longitude').prop('hidden', true);
        $('#id_latitude').prop('hidden', true);

        let survey_geometry = $('#id_geometry_options').find(":selected").text();

        if (survey_geometry === "Circular Patch" ) {
            $('#id_longitude').prop('hidden', false);
            $('#id_latitude').prop('hidden', false);
            $('#id_survey_area').prop('hidden', false);
            $('label[for="id_longitude"]').prop('hidden', false);
            $('label[for="id_latitude"]').prop('hidden', false);
            $('label[for="id_survey_area"]').prop('hidden', false);

        }
        else {
            $('#id_longitude').prop('hidden', true);
            $('#id_latitude').prop('hidden', true);
            $('#id_survey_area').prop('hidden', true);
            $('label[for="id_longitude"]').prop('hidden', true);
            $('label[for="id_latitude"]').prop('hidden', true);
            $('label[for="id_survey_area"]').prop('hidden', true);

        }

    }
});