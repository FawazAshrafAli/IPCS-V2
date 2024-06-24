function addProductValidate(){
    var productName = document.addProductForm.product_name.value;
    var image = document.addProductForm.image;
    var link = document.addProductForm.link.value;

    if(productName==null || productName.trim().length === 0 || productName[0] === ' '){
        document.getElementById('product_name-span').innerHTML="<i>Required</i>";
        document.addProductForm.product_name.focus();
        document.addProductForm.product_name.style.border = "1px solid red";
        scrollToError('product_name-span');
        return false;
    } else {
        document.getElementById('product_name-span').innerHTML="";
        document.addProductForm.product_name.blur();
        document.addProductForm.product_name.style.border = "none";
    }

    if (image.files.length === 0) {
        document.getElementById('image-span').innerHTML="<i>Required</i>";
        document.addProductForm.image.focus();
        document.addProductForm.image.style.border = "1px solid red";
        scrollToError('image-span');
        return false;
    } else {
        document.getElementById('image-span').innerHTML="";
        document.addProductForm.image.blur();
        document.addProductForm.image.style.border = "none";
    }

    if(link==null|| link.trim().length === 0 || link[0] === ' '){
        document.getElementById('link-span').innerHTML="<i>Required</i>";
        document.addProductForm.link.focus();
        document.addProductForm.link.style.border = "1px solid red";
        scrollToError('link-span');
        return false;
    } else {
        document.getElementById('link-span').innerHTML="";
        document.addProductForm.link.blur();
        document.addProductForm.link.style.border = "none";
    }

    return true;
}

function updateProductValidate(){
    var productName = document.updateProductForm.product_name.value;

    if(productName==null || productName.trim().length === 0 || productName[0] === ' '){
        document.getElementById('product_name-span').innerHTML="<i>Required</i>";
        document.updateProductForm.product_name.focus();
        document.updateProductForm.product_name.style.border = "1px solid red";
        scrollToError('product_name-span');
        return false;
    } else {
        document.getElementById('product_name-span').innerHTML="";
        document.updateProductForm.product_name.blur();
        document.updateProductForm.product_name.style.border = "none";
    }

    return true;
}

function addClientValidate(){
    var clienttName = document.addClientForm.name.value;
    var image = document.addClientForm.image;

    if(clienttName==null || clienttName.trim().length === 0 || clienttName[0] === ' '){
        document.getElementById('name-span').innerHTML="<i>Required</i>";
        document.addClientForm.name.focus();
        document.addClientForm.name.style.border = "1px solid red";
        scrollToError('name-span');
        return false;
    } else {
        document.getElementById('name-span').innerHTML="";
        document.addClientForm.name.blur();
        document.addClientForm.name.style.border = "none";
    }

    if (image.files.length === 0) {
        document.getElementById('image-span').innerHTML="<i>Required</i>";
        document.addClientForm.image.focus();
        document.addClientForm.image.style.border = "1px solid red";
        scrollToError('image-span');
        return false;
    } else {
        document.getElementById('image-span').innerHTML="";
        document.addClientForm.image.blur();
        document.addClientForm.image.style.border = "none";
    }

    return true;
}

function updateClientValidate(){
    var clientName = document.updateClientForm.name.value;

    if(clientName==null || clientName.trim().length === 0 || clientName[0] === ' '){
        document.getElementById('name-span').innerHTML="<i>Required</i>";
        document.updateClientForm.name.focus();
        document.updateClientForm.name.style.border = "1px solid red";
        scrollToError('name-span');
        return false;
    } else {
        document.getElementById('name-span').innerHTML="";
        document.updateClientForm.name.blur();
        document.updateClientForm.name.style.border = "none";
    }

    return true;
}

