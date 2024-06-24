function markUnreadPopUpRepair(event, repairRequestId) {
    event.stopPropagation();
    if (document.getElementById('read-unread-' + repairRequestId).className == 'mdi mdi-email-open text-secondary'){
      document.getElementById('repair-request-object').innerHTML = repairRequestId;
      document.getElementById('confirm_unread_box').style.display = 'block';      
      document.getElementById('confirm-unread-btn').value = repairRequestId;
    }
}


function markUnreadRepair(repairRequestId) {
    $.ajax({
      type: 'GET',
      url: '/admin/mark_as_unread_repair/'+repairRequestId,
      dataType: 'json',
      success: function (data) {
        $('#read-unread-' + repairRequestId).prop('class', 'mdi mdi-email text-primary').prop('title', 'Not Viewed');
        document.getElementById('confirm_unread_box').style.display = 'none';

        $('#read-unread-' + repairRequestId).on('mouseenter', function () {
          $(this).css('box-shadow', 'none');
        });
      },
      error: function (error) {
        console.error('Error: ', error);
      }
    });
  };