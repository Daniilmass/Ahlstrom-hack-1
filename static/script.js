$(document).ready(function() {
    $('.issue_table tr').click(function() {
        $(location).attr('href',  location.href +'edit/'+ $(this).prop('id'));
    });
});