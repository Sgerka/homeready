const stage = 'prod';
const trackingURL = 'https://cp422o1834.execute-api.us-east-1.amazonaws.com/test/tracking';
const storakeKey = 'hrs';

const sendTrackingData = async (data) => {
    switch (stage) {
        case 'dev':
            console.log(data);
            break;
        case 'prod':
            let response = await apiGatewayRequest(data);
            console.log(response);
            break;
        default:
            break;
    }

};


const apiGatewayRequest = async (data) => {
    return await fetch(`${trackingURL}\?` + new URLSearchParams(data));
};

const setCookie = (name, value) => {
    let date = new Date();
    // date.setTime(date.getTime() + 3600000);
    date.setTime(date.getTime());
    let path = document.location.pathname;
    let expires = date.toUTCString();
    document.cookie = `${name}=${value}; path=${path}; Expires=${expires}`;
};

window.onload = async () => {
    let value = document.location.search;
    if (value !== '') {
        if (!sessionStorage.getItem(storakeKey)) {
            value = value.replace('?p=', '');
            sessionStorage.setItem(storakeKey, value);
            await sendTrackingData({
                type: 'session',
                link: value
            });
        }

        setInterval(async () => {
            if (document.hasFocus()) {
                await sendTrackingData({
                    type: 'update_session',
                    link: value
                });
            }
        }, 60000);
    }
};