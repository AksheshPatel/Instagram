
$('button').on('click',function (event) {
    event.preventDefault();
    var element = $(this);
    $.ajax({
        url : element.attr('data-id')+'/like',
        type : 'GET',
        data : {id : element.attr('data-id')},
        success : function (response) {
            element.html(' '+ response);
            
        }

    })
});
