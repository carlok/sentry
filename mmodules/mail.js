"use strict"

const htmlToText = require("html-to-text")
const mailer = require("nodemailer")
const ses = require("nodemailer-ses-transport")

const _send = function (transport, mailOptions) {
    const transporter = mailer.createTransport(
        ses(transport)
    )

    return new Promise((resolve, reject) => {
        transporter.sendMail(mailOptions, (error, info) => {
            if (error) {
                return reject(error)
            }

            return resolve(info)
        })
    })
}

const sendAlarm = function (transport) {
    const bodyHtml = "sentry sent you this alarm: check it out"
    const bodyText = htmlToText.fromString(bodyHtml, {
        wordwrap: 60
    })

    const mailOptions = {
        from: process.env.SMTP_FROM,
        to: process.env.SMTP_TO,
        subject: `[${process.env.REMOTE_API_NAME}] Sentry problem`,
        text: bodyText,
        html: bodyHtml
    }

    return _send(transport, mailOptions)
}

module.exports = {
    sendAlarm: sendAlarm
}
