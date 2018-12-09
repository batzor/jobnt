$(document).ready(function(){
  show_offers();
  $('#search-form').on('submit', function(event) {
    event.preventDefault();
    console.log('form submitted!');
    show_offers();
  });
});