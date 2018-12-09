function show_offers(){
  $.ajax({
    url: 'search/',
    type: 'GET',
    data: $('#search-form').serialize(),
    success: function(data) {
      $('#joboffers').html(data);
      update_sub_listeners();
    },
    error: function() { }
  });
}

function subscribe(event) {
  target = $(event.target);
  method = target.data('method')
  url = {
          'sub': '/catalog/add_sub/',
          'unsub': '/catalog/rem_sub/'
        }[method]
  company_id = target.data("company-id")
  company_name = target.data("company-name")
  
  all_company_btns = $(`[data-company-id=${company_id}]`)

  all_company_btns.prop('disabled', true)

  $.ajax({
    url: url,
    type: 'GET',
    data: {'company_id': company_id},
    success: function(data){
      console.log("[ajax success] " + data);


      // Change button look
      if (method == 'sub') {
        all_company_btns.html('Unsubscribe from ' + company_name)
      } else {
        all_company_btns.html('Subscribe to ' + company_name)
      }

      // Change button data
      new_method = (method == 'sub' ?'unsub' :'sub')
      all_company_btns.data('method', new_method)

      all_company_btns.prop('disabled', false)
    },
    error: function() {}
  });
}

function update_sub_listeners() {
  $('.subscribe').on('click', subscribe)
}