function addTechnicianValidate(){
    var technicianName = document.addTechnicianForm.name.value;
    var email = document.addTechnicianForm.email.value;
    var mobile = document.addTechnicianForm.mobile.value;
    var department = document.addTechnicianForm.department.value;
    var residentialLocation = document.addTechnicianForm.residential_location.value;
    var photo = document.addTechnicianForm.photo.value;

    if(technicianName==null || technicianName.trim().length === 0 || technicianName[0] === ' '){
        document.getElementById('name-span').innerHTML="<i>Required</i>";
        document.addTechnicianForm.name.focus();
        document.addTechnicianForm.name.style.border = "1px solid red";        
        scrollToError('name-span');
        return false;
    } else {
        document.getElementById('name-span').innerHTML="";
        document.addTechnicianForm.name.blur();
        document.addTechnicianForm.name.style.border = "none";
    }

    if(email==null || email.trim().length === 0 || email[0] === ' '){
        document.getElementById('email-span').innerHTML="<i>Required</i>";
        document.addTechnicianForm.email.focus();
        document.addTechnicianForm.email.style.border = "1px solid red";        
        scrollToError('email-span');
        return false;
    } else {
        document.getElementById('email-span').innerHTML="";
        document.addTechnicianForm.email.blur();
        document.addTechnicianForm.email.style.border = "none";
    }

    if(mobile==null || mobile.trim().length === 0 || mobile[0] === ' '){
        document.getElementById('mobile-span').innerHTML="<i>Required</i>";
        document.addTechnicianForm.mobile.focus();
        document.addTechnicianForm.mobile.style.border = "1px solid red";        
        scrollToError('mobile-span');
        return false;
    } else {
        document.getElementById('mobile-span').innerHTML="";
        document.addTechnicianForm.mobile.blur();
        document.addTechnicianForm.mobile.style.border = "none";
    }

    if(department==null || department.trim().length === 0 || department[0] === ' '){
        document.getElementById('department-span').innerHTML="<i>Required</i>";
        document.addTechnicianForm.department.focus();
        document.addTechnicianForm.department.style.border = "1px solid red";        
        scrollToError('department-span');
        return false;
    } else {
        document.getElementById('department-span').innerHTML="";
        document.addTechnicianForm.department.blur();
        document.addTechnicianForm.department.style.border = "none";
    }

    if(residentialLocation==null || residentialLocation.trim().length === 0 || residentialLocation[0] === ' '){
        document.getElementById('residential_location-span').innerHTML="<i>Required</i>";
        document.addTechnicianForm.residential_location.focus();
        document.addTechnicianForm.residential_location.style.border = "1px solid red";        
        scrollToError('residential_location-span');
        return false;
    } else {
        document.getElementById('residential_location-span').innerHTML="";
        document.addTechnicianForm.residential_location.blur();
        document.addTechnicianForm.residential_location.style.border = "none";
    }

    if(photo==null || photo.trim().length === 0 || photo[0] === ' '){
        document.getElementById('photo-span').innerHTML="<i>Required</i>";
        document.addTechnicianForm.photo.focus();
        document.addTechnicianForm.photo.style.border = "1px solid red";        
        scrollToError('photo-span');
        return false;
    } else {
        document.getElementById('photo-span').innerHTML="";
        document.addTechnicianForm.photo.blur();
        document.addTechnicianForm.photo.style.border = "none";
    }

    return true;
    
}

function updateTechnicianValidate(){
    var technicianName = document.updateTechnicianForm.name.value;
    var email = document.updateTechnicianForm.email.value;
    var mobile = document.updateTechnicianForm.mobile.value;
    var department = document.updateTechnicianForm.department.value;
    var residentialLocation = document.updateTechnicianForm.residential_location.value;    

    if(technicianName==null || technicianName.trim().length === 0 || technicianName[0] === ' '){
        document.getElementById('name-span').innerHTML="<i>Required</i>";
        document.updateTechnicianForm.name.focus();
        document.updateTechnicianForm.name.style.border = "1px solid red";        
        scrollToError('name-span');
        return false;
    } else {
        document.getElementById('name-span').innerHTML="";
        document.updateTechnicianForm.name.blur();
        document.updateTechnicianForm.name.style.border = "none";
    }

    if(email==null || email.trim().length === 0 || email[0] === ' '){
        document.getElementById('email-span').innerHTML="<i>Required</i>";
        document.updateTechnicianForm.email.focus();
        document.updateTechnicianForm.email.style.border = "1px solid red";        
        scrollToError('email-span');
        return false;
    } else {
        document.getElementById('email-span').innerHTML="";
        document.updateTechnicianForm.email.blur();
        document.updateTechnicianForm.email.style.border = "none";
    }

    if(mobile==null || mobile.trim().length === 0 || mobile[0] === ' '){
        document.getElementById('mobile-span').innerHTML="<i>Required</i>";
        document.updateTechnicianForm.mobile.focus();
        document.updateTechnicianForm.mobile.style.border = "1px solid red";        
        scrollToError('mobile-span');
        return false;
    } else {
        document.getElementById('mobile-span').innerHTML="";
        document.updateTechnicianForm.mobile.blur();
        document.updateTechnicianForm.mobile.style.border = "none";
    }

    if(department==null || department.trim().length === 0 || department[0] === ' '){
        document.getElementById('department-span').innerHTML="<i>Required</i>";
        document.updateTechnicianForm.department.focus();
        document.updateTechnicianForm.department.style.border = "1px solid red";        
        scrollToError('department-span');
        return false;
    } else {
        document.getElementById('department-span').innerHTML="";
        document.updateTechnicianForm.department.blur();
        document.updateTechnicianForm.department.style.border = "none";
    }

    if(residentialLocation==null || residentialLocation.trim().length === 0 || residentialLocation[0] === ' '){
        document.getElementById('residential_location-span').innerHTML="<i>Required</i>";
        document.updateTechnicianForm.residential_location.focus();
        document.updateTechnicianForm.residential_location.style.border = "1px solid red";        
        scrollToError('residential_location-span');
        return false;
    } else {
        document.getElementById('residential_location-span').innerHTML="";
        document.updateTechnicianForm.residential_location.blur();
        document.updateTechnicianForm.residential_location.style.border = "none";
    }

    return true;
    
}

