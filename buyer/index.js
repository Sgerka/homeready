'use strict';

const webflowAPI = require('./modules/webflow_module');


exports.handler = async (event) => {
    const response = {};
    response.headers = {
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
    };

    let dataFromRequest = JSON.parse(event.body);

    let updateBuyerData = async () => {
        let buyersCollectionId, sellersCollectionId, projectsCollectionId, buyersItems, sellersItems, projectsItems;

        await Promise.all([webflowAPI.getCollectionIdByName('Buyers'), webflowAPI.getCollectionIdByName('Sellers'), webflowAPI.getCollectionIdByName('Projects')]).then(async (collections) => {
            buyersCollectionId = collections[0][0]['_id'];
            sellersCollectionId = collections[1][0]['_id'];
            projectsCollectionId = collections[2][0]['_id'];
            await Promise.all([webflowAPI.getCollectionItems(buyersCollectionId), webflowAPI.getCollectionItems(sellersCollectionId), webflowAPI.getCollectionItems(projectsCollectionId)]).then(async (items) => {
                buyersItems = items[0];
                sellersItems = items[1];
                projectsItems = items[2];
            });
        });


        let projectToAdd = projectsItems.items.filter(item => item.address.includes(dataFromRequest.Project))[0]._id;
        let sellerToAdd = sellersItems.items.filter(item => item.slug.includes(dataFromRequest.seller))[0]._id;
        let existingBuyerOfThisSeller = buyersItems.items.filter(item => item['phone-number'] === dataFromRequest.Phone && item['sellers2'] === sellerToAdd)[0];

        if (existingBuyerOfThisSeller) {
            if (!existingBuyer.projects.includes(projectToAdd)) {
                existingBuyer.projects.push(projectToAdd);
                projectToAdd = existingBuyer.projects;
            }

            return await webflowAPI.updateCollectionItem(buyersCollectionId, existingBuyer['_id'], {
                'name': dataFromRequest.name,
                'slug': existingBuyer.slug,
                '_archived': false,
                '_draft': false,
                'phone-number': dataFromRequest.Phone,
                'projects': projectToAdd,
                'sellers2': sellerToAdd
            });

        } else {
            return await webflowAPI.setCollectionItem(buyersCollectionId, {
                'name': dataFromRequest.name,
                '_archived': false,
                '_draft': false,
                'phone-number': dataFromRequest.Phone,
                'projects': [projectToAdd],
                'sellers2': sellerToAdd
            });

        }
    };

    let updateBuyer = null;
    let error = '';

    try {
        updateBuyer = await updateBuyerData();
    } catch (e) {
        error = e;
    }

    if (updateBuyer == null) {
        response.statusCode = 400;
        response.body = `${error.name}: ${error.msg}. ${error.problems}`;

    } else {
        response.statusCode = 200;
        response.body = JSON.stringify(event);
    }

    console.log(response);
    return response;
};


// @TODO: We need to generate link and save it in DB somehow. And error handling.
// @TODO: Add a field to buyers with json {'project': 'link'}
