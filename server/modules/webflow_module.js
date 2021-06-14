const token = 'da89af68b3d968cd70822438d568281e39ce4dc2e6ee125ef8652c82193821d0';
const siteId = '60ba6f9ff86d92995f70770a';

const Webflow = require('webflow-api');
const webflowClient = new Webflow({token: token});

module.exports = {

    getInfo: async () => {
        return webflowClient.info();
    },

    getCollections: async () => {
        return webflowClient.collections({siteId: siteId});
    },

    getCollectionIdByName: async (name) => {
        let collections = await module.exports.getCollections();
        return collections.filter(collection => collection.name === name);
    },

    getCollectionItems: async (collectionId) => {
        return webflowClient.items({collectionId: collectionId}, {limit: 100});
    },

    setCollectionItem: async (collectionId, item) => {
        let newItem = await webflowClient.createItem({
            collectionId: collectionId,
            fields: item
        }, {live: true});
        return newItem;
    },

    updateCollectionItem: async (collectionId, itemId, fields) => {
        const updatedItem = await webflowClient.updateItem({
            collectionId: collectionId,
            itemId: itemId,
            fields: fields
        }, {live: true});
        return updatedItem;
    },

    patchCollectionItem: async (collectionId, itemId, fields) => {
        const patchedItem = await webflowClient.patchItem({
            collectionId: collectionId,
            itemId: itemId,
            fields: fields
        }, {live: true});
        return patchedItem;
    }

};
