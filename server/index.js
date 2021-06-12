'use strict';

const webflowAPI = require('./modules/webflow_module');


exports.handler = async (event) => {
    const response = {};
    response.headers = {
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
    };

    let queryString = event.queryStringParameters;

    let updateActivityLog = async () => {
        if (Object.keys(queryString).length < 1) {
            return false;
        }

        let activitiesCollection = await webflowAPI.getCollectionIdByName('Activities');
        let activitiesCollectionId = activitiesCollection[0]['_id'];
        let activitiesCollectionItems = await webflowAPI.getCollectionItems(activitiesCollectionId);

        let linksCollection = await webflowAPI.getCollectionIdByName('Links');
        let linksCollectionId = linksCollection[0]['_id'];
        let linksCollectionItems = await webflowAPI.getCollectionItems(linksCollectionId);
        let matchingLink = linksCollectionItems.items.filter(item => item.link.includes(queryString.link))[0];

        if (!matchingLink) {
            return false;
        }

        let seller = matchingLink.seller;
        let buyer = matchingLink.buyer;
        let project = matchingLink.project;

        if (queryString.type === 'session' || !queryString.session_id) {
            return await webflowAPI.setCollectionItem(activitiesCollectionId, {
                'name': new Date().toISOString(),
                '_archived': false,
                '_draft': false,
                'buyer': buyer,
                'project': project,
                'seller': seller,
                'time': new Date().toISOString(),
                'type': 'fa194ee38860554c54e3e29f54d0f977',
                'duration-seconds': 30,
                'duration': '0.5 דקות'
            });
        } else {
            let existing_session = activitiesCollectionItems.items.filter(item => item._id === queryString.session_id)[0];

            return await webflowAPI.updateCollectionItem(activitiesCollectionId, queryString.session_id, {
                'name': existing_session.name,
                'slug': existing_session.slug,
                '_archived': false,
                '_draft': false,
                'buyer': existing_session.buyer,
                'project': existing_session.project,
                'seller': existing_session.seller,
                'time': new Date().toISOString(),
                'type': 'fa194ee38860554c54e3e29f54d0f977',
                'duration-seconds': existing_session['duration-seconds'] + 60,
                'duration': ` דקות ${(existing_session['duration-seconds'] + 60) / 60}`
            });
        }


    };


    let update = await updateActivityLog();

    if (!update) {
        response.statusCode = 400;
        response.body = `Error in update`;

    } else {
        response.statusCode = 200;
        response.body = JSON.stringify(update);
    }

    console.log(response);

    return response;

};
