function markUnreadPopUpWarranty(event, warrantyRequestId) {
    event.stopPropagation();
    if (document.getElementById('read-unread-' + warrantyRequestId).className == 'mdi mdi-email-open text-secondary'){
      document.getElementById('warranty-request-object').innerHTML = warrantyRequestId;
      document.getElementById('confirm_unread_box').style.display = 'block';      
      document.getElementById('confirm-unread-btn').value = warrantyRequestId;
    }
}


function markUnreadWarranty(warrantyRequestId) {
    $.ajax({
      type: 'GET',
      url: '/admin/mark_as_unread_warranty/'+warrantyRequestId,
      dataType: 'json',
      success: function (data) {
        $('#read-unread-' + warrantyRequestId).prop('class', 'mdi mdi-email text-primary').prop('title', 'Not Viewed');
        document.getElementById('confirm_unread_box').style.display = 'none';

        $('#read-unread-' + warrantyRequestId).on('mouseenter', function () {
          $(this).css('box-shadow', 'none');
        });
      },
      error: function (error) {
        console.error('Error: ', error);
      }
    });
  };