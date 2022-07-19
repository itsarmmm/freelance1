$(document).ready(function() {
   $('input[type="radio"]').click(function() {
       if($(this).attr('id') == 'yur') {
            $('#inn').show();
            $('#inn').val('');
       }
       else {
            $('#inn').hide();
            $('#inn').val('none');
       }
   });
});