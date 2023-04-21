$(document).ready(function() {
  $('form').on('submit', function(event) {
    event.preventDefault();
    var spindle_speed = $('input#spindle_speed').val();
    var feed_rate = $('input#feed_rate').val();
    var depth_of_cut = $('input#depth_of_cut').val();
    $.ajax({
      url: '/predict',
      method: 'POST',
      data: {
        spindle_speed: spindle_speed,
        feed_rate: feed_rate,
        depth_of_cut: depth_of_cut
      },
      success: function(data) {
        $('p#prediction').text('The predicted surface roughness is: ' + data.prediction.toFixed(4));
      },
      error: function(xhr, status, error) {
        console.log(error);
      }
    });
  });
});