function warrantyValidate(){
      
    var customerName=document.warranty_form.customer_name.value;    
    var email=document.warranty_form.email_id.value;
    var contactNumber=document.warranty_form.contact_number.value;

    var product=document.warranty_form.product.value;    
    
    var serialNumber=document.warranty_form.serial_number.value;
    var modelNumber=document.warranty_form.model_number.value;
    var invoiceNumber=document.warranty_form.invoice_number.value;
    var billingName=document.warranty_form.billing_name.value;
    var addressCustomer=document.warranty_form.address_customer.value;
    var productComplain=document.warranty_form.product_complain.value;

    if(customerName==null|| customerName.trim().length === 0 || customerName[0] === ' '){
        document.getElementById('name-span').innerHTML="<i>Required</i>";
        document.warranty_form.customer_name.focus();
        document.warranty_form.customer_name.style.border = "1px solid red";
        scrollToError('name-span');
        return false;
    } else {
        document.getElementById('name-span').innerHTML="";
        document.warranty_form.customer_name.blur();
        document.warranty_form.customer_name.style.border = "none";
    }

    if(email==null|| email.trim().length === 0 || email[0] === ' '){
        document.getElementById('email-span').innerHTML="<i>Required</i>";
        document.warranty_form.email_id.focus();
        document.warranty_form.email_id.style.border = "1px solid red";
        scrollToError('email-span');
        return false;
    } else {
        document.getElementById('email-span').innerHTML="";
        document.warranty_form.email_id.blur();
        document.warranty_form.email_id.style.border = "none";
    }

    if(contactNumber==null|| contactNumber.trim().length === 0 || contactNumber[0] === ' '){
        document.getElementById('contact-span').innerHTML="<i>Required</i>";
        document.warranty_form.contact_number.focus();
        document.warranty_form.contact_number.style.border = "1px solid red";
        scrollToError('contact-span');
        return false;
    } else {
        document.getElementById('contact-span').innerHTML="";
        document.warranty_form.contact_number.blur();
        document.warranty_form.contact_number.style.border = "none";
    }

    if(product==null || product=="" || product=="none"){        
        document.getElementById('product-span').innerHTML="<i>Required<i>";
        document.warranty_form.product.focus();
        document.warranty_form.product.style.border = "1px solid red";
        scrollToError('product-span');
        return false;
    } else {
        document.getElementById('product-span').innerHTML="";
        document.warranty_form.product.blur();
        document.warranty_form.product.style.border = "none";
    }

    if(serialNumber==null|| serialNumber.trim().length === 0 || serialNumber[0] === ' '){
        document.getElementById('serial-span').innerHTML="<i>Required</i>";
        document.warranty_form.serial_number.focus();
        document.warranty_form.serial_number.style.border = "1px solid red";
        scrollToError('serial-span');
        return false;
    } else {
        document.getElementById('serial-span').innerHTML="";
        document.warranty_form.serial_number.blur();
        document.warranty_form.serial_number.style.border = "none";
    }

    if(modelNumber==null|| modelNumber.trim().length === 0 || modelNumber[0] === ' '){
        document.getElementById('model-span').innerHTML="<i>Required</i>";
        document.warranty_form.model_number.focus();
        document.warranty_form.model_number.style.border = "1px solid red";
        scrollToError('model-span');
        return false;
    } else {
        document.getElementById('model-span').innerHTML="";
        document.warranty_form.model_number.blur();
        document.warranty_form.model_number.style.border = "none";
    }

    if(invoiceNumber==null|| invoiceNumber.trim().length === 0 || invoiceNumber[0] === ' '){
        document.getElementById('invoice-span').innerHTML="<i>Required</i>";
        document.warranty_form.invoice_number.focus();
        document.warranty_form.invoice_number.style.border = "1px solid red";
        scrollToError('invoice-span');
        return false;
    } else {
        document.getElementById('invoice-span').innerHTML="";
        document.warranty_form.invoice_number.blur();
        document.warranty_form.invoice_number.style.border = "none";
    }

    if(billingName==null|| billingName.trim().length === 0 || billingName[0] === ' '){
        document.getElementById('billing-span').innerHTML="<i>Required</i>";
        document.warranty_form.billing_name.focus();
        document.warranty_form.billing_name.style.border = "1px solid red";
        scrollToError('billing-span');
        return false;
    } else {
        document.getElementById('billing-span').innerHTML="";
        document.warranty_form.billing_name.blur();
        document.warranty_form.billing_name.style.border = "none";
    }

    if(addressCustomer==null|| addressCustomer.trim().length === 0 || addressCustomer[0] === ' '){
        document.getElementById('address-span').innerHTML="<i>Required</i>";
        document.warranty_form.address_customer.focus();
        document.warranty_form.address_customer.style.border = "1px solid red";
        scrollToError('address-span');
        return false;
    } else {
        document.getElementById('address-span').innerHTML="";
        document.warranty_form.address_customer.blur();
        document.warranty_form.address_customer.style.border = "none";
    }

    if(productComplain==null|| productComplain.trim().length === 0 || productComplain[0] === ' '){
        document.getElementById('complain-span').innerHTML="<i>Required</i>";
        document.warranty_form.product_complain.focus();
        document.warranty_form.product_complain.style.border = "1px solid red";
        scrollToError('complain-span');
        return false;
    } else {
        document.getElementById('complain-span').innerHTML="";
        document.warranty_form.product_complain.blur();
        document.warranty_form.product_complain.style.border = "none";
    }

    return true;
}

