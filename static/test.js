 $('input').change(function (e) {

        var testno = $(e.target).attr('data-no');
        var correct_answer = $('[name=test'+testno+'_result]').val();
        var current_answer = $(e.target).val();
        if( correct_answer == current_answer)
        {
        $('[data-test='+testno+']').removeClass('allwhite');
        $('#gal'+testno).show();
        $('#cr'+testno).hide();
        }
        else
        {
        $('[data-test='+testno+']').addClass('allwhite');
        $('#gal'+testno).hide();
        $('#cr'+testno).show();
        }

        var wrongAnswers = $('.allwhite').length
        if(wrongAnswers==0)
        {
           $('#imgtable').removeClass('theme-table');
           $('#imgtable').addClass('theme-wintable');
           $('#wintext').show();
        }
        else
        {
           $('#imgtable').removeClass('theme-wintable');
           $('#imgtable').addClass('theme-table');
           $('#wintext').hide();
        }


});