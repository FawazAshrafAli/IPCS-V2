var remark = document.getElementById('remark');

if (remark != null) {
    if (remark.value==null || remark.value.trim().length === 0 || remark.value[0] === ' ') {
        document.getElementById('remark-submit-btn').setAttribute('disabled', 'true');
    } else {
        document.getElementById('remark-submit-btn').removeAttribute('disabled');
    };

    remark.addEventListener('input', function () {
        if (this.value==null || this.value.trim().length === 0 || this.value[0] === ' ') {
            document.getElementById('remark-submit-btn').setAttribute('disabled', 'true');
        } else {
            document.getElementById('remark-submit-btn').removeAttribute('disabled');
        };
    });
}

var reason = document.getElementById('reason');

if (reason != null) {
    if (reason.value==null || reason.value.trim().length === 0 || reason.value[0] === ' ') {
        document.getElementById('reason-submit-btn').setAttribute('disabled', 'true');
    } else {
        document.getElementById('reason-submit-btn').removeAttribute('disabled');
    };

    reason.addEventListener('input', function () {
        if (this.value==null || this.value.trim().length === 0 || this.value[0] === ' ') {
            document.getElementById('reason-submit-btn').setAttribute('disabled', 'true');
        } else {
            document.getElementById('reason-submit-btn').removeAttribute('disabled');
        };
    });
}