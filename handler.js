'use strict'

const myModulesPath = "./mmodules/"
const api = require(`${myModulesPath}api`)
const mail = require(`${myModulesPath}mail`)

const apiOptions = {
  uri: `${process.env.REMOTE_API_BASE}${process.env.REMOTE_API_PATH}`
}

const transport = {
  accessKeyId: process.env.SMTP_USERNAME,
  secretAccessKey: process.env.SMTP_PASSWORD,
  region: process.env.AWS_REGION_SES,
  rateLimit: 5 // do not send more than 5 messages in a second
}

module.exports.sentry = async event => {
  return api.get(apiOptions)
    .then(() => console.log("ok")) // response.body
    .catch(() => mail.sendAlarm(transport))
};
