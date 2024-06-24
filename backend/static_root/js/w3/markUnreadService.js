function markUnreadPopUpService(event, serviceRequestId) {
    event.stopPropagation();
    if (document.getElementById('read-unread-' + serviceRequestId).className == 'mdi mdi-email-open text-secondary'){
      document.getElementById('service-request-object').innerHTML = serviceRequestId;
      document.getElementById('confirm_unread_box').style.display = 'block';      
      document.getElementById('confirm-unread-btn').value = serviceRequestId;
    }
}


function markUnreadService(serviceRequestId) {
    $.ajax({
      type: 'GET',
      url: '/admin/mark_as_unread_service/'+serviceRequestId,
      dataType: 'json',
      success: function (data) {
        $('#read-unread-' + serviceRequestId).prop('class', 'mdi mdi-email text-primary').prop('title', 'Not Viewed');
        document.getElementById('confirm_unread_box').style.display = 'none';

        $('#read-unread-' + serviceRequestId).on('mouseenter', function () {
          $(this).css('box-shadow', 'none');
        });
      },
      error: function (error) {
        console.error('Error: ', error);
      }
    });
  };