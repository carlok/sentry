"use strict"

const rp = require("request-promise-native")

const get = function (opt) {
    const options = {
        method: "GET",
        uri: opt.uri,
        headers: {},
        qs: {},
        body: {},
        json: true, // Automatically stringifies the body to JSON
        resolveWithFullResponse: true,
        strictSSL: false
    }

    return rp(options)
};

module.exports = {
    get: get
}
