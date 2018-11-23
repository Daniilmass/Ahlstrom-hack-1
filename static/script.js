$(document).ready(function() {
    $('.data_table tr').click(function() {
        $(location).attr('href',  location.href +'#');//+ $(this).prop('id'));//
    });
    $('#add_button').click(function() {
        $(location).attr('href',  location.href +'add/');
    });
    $('#send_issue').click(function() {
        var injury = $('#injury').is(':checked');
        var fixed = $('#fixed').is(':checked');
        var select_machine = $('#select_machine').val();
        var select_parts = $('#select_parts option:selected').val();
        console.log(select_parts)
        console.log(injury,fixed,select_machine)
        $.ajax({
          url: location.href,
          type: "POST",
          data: JSON.stringify( {'injury':injury,
                 'fixed': fixed,
                 'machines':[select_machine],
                 'parts':select_parts}),
          dataType: 'json'
        });
        $('#issue_added').show()
    });
});

