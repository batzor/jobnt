$(document).ready(function(){
  $('#search-form').on('submit', function(event){
    event.preventDefault();
    console.log('form submitted!');
    $.ajax({
      url: 'search/',
      type: 'GET',
      data: $('#search-form').serialize(),

      success: function(data){
        $('#joboffers').html(data);
      },

      error: function(){
      }
    });

  });
});