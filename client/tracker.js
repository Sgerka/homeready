const stage = 'dev';
const trackingURL = 'https://cp422o1834.execute-api.us-east-1.amazonaws.com/test/tracking';

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


window.onload = async () => {
    if (!sessionStorage.getItem('homeready_session')) {
        let data = {
            'user': 'german',
            'apartment': 2,
            'event': 'fa194ee38860554c54e3e29f54d0f977'
        };

        await sendTrackingData(data);
        sessionStorage.setItem('homeready_session', data.apartment);
    }
};
