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

function add_sub(company_id){
  $.ajax({
    url: 'catalog/add_sub/',
    type: 'GET',
    data: {'company_id': company_id},
    success: function(data){
      // $('#joboffers').html(data);
      console.log(data)
    },
    error: function() {}
  });
}

$(document).ready(function(){
  show_offers();
  $('#search-form').on('submit', function(event){
    event.preventDefault();
    console.log('form submitted!');
    show_offers();
  });

  // 
  $('.subscribe-to-company').on('click', function(event) {
    console.log($(event.target).data('company-id'))
    // add_sub($(event.target).data('company-id'))
  })
});