function repairValidate(){
    
    var customerName=document.repair_form.customer_name.value;        
    var email=document.repair_form.email_id.value;
    var contactNumber=document.repair_form.contact_number.value;

    var product=document.repair_form.product.value;    
    
    var serialNumber=document.repair_form.serial_number.value;
    var modelNumber=document.repair_form.model_number.value;
    var addressCustomer=document.repair_form.address_customer.value;
    var itemDescription=document.repair_form.item_description.value;
    if(customerName==null|| customerName.trim().length === 0 || customerName[0] === ' '){        
        document.getElementById('name-span').innerHTML="<i>Required</i>";
        document.repair_form.customer_name.focus();
        document.repair_form.customer_name.style.border = "1px solid red";
        scrollToError('name-span');
        return false;
    } else {
        document.getElementById('name-span').innerHTML="";
        document.repair_form.customer_name.blur();
        document.repair_form.customer_name.style.border = "none";
    }

    if(email==null|| email.trim().length === 0 || email[0] === ' '){
        document.getElementById('email-span').innerHTML="<i>Required</i>";
        document.repair_form.email_id.focus();
        document.repair_form.email_id.style.border = "1px solid red";
        scrollToError('email-span');
        return false;
    } else {
        document.getElementById('email-span').innerHTML="";
        document.repair_form.email_id.blur();
        document.repair_form.email_id.style.border = "none";
    }

    if(contactNumber==null|| contactNumber.trim().length === 0 || contactNumber[0] === ' '){
        document.getElementById('contact-span').innerHTML="<i>Required</i>";
        document.repair_form.contact_number.focus();
        document.repair_form.contact_number.style.border = "1px solid red";
        scrollToError('contact-span');
        return false;
    } else {
        document.getElementById('contact-span').innerHTML="";
        document.repair_form.contact_number.blur();
        document.repair_form.contact_number.style.border = "none";
    }

    if(product==null || product=="" || product=="none"){        
        document.getElementById('product-span').innerHTML="<i>Required<i>";
        document.repair_form.product.focus();
        document.repair_form.product.style.border = "1px solid red";
        scrollToError('product-span');
        return false;
    } else {
        document.getElementById('product-span').innerHTML="";
        document.repair_form.product.blur();
        document.repair_form.product.style.border = "none";
    }

    if(serialNumber==null|| serialNumber.trim().length === 0 || serialNumber[0] === ' '){
        document.getElementById('serial-span').innerHTML="<i>Required</i>";
        document.repair_form.serial_number.focus();
        document.repair_form.serial_number.style.border = "1px solid red";
        scrollToError('serial-span');
        return false;
    } else {
        document.getElementById('serial-span').innerHTML="";
        document.repair_form.serial_number.blur();
        document.repair_form.serial_number.style.border = "none";
    }

    if(modelNumber==null|| modelNumber.trim().length === 0 || modelNumber[0] === ' '){
        document.getElementById('model-span').innerHTML="<i>Required</i>";
        document.repair_form.model_number.focus();
        document.repair_form.model_number.style.border = "1px solid red";
        scrollToError('model-span');
        return false;
    } else {
        document.getElementById('model-span').innerHTML="";
        document.repair_form.model_number.blur();
        document.repair_form.model_number.style.border = "none";
    }

    if(addressCustomer==null|| addressCustomer.trim().length === 0 || addressCustomer[0] === ' '){
        document.getElementById('address-span').innerHTML="<i>Required</i>";
        document.repair_form.address_customer.focus();
        document.repair_form.address_customer.style.border = "1px solid red";
        scrollToError('address-span');
        return false;
    } else {
        document.getElementById('address-span').innerHTML="";
        document.repair_form.address_customer.blur();
        document.repair_form.address_customer.style.border = "none";
    }

    if(itemDescription==null|| itemDescription.trim().length === 0 || itemDescription[0] === ' '){
        document.getElementById('item-span').innerHTML="<i>Required</i>";
        document.repair_form.item_description.focus();
        document.repair_form.item_description.style.border = "1px solid red";
        scrollToError('item-span');
        return false;
    } else {
        document.getElementById('item-span').innerHTML="";
        document.repair_form.item_description.blur();
        document.repair_form.item_description.style.border = "none";
    }

    return true;
}

