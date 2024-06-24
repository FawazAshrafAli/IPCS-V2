function loadingAnimation() {
    var newDiv = document.getElementById('assurance-section')
    newDiv.innerHTML = '<div class="text-center" id="loading-div"><div class="spinner-border" role="status"><span class="visually-hidden">Loading...</span></div></div><br/>';
}

function loadingAnimation2() {
    var newDiv = document.getElementById('assurance-section-2')
    newDiv.innerHTML = '<div class="text-center" id="loading-div"><div class="spinner-border" role="status"><span class="visually-hidden">Loading...</span></div></div><br/>';
}

function rejectWarrantyAndLoadAnimation() {
    document.getElementById('warranty-rejection-form').submit(); 

    var newDiv = document.getElementById('rejection-assurance-section');
    newDiv.innerHTML = '<div class="text-center" id="loading-div"><div class="spinner-border" role="status"><span class="visually-hidden">Loading...</span></div></div><br/>';
    
    document.getElementById('close-rejection-btn').style.display = 'none';
}

function completeWarrantyAndLoadAnimation() {
    document.getElementById('warranty-completion-form').submit(); 

    var newDiv = document.getElementById('completion-assurance-section');
    newDiv.innerHTML = '<div class="text-center" id="loading-div"><div class="spinner-border" role="status"><span class="visually-hidden">Loading...</span></div></div><br/>';
    
    document.getElementById('close-completion-btn').style.display = 'none';
}

function completeServiceAndLoadAnimation() {
    document.getElementById('service-completion-form').submit(); 

    var newDiv = document.getElementById('completion-assurance-section');
    newDiv.innerHTML = '<div class="text-center" id="loading-div"><div class="spinner-border" role="status"><span class="visually-hidden">Loading...</span></div></div><br/>';    
}

function updateRemarkAndLoadAnimation() {
    document.getElementById('remark_update').submit(); 

    var newDiv = document.getElementById('remark-assurance-section');
    newDiv.innerHTML = '<div class="text-center" id="loading-div"><div class="spinner-border" role="status"><span class="visually-hidden">Loading...</span></div></div><br/>';

    document.getElementById('remark').setAttribute('disabled', 'true');
}

function updateReasonAndLoadAnimation() {
    document.getElementById('reason_update').submit(); 

    var newDiv = document.getElementById('reason-assurance-section');
    newDiv.innerHTML = '<div class="text-center" id="loading-div"><div class="spinner-border" role="status"><span class="visually-hidden">Loading...</span></div></div><br/>';       
}

function setReadyToDispatchAndLoadAnimation() {
    document.getElementById('repair-ready-to-dipatch-form').submit(); 

    var newDiv = document.getElementById('readyToDispatch-assurance-section');
    newDiv.innerHTML = '<div class="text-center" id="loading-div"><div class="spinner-border" role="status"><span class="visually-hidden">Loading...</span></div></div><br/>';       
}