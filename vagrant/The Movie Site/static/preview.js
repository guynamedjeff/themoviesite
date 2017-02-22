$(function() {
$('#preview').click(function() {
    $.ajax({
        url: '/previewNewMovie/',
        data: $('form').serialize(),
        type: 'POST',
        success: function(response) {
            var movie = JSON.parse(response);
            var trailer = movie.trailer.replace("watch?v=", "embed/");
            $('#preview-poster').attr("src", movie.poster)
            $('#trailer').attr("src", trailer)
            $('#preview-pane').show()
        },
        error: function(error) {
            console.log(error);
        }
    });
});
});
$(function() {
$('#submit').click(function() {
    $.ajax({
        url: '/addNewMovie/',
        data: $('form').serialize(),
        type: 'POST',
        success: function(response) {
            $('#movie-form').each(function(){
              this.reset();
            })
            $('#message').html("You have successfully added " + JSON.parse(response).name)
            $('#preview-pane').hide()
        },
        error: function(error) {
            console.log(error);
        }
    });
});
});