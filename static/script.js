$(document).ready(function() {
    $('.data_table tr').click(function() {
        $(location).attr('href',  location.href +'edit/'+ $(this).prop('id'));
    });
    $('#add_button').click(function() {
        $(location).attr('href',  location.href +'add/');
    });
});