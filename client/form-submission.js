
let submitFormData = {};
const endpointUrl = 'https://lgi8tlgvtd.execute-api.us-east-1.amazonaws.com/test/newbuyer';

async function postData(url = '', data = {}) {
    const response = await fetch(url, {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data) // body data type must match "Content-Type" header
    });
    return response.json(); // parses JSON response into native JavaScript objects
}

let formid = '#wf-form-Email-Form';

$(formid).submit(function (e) {
    submitFormData = JSON.parse('{"' + $(formid).serialize().replace(/&/g, '","').replace(/=/g,'":"') + '"}', function(key, value) { return key===""?value:decodeURIComponent(value) })

    submitFormData['seller'] = window.location.pathname.split('/')[2]
    let code = $('.iti__active span.iti__dial-code').text().replace(/[^0-9]/g, '');

    submitFormData.Phone = submitFormData.Phone.replace(/[^0-9]/g, '');

    if(!submitFormData.Phone.includes(code)){
        submitFormData.Phone = code + submitFormData.Phone.replace(/^0+/, '');
    }

    postData(endpointUrl, submitFormData)
        .then(data => {
            if(data.link){
                $( 'a[href*="wa"]' )[0].href = $( 'a[href*="wa"]' )[0].href.replace('-phoneplaceholder', submitFormData.Phone);
                $( 'a[href*="wa"]' )[0].href = $( 'a[href*="wa"]' )[0].href.replace('linkplaceholder', data.link);
                $('#myInput').text(data.link);
            }
            console.log(data.link); // JSON data parsed by `data.json()` call
        });
});

$('.modal-closer').click(function() {
    location.reload()
});

// New:
$('.card-subtitle').each(function () {
    let text = $(this).text();
    $(this).text(formatPhoneNumber(text));
});


let formatPhoneNumber = (phoneNumberString) => {
    phoneNumberString = phoneNumberString.replace('972', '0');
    var cleaned = ('' + phoneNumberString).replace(/\D/g, '');
    var match = cleaned.match(/^(\d{3})(\d{3})(\d{4})$/);
    if (match) {
        return match[1] + '-' + match[2] + '-' + match[3];
    }
    return phoneNumberString;
}


let text = $('.phone-number').text();
$('.phone-number').text(formatPhoneNumber(text));
