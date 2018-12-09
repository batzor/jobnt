function show_offers(){
  $.ajax({
    url: 'search/',
    type: 'GET',
    data: $('#search-form').serialize(),
    success: function(data) {
      $('#joboffers').html(data);
      update_sub_listeners()
      update_fav_listeners()
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
      console.log("[ajax sub; success] " + data);


      // Change button look
      if (method == 'sub') {
        all_company_btns.html('Unsubscribe from ' + company_name)
        all_company_btns.addClass('btn-outline-secondary')
        all_company_btns.removeClass('btn-secondary')
      } else {
        all_company_btns.html('Subscribe to ' + company_name)
        all_company_btns.addClass('btn-secondary')
        all_company_btns.removeClass('btn-outline-secondary')
      }

      // Change button data
      new_method = (method == 'sub' ?'unsub' :'sub')
      all_company_btns.data('method', new_method)

      all_company_btns.prop('disabled', false)
    },
    error: function() {}
  });
}

function favorite(event) {
  target = $(event.target);
  method = target.data('method')
  console.log(method)
  url = {
          'fav': '/catalog/add_fav/',
          'unfav': '/catalog/rem_fav/'
        }[method]
  offer_id = target.data("offer-id")

  target.prop('disabled', true)

  $.ajax({
    url: url,
    type: 'GET',
    data: {'offer_id': offer_id},
    success: function(data){
      console.log("[ajax fav; success] " + data);

      // Change button look
      if (method == 'fav') {
        target.html('Remove from Favorites')
        target.addClass('btn-outline-warning')
        target.removeClass('btn-warning')
      } else {
        target.html('Add to Favorites')
        target.addClass('btn-warning')
        target.removeClass('btn-outline-warning')
      }

      // Change button data
      new_method = (method == 'fav' ?'unfav' :'fav')
      target.data('method', new_method)

      target.prop('disabled', false)
    },
    error: function() {}
  });
}

function update_sub_listeners() {
  $('.subscribe').on('click', subscribe)
}

function update_fav_listeners() {
  $('.favorite').on('click', favorite)
}