function serviceValidate(){    
    var customerName=document.service_form.customer_name.value;        
    var email=document.service_form.email_id.value;
    var contactNumber=document.service_form.contact_number.value;

    var product=document.service_form.product.value;  
    
    var serialNumber=document.service_form.serial_number.value;
    var addressCustomer=document.service_form.address_customer.value;
    var itemDescription=document.service_form.service_description.value;

    if(customerName==null|| customerName.trim().length === 0 || customerName[0] === ' '){        
        document.getElementById('name-span').innerHTML="<i>Required</i>";
        document.service_form.customer_name.focus();
        document.service_form.customer_name.style.border = "1px solid red";
        scrollToError('name-span');
        return false;
    } else {
        document.getElementById('name-span').innerHTML="";
        document.service_form.customer_name.blur();
        document.service_form.customer_name.style.border = "none";
    };     

    if(email==null|| email.trim().length === 0 || email[0] === ' '){
        document.getElementById('email-span').innerHTML="<i>Required</i>";
        document.service_form.email_id.focus();
        document.service_form.email_id.style.border = "1px solid red";
        scrollToError('email-span');
        return false;
    } else {
        document.getElementById('email-span').innerHTML="";
        document.service_form.email_id.blur();
        document.service_form.email_id.style.border = "none";
    };

    if(contactNumber==null|| contactNumber.trim().length === 0 || contactNumber[0] === ' '){
        document.getElementById('contact-span').innerHTML="<i>Required</i>";
        document.service_form.contact_number.focus();
        document.service_form.contact_number.style.border = "1px solid red";
        scrollToError('contact-span');
        return false;
    } else {
        document.getElementById('contact-span').innerHTML="";
        document.service_form.contact_number.blur();
        document.service_form.contact_number.style.border = "none";
    };

    if(product==null || product=="" || product=="none"){        
        document.getElementById('product-span').innerHTML="<i>Required<i>";
        document.service_form.product.focus();
        document.service_form.product.style.border = "1px solid red";
        scrollToError('product-span');
        return false;
    } else {
        document.getElementById('product-span').innerHTML="";
        document.service_form.product.blur();
        document.service_form.product.style.border = "none";
    };

    if(serialNumber==null|| serialNumber.trim().length === 0 || serialNumber[0] === ' '){
        document.getElementById('serial-span').innerHTML="<i>Required</i>";
        document.service_form.serial_number.focus();
        document.service_form.serial_number.style.border = "1px solid red";
        scrollToError('serial-span');
        return false;
    } else {
        document.getElementById('serial-span').innerHTML="";
        document.service_form.serial_number.blur();
        document.service_form.serial_number.style.border = "none";
    };

    if(addressCustomer==null|| addressCustomer.trim().length === 0 || addressCustomer[0] === ' '){
        document.getElementById('address-span').innerHTML="<i>Required</i>";
        document.service_form.address_customer.focus();
        document.service_form.address_customer.style.border = "1px solid red";
        scrollToError('address-span');
        return false;
    } else {
        document.getElementById('address-span').innerHTML="";
        document.service_form.address_customer.blur();
        document.service_form.address_customer.style.border = "none";
    };

    if(itemDescription==null|| itemDescription.trim().length === 0 || itemDescription[0] === ' '){
        document.getElementById('item-span').innerHTML="<i>Required</i>";
        document.service_form.service_description.focus();
        document.service_form.service_description.style.border = "1px solid red";
        scrollToError('item-span');
        return false;
    } else {
        document.getElementById('item-span').innerHTML="";
        document.service_form.service_description.blur();
        document.service_form.service_description.style.border = "none";
    };

    return true;
}

function productValidate(){      
    var name=document.productForm.product_name.value;
    
    if(name==null|| name.trim().length === 0 || name[0] === ' '){        
        document.getElementById('product_namee').innerHTML="<i>Enter the Product Name</i>";
        document.productForm.product_name.focus();
        scrollToError('product_namee-span');
        return false;
    }

    return true;
}

