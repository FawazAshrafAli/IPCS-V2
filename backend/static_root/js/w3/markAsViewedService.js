function markAsViewedService(serviceRequestId) {
    $.ajax({
      type : "GET",
      url : '/admin/mark_as_viewed_service/' + serviceRequestId,
      dataType: 'json', 
      success: function (data) {
        $('#read-unread-' + serviceRequestId).prop('class', 'mdi mdi-email-open text-secondary').prop('title', 'Viewed');

        $('#read-unread-' + serviceRequestId).on('mouseenter', function () {
            $(this).css('box-shadow', '0px 0px 5px #777');
        });

        $('#read-unread-' + serviceRequestId).on('mouseleave', function () {
            $(this).css('box-shadow', 'none');
        });
      },
      error: function (error) {
        console.error('Error: ', error);
      }
    });
};