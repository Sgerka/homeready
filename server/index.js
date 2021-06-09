'use strict';

const webflowAPI = require('./modules/webflow_module');


exports.handler = async (event) => {
    const response = {};
    response.headers = {
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
    };

    let updateActivityLog = async () => {
        let activitiesCollection = await webflowAPI.getCollectionIdByName('Activities');
        let activitiesCollectionId = activitiesCollection[0]['_id'];

        return await webflowAPI.setCollectionItem(activitiesCollectionId, {
            'name': '05',
            'slug': '0005',
            '_archived': false,
            '_draft': false,
            'buyer': '60bf30547e21d36d22945c6e',
            'project': '60bb21c19d47da1e8faa75af',
            'seller': '60bf30a535f9adfa7f8f3653',
            'time': new Date().toISOString(),
            'type': 'fa194ee38860554c54e3e29f54d0f977'
        });
    };

    let newItem = null;
    let error = '';

    try {
        newItem = await updateActivityLog();
    } catch (e) {
        error = e;
    }

    if (newItem == null) {
        response.statusCode = 400;
        response.body = `${error.name}: ${error.msg}. ${error.problems}`;

    } else {
        response.statusCode = 200;
        response.body = JSON.stringify(event);
    }

    console.log(response);

    return response;

};
