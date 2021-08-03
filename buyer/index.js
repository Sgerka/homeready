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
        let buyerData = {};

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


        let projectToAddObject = projectsItems.items.filter(item => item.slug.includes(dataFromRequest.Project))[0];
        let projectToAdd = projectToAddObject._id;
        let projectToAddSlug = dataFromRequest.Project;
        let sellerToAdd = sellersItems.items.filter(item => item.slug.includes(dataFromRequest.seller))[0]._id;
        let existingBuyerOfThisSeller = buyersItems.items.filter(item => item['phone-number'] === dataFromRequest.Phone && item['sellers2'] === sellerToAdd)[0];
        let updateCollectionItemRequest = null;
        let totalBuyersOfThisProject = projectToAddObject['total-buyers'] === undefined ? 0 : projectToAddObject['total-buyers'];

        if (existingBuyerOfThisSeller) {
            if (!existingBuyerOfThisSeller.projects.includes(projectToAdd)) {
                let newProject = projectToAdd;
                existingBuyerOfThisSeller.projects.push(projectToAdd);
                projectToAdd = existingBuyerOfThisSeller.projects;
                updateCollectionItemRequest = await webflowAPI.updateCollectionItem(buyersCollectionId, existingBuyerOfThisSeller['_id'], {
                    'name': dataFromRequest.name,
                    'slug': existingBuyerOfThisSeller.slug,
                    '_archived': false,
                    '_draft': false,
                    'phone-number': dataFromRequest.Phone,
                    'projects': projectToAdd,
                    'sellers2': sellerToAdd
                });

                await webflowAPI.patchCollectionItem(projectsCollectionId, newProject, {
                    'total-buyers': totalBuyersOfThisProject + 1
                });

                buyerData = {
                    'buyerId': updateCollectionItemRequest._id,
                    'sellerId': updateCollectionItemRequest.sellers2,
                    'projectId': newProject,
                    'projectSlug': projectToAddSlug
                };

            } else {
                buyerData = {
                    'buyerId': existingBuyerOfThisSeller._id,
                    'sellerId': existingBuyerOfThisSeller.sellers2,
                    'projectId': projectToAdd,
                    'projectSlug': projectToAddSlug
                };
            }

        } else {
            try {
                updateCollectionItemRequest = await webflowAPI.setCollectionItem(buyersCollectionId, {
                    'name': dataFromRequest.name,
                    'slug': dataFromRequest.Phone.toString(),
                    '_archived': false,
                    '_draft': false,
                    'phone-number': dataFromRequest.Phone,
                    'projects': [projectToAdd],
                    'sellers2': sellerToAdd
                });
            } catch (e) {
                throw e;
            }


            await webflowAPI.patchCollectionItem(projectsCollectionId, projectToAdd, {
                'total-buyers': totalBuyersOfThisProject + 1
            });

            buyerData = {
                'buyerId': updateCollectionItemRequest._id,
                'sellerId': updateCollectionItemRequest.sellers2,
                'projectId': projectToAdd,
                'projectSlug': projectToAddSlug
            };
        }
        return buyerData;
    };

    let addNewLink = async (data) => {
        let linksCollection = await webflowAPI.getCollectionIdByName('Links');
        let linksCollectionId = linksCollection[0]['_id'];
        let linksItems = await webflowAPI.getCollectionItems(linksCollectionId);
        let linksMatchingRequest = linksItems.items.filter(item => item.seller === data.sellerId && item.project === data.projectId && item.buyer === data.buyerId);

        if (linksMatchingRequest.length > 0) {
            return linksMatchingRequest[0].link;
        } else {
            let generateLink = Math.round(Math.random() * 10000000);
            let updateCollectionItemRequest = await webflowAPI.setCollectionItem(linksCollectionId, {
                'name': generateLink.toString(),
                '_archived': false,
                '_draft': false,
                'buyer': data.buyerId,
                'seller': data.sellerId,
                'project': data.projectId,
                'link': `http://homeready.co.il/project/${data.projectSlug}/?p=${generateLink}`
            });

            return updateCollectionItemRequest.link;
        }
    };

    let updateBuyer = null;
    let link = null;

    try {
        updateBuyer = await updateBuyerData();
    } catch (e) {
        response.statusCode = 400;
        response.body = JSON.stringify(e);
        console.log(response);
        return response;
    }

    try {
        link = await addNewLink(updateBuyer);
    } catch (e) {
        response.statusCode = 400;
        response.body = JSON.stringify(e);
        console.log(response);
        return response;
    }

    if (link == null) {
        response.statusCode = 400;
        response.body = `Ooops`;

    } else {
        response.statusCode = 200;
        response.body = JSON.stringify({'link': link});
    }

    console.log(response);
    return response;
};
