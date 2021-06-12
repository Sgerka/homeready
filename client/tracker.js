const stage = 'prod';
const trackingURL = 'https://cp422o1834.execute-api.us-east-1.amazonaws.com/test/tracking';

const sendTrackingData = async (data) => {
    switch (stage) {
        case 'dev':
            console.log(data);
            break;
        case 'prod':
            return await apiGatewayRequest(data);
        default:
            break;
    }

};


const apiGatewayRequest = async (data) => {
    let response = await fetch(`${trackingURL}\?` + new URLSearchParams(data));
    let json = await response.json();
    return json;
};

window.onload = async () => {
    let value = document.location.search;
    if (value !== '') {
        if (!sessionStorage.getItem(value)) {
            value = value.replace('?p=', '');
            let responseFromAPI = await sendTrackingData({
                type: 'session',
                link: value
            });
            if (responseFromAPI && responseFromAPI['_id']) {
                sessionStorage.setItem(value, responseFromAPI['_id']);
            }
        }

        setInterval(async () => {
            if (document.hasFocus()) {
                await sendTrackingData({
                    type: 'update_session',
                    link: value,
                    session_id: sessionStorage.getItem(value)
                });
            }
        }, 60000);
    }
};