function markAsViewedRepair(repairRequestId) {
    $.ajax({
      type : "GET",
      url : '/admin/mark_as_viewed_repair/' + repairRequestId,
      dataType: 'json', 
      success: function (data) {
        $('#read-unread-' + repairRequestId).prop('class', 'mdi mdi-email-open text-secondary').prop('title', 'Viewed');

        $('#read-unread-' + repairRequestId).on('mouseenter', function () {
            $(this).css('box-shadow', '0px 0px 5px #777');
        });

        $('#read-unread-' + repairRequestId).on('mouseleave', function () {
            $(this).css('box-shadow', 'none');
        });
      },
      error: function (error) {
        console.error('Error: ', error);
      }
    });
};