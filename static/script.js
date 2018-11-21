$(document).ready(function() {
    $('.issue_table tr').click(function() {
        // window.location.href = location.host +"";
        console.log(location.href +'edit/'+ $(this).prop('id'))
    });
});