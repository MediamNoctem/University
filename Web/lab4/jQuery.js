$(document).ready(function() {
    $('#jQuery')
    $('.ball').on('click', function () {
        if ($(this).attr('class') === 'ball red') {
            if ($(this).parent().next().children().attr('class') === 'ball') {
                $(this).attr('class', 'ball');
                $(this).parent().next().children().attr('class', 'ball red');
            }
            else {
                if ($(this).parent().next().next().children().attr('class') === 'ball') {
                    $(this).attr('class', 'ball');
                    $(this).parent().next().next().children().attr('class', 'ball red');
                }
                else {
                    if ($(this).parent().next().children().attr('class') !== 'ball' && $(this).parent().next().next().children().attr('class') !== 'ball' && $(this).parent().prev().children().attr('class') === 'ball') {
                        $(this).attr('class', 'ball');
                        $(this).parent().prev().children().attr('class', 'ball red');
                    }
                }
            }
        }
        else {
            if ($(this).attr('class') === 'ball blue') {
                if ($(this).parent().prev().children().attr('class') === 'ball') {
                    $(this).attr('class', 'ball');
                    $(this).parent().prev().children().attr('class', 'ball blue');
                }
                else {
                    if ($(this).parent().prev().prev().children().attr('class') === 'ball') {
                        $(this).attr('class', 'ball');
                        $(this).parent().prev().prev().children().attr('class', 'ball blue');
                    }
                    else {
                        if ($(this).parent().prev().children().attr('class') !== 'ball' && $(this).parent().prev().prev().children().attr('class') !== 'ball' && $(this).parent().next().children().attr('class') === 'ball') {
                            $(this).attr('class', 'ball');
                            $(this).parent().next().children().attr('class', 'ball blue');
                        }
                    }
                }
            }
        }
    })
})
