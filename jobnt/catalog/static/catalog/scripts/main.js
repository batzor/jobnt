function show_offers(){
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
}

$(document).ready(function(){
  show_offers();
  $('#search-form').on('submit', function(event){
    event.preventDefault();
    console.log('form submitted!');
    show_offers();
  });
});