function warrantyRejectionValidate(){
    var rejectionReason=document.rejectionReasonForm.reason.value;

    if(rejectionReason==null|| rejectionReason.trim().length === 0 || rejectionReason[0] === ' '){
        document.getElementById('reason-span').innerHTML="<i>Required</i>";
        document.service_form.reason.focus();
        document.service_form.reason.style.border = "1px solid red";
        scrollToError('reason-span');
        return false;
    } else {
        document.getElementById('reason-span').innerHTML="";
        document.service_form.reason.blur();
        document.service_form.reason.style.border = "none";
    };

    return true;

}

// Customer Section

function customerSignInValidate(){
    var email=document.customerSignInForm.email.value;
    var password=document.customerSignInForm.password.value;

    if(email==null|| email.trim().length === 0 || email[0] === ' '){
        document.getElementById('email-span').innerHTML="<i>Required</i>";
        document.customerSignInForm.email.focus();
        document.customerSignInForm.email.style.border = "1px solid red";
        scrollToError('email-span');
        return false;
    } else {
        document.getElementById('email-span').innerHTML="";
        document.customerSignInForm.email.blur();
        document.customerSignInForm.email.style.border = "none";
    }

    if(password==null|| password.trim().length === 0 || password[0] === ' '){
        document.getElementById('password-span').innerHTML="<i>Required</i>";
        document.customerSignInForm.password.focus();
        document.customerSignInForm.password.style.border = "1px solid red";
        scrollToError('password-span');
        return false;
    } else {
        document.getElementById('password-span').innerHTML="";
        document.customerSignInForm.password.blur();
        document.customerSignInForm.password.style.border = "none";
    };

    return true;

}

function customerForgotPasswordValidate(){
    var email=document.customerForgotPasswordForm.email.value;

    if(email==null|| email.trim().length === 0 || email[0] === ' '){
        document.getElementById('forgot_email-span').innerHTML="<i>Required</i>";
        document.customerForgotPasswordForm.email.focus();
        document.customerForgotPasswordForm.email.style.border = "1px solid red";
        scrollToError('forgot_email-span');
        return false;
    } else {
        document.getElementById('forgot_email-span').innerHTML="";
        document.customerForgotPasswordForm.email.blur();
        document.customerForgotPasswordForm.email.style.border = "none";
    }

    return true;

}

function customerResetForgottenPasswordValidate() {
    var otp=document.customerResetForgottenPasswordForm.otp.value;
    var newPassword=document.customerResetForgottenPasswordForm.new_password.value;
    var repeatPassword=document.customerResetForgottenPasswordForm.repeat_password.value;

    if(otp==null|| otp.trim().length === 0 || otp[0] === ' '){
        document.getElementById('otp-span').innerHTML="<i>Required</i>";
        document.customerResetForgottenPasswordForm.otp.focus();
        document.customerResetForgottenPasswordForm.otp.style.border = "1px solid red";
        scrollToError('otp-span');
        return false;
    } else {
        document.getElementById('otp-span').innerHTML="";
        document.customerResetForgottenPasswordForm.otp.blur();
        document.customerResetForgottenPasswordForm.otp.style.border = "none";
    };

    if(newPassword==null|| newPassword.trim().length === 0 || newPassword[0] === ' '){
        document.getElementById('new_password-span').innerHTML="<i>Required</i>";
        document.customerResetForgottenPasswordForm.new_password.focus();
        document.customerResetForgottenPasswordForm.new_password.style.border = "1px solid red";
        scrollToError('new_password-span');
        return false;
    } else {
        document.getElementById('new_password-span').innerHTML="";
        document.customerResetForgottenPasswordForm.new_password.blur();
        document.customerResetForgottenPasswordForm.new_password.style.border = "none";
    };

    if(repeatPassword==null|| repeatPassword.trim().length === 0 || repeatPassword[0] === ' '){
        document.getElementById('repeat_password-span').innerHTML="<i>Required</i>";
        document.customerResetForgottenPasswordForm.repeat_password.focus();
        document.customerResetForgottenPasswordForm.repeat_password.style.border = "1px solid red";
        scrollToError('repeat_password-span');
        return false;
    } else {
        document.getElementById('repeat_password-span').innerHTML="";
        document.customerResetForgottenPasswordForm.repeat_password.blur();
        document.customerResetForgottenPasswordForm.repeat_password.style.border = "none";
    };

    return true;

}

function customerSignUpValidate(){
    var name=document.customerSignUpForm.name.value;
    var email=document.customerSignUpForm.email.value;
    var phone=document.customerSignUpForm.phone.value;
    var password=document.customerSignUpForm.password.value;
    var repeatPassword=document.customerSignUpForm.repeat_password.value;

    if(name==null|| name.trim().length === 0 || name[0] === ' '){
        document.getElementById('name-span').innerHTML="<i>Required</i>";
        document.customerSignUpForm.name.focus();
        document.customerSignUpForm.name.style.border = "1px solid red";
        scrollToError('name-span');
        return false;
    } else {
        document.getElementById('name-span').innerHTML="";
        document.customerSignUpForm.name.blur();
        document.customerSignUpForm.name.style.border = "none";
    }

    if(email==null|| email.trim().length === 0 || email[0] === ' '){
        document.getElementById('email-span').innerHTML="<i>Required</i>";
        document.customerSignUpForm.email.focus();
        document.customerSignUpForm.email.style.border = "1px solid red";
        scrollToError('email-span');
        return false;
    } else {
        document.getElementById('email-span').innerHTML="";
        document.customerSignUpForm.email.blur();
        document.customerSignUpForm.email.style.border = "none";
    }

    if(phone==null|| phone.trim().length === 0 || phone[0] === ' '){
        document.getElementById('phone-span').innerHTML="<i>Required</i>";
        document.customerSignUpForm.phone.focus();
        document.customerSignUpForm.phone.style.border = "1px solid red";
        scrollToError('phone-span');
        return false;
    } else {
        document.getElementById('phone-span').innerHTML="";
        document.customerSignUpForm.phone.blur();
        document.customerSignUpForm.phone.style.border = "none";
    }

    if(password==null|| password.trim().length === 0 || password[0] === ' '){
        document.getElementById('password-span').innerHTML="<i>Required</i>";
        document.customerSignUpForm.password.focus();
        document.customerSignUpForm.password.style.border = "1px solid red";
        scrollToError('password-span');
        return false;
    } else {
        document.getElementById('password-span').innerHTML="";
        document.customerSignUpForm.password.blur();
        document.customerSignUpForm.password.style.border = "none";
    };

    if(repeatPassword==null|| repeatPassword.trim().length === 0 || repeatPassword[0] === ' '){
        document.getElementById('repeat_password-span').innerHTML="<i>Required</i>";
        document.customerSignUpForm.repeat_password.focus();
        document.customerSignUpForm.repeat_password.style.border = "1px solid red";
        scrollToError('repeat_password-span');
        return false;
    } else {
        document.getElementById('repeat_password-span').innerHTML="";
        document.customerSignUpForm.repeat_password.blur();
        document.customerSignUpForm.repeat_password.style.border = "none";
    };

    return true;

}

function customerInfoValidate(){
    var name = document.customerInfo.name.value;
    var phone = document.customerInfo.phone.value;

    if(name==null || name.trim().length === 0 || name[0] === ' '){
        document.getElementById('name-span').innerHTML="<i>Required</i>";
        document.customerInfo.name.focus();
        document.customerInfo.name.style.border = "1px solid red";
        scrollToError('name-span');
        return false;
    } else {
        document.getElementById('name-span').innerHTML="";
        document.customerInfo.name.blur();
        document.customerInfo.name.style.border = "none";
    }

    if(phone==null || phone.trim().length === 0 || phone[0] === ' '){
        document.getElementById('phone-span').innerHTML="<i>Required</i>";
        document.customerInfo.phone.focus();
        document.customerInfo.phone.style.border = "1px solid red";
        scrollToError('phone-span');
        return false;
    } else {
        document.getElementById('phone-span').innerHTML="";
        document.customerInfo.phone.blur();
        document.customerInfo.phone.style.border = "none";
    }

    return true;
}

// Admin Section

function adminSignInValidate(){
    var username=document.adminSignInForm.username.value;
    var password=document.adminSignInForm.password.value;

    if(username==null|| username.trim().length === 0 || username[0] === ' '){
        document.getElementById('username-span').innerHTML="<i>Required</i>";
        document.adminSignInForm.username.focus();
        document.adminSignInForm.username.style.border = "1px solid red";
        scrollToError('username-span');
        return false;
    } else {
        document.getElementById('username-span').innerHTML="";
        document.adminSignInForm.username.blur();
        document.adminSignInForm.username.style.border = "none";
    }

    if(password==null|| password.trim().length === 0 || password[0] === ' '){
        document.getElementById('password-span').innerHTML="<i>Required</i>";
        document.adminSignInForm.password.focus();
        document.adminSignInForm.password.style.border = "1px solid red";
        scrollToError('password-span');
        return false;
    } else {
        document.getElementById('password-span').innerHTML="";
        document.adminSignInForm.password.blur();
        document.adminSignInForm.password.style.border = "none";
    };

    return true;

}

function adminForgotPasswordValidate(){
    var username=document.adminForgorPasswordForm.username.value;

    if(username==null|| username.trim().length === 0 || username[0] === ' '){
        document.getElementById('forgot_username-span').innerHTML="<i>Required</i>";
        document.adminForgorPasswordForm.username.focus();
        document.adminForgorPasswordForm.username.style.border = "1px solid red";
        scrollToError('forgot_username-span');
        return false;
    } else {
        document.getElementById('forgot_username-span').innerHTML="";
        document.adminForgorPasswordForm.username.blur();
        document.adminForgorPasswordForm.username.style.border = "none";
    }

    return true;

}

function adminResetForgottenPasswordValidate() {
    var otp=document.adminResetForgottenPasswordForm.otp.value;
    var newPassword=document.adminResetForgottenPasswordForm.new_password.value;
    var repeatPassword=document.adminResetForgottenPasswordForm.repeat_password.value;

    if(otp==null|| otp.trim().length === 0 || otp[0] === ' '){
        document.getElementById('otp-span').innerHTML="<i>Required</i>";
        document.adminResetForgottenPasswordForm.otp.focus();
        document.adminResetForgottenPasswordForm.otp.style.border = "1px solid red";
        scrollToError('otp-span');
        return false;
    } else {
        document.getElementById('otp-span').innerHTML="";
        document.adminResetForgottenPasswordForm.otp.blur();
        document.adminResetForgottenPasswordForm.otp.style.border = "none";
    };

    if(newPassword==null|| newPassword.trim().length === 0 || newPassword[0] === ' '){
        document.getElementById('new_password-span').innerHTML="<i>Required</i>";
        document.adminResetForgottenPasswordForm.new_password.focus();
        document.adminResetForgottenPasswordForm.new_password.style.border = "1px solid red";
        scrollToError('new_password-span');
        return false;
    } else {
        document.getElementById('new_password-span').innerHTML="";
        document.adminResetForgottenPasswordForm.new_password.blur();
        document.adminResetForgottenPasswordForm.new_password.style.border = "none";
    };

    if(repeatPassword==null|| repeatPassword.trim().length === 0 || repeatPassword[0] === ' '){
        document.getElementById('repeat_password-span').innerHTML="<i>Required</i>";
        document.adminResetForgottenPasswordForm.repeat_password.focus();
        document.adminResetForgottenPasswordForm.repeat_password.style.border = "1px solid red";
        scrollToError('repeat_password-span');
        return false;
    } else {
        document.getElementById('repeat_password-span').innerHTML="";
        document.adminResetForgottenPasswordForm.repeat_password.blur();
        document.adminResetForgottenPasswordForm.repeat_password.style.border = "none";
    };

    return true;

}

function scrollToError(elementId) {
    var errorElement = document.getElementById(elementId);

    // Introduce a slight delay before scrolling
    setTimeout(function() {
        window.scrollTo({
            top: errorElement.offsetTop,
            behavior: 'smooth'
        });
    }, 100); // Adjust the delay as needed
}

// General
function resetPasswordValidate(){
    var currentPassword=document.resetPasswordForm.current_password.value;
    var newPassword=document.resetPasswordForm.new_password.value;
    var repeatPassword=document.resetPasswordForm.repeat_password.value;

    if(currentPassword==null|| currentPassword.trim().length === 0 || currentPassword[0] === ' '){
        document.getElementById('current_password-span').innerHTML="<i>Required</i>";
        document.resetPasswordForm.current_password.focus();
        document.resetPasswordForm.current_password.style.border = "1px solid red";
        scrollToError('current_password-span');
        return false;
    } else {
        document.getElementById('current_password-span').innerHTML="";
        document.resetPasswordForm.current_password.blur();
        document.resetPasswordForm.current_password.style.border = "none";
    };

    if(newPassword==null|| newPassword.trim().length === 0 || newPassword[0] === ' '){
        document.getElementById('new_password-span').innerHTML="<i>Required</i>";
        document.resetPasswordForm.new_password.focus();
        document.resetPasswordForm.new_password.style.border = "1px solid red";
        scrollToError('new_password-span');
        return false;
    } else {
        document.getElementById('new_password-span').innerHTML="";
        document.resetPasswordForm.new_password.blur();
        document.resetPasswordForm.new_password.style.border = "none";
    };

    if(repeatPassword==null|| repeatPassword.trim().length === 0 || repeatPassword[0] === ' '){
        document.getElementById('repeat_password-span').innerHTML="<i>Required</i>";
        document.resetPasswordForm.repeat_password.focus();
        document.resetPasswordForm.repeat_password.style.border = "1px solid red";
        scrollToError('repeat_password-span');
        return false;
    } else {
        document.getElementById('repeat_password-span').innerHTML="";
        document.resetPasswordForm.repeat_password.blur();
        document.resetPasswordForm.repeat_password.style.border = "none";
    };

    return true;

}