
$(document).ready(function() {

    // photo_sys_2 hide/show options on change.
    check_photo_sys_2_type();
    $('body').on('change', '#id_photo_sys_2',
        function() {
            check_photo_sys_2_type();
        });

    function check_photo_sys_2_type() {
        if ($('#id_photo_sys_2').find(":selected").text() == 'GAIADR2_TMASS')
        {

        }
        else{

        };
    }
});