function markAsViewedWarranty(warrantyRequestId) {
    $.ajax({
      type : "GET",
      url : '/admin/mark_as_viewed_warranty/' + warrantyRequestId,
      dataType: 'json', 
      success: function (data) {
        $('#read-unread-' + warrantyRequestId).prop('class', 'mdi mdi-email-open text-secondary').prop('title', 'Viewed');

        $('#read-unread-' + warrantyRequestId).on('mouseenter', function () {
            $(this).css('box-shadow', '0px 0px 5px #777');
        });

        $('#read-unread-' + warrantyRequestId).on('mouseleave', function () {
            $(this).css('box-shadow', 'none');
        });
      },
      error: function (error) {
        console.error('Error: ', error);
      }
    });
};