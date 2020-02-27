from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from requests.exceptions import HTTPError
from socket import gaierror

import json
import logging
import os
import requests
import smtplib
import sys
import urllib3


def error_local(vhost, error_code):
    message = '[CEF] λ Error: ' + vhost
    mail_error(message, message + "\n" + error_code)
    print(error_code)


def mail_error(subject, body):
    msg = MIMEMultipart()
    msg['From'] = os.environ["EMAIL_SENDER"]
    msg['To'] = os.environ["EMAIL_RECEIVER"]
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(os.environ["EMAIL_HOST"], os.environ["EMAIL_PORT"])
    server.starttls()
    server.login(
        os.environ["EMAIL_HOST_USER"],
        os.environ["EMAIL_HOST_PASSWORD"])
    text = msg.as_string()

    try:
        server.sendmail(msg['From'], msg['To'], text)
        server.quit()
    except (gaierror, ConnectionRefusedError):
        print('Failed to connect to the server. Bad connection settings?')
    except smtplib.SMTPServerDisconnected:
        print('Failed to connect to the server. Wrong user/password?')
    except smtplib.SMTPException as e:
        print('SMTP error occurred: ' + str(e))
    else:
        print('Sent')


def vhost_https_get(vhost):
    try:
        url = 'https://' + vhost + '.cliccaefinanzia.it/api/v1/proposals/public'
        print(url)
        response = requests.get(url, verify=False, timeout=10)

        print(response.status_code)

        if response.status_code != 200:
            error_local(vhost, 'HTTP != 200')
    except HTTPError as http_err:
        error_local(vhost, str(http_err))
        print(str(http_err))
    except Exception as err:
        error_local(vhost, str(err))
        print(str(err))
    return


def run(event, context):
    vhosts = ['api-proposals-staging', 'api-proposals']

    urllib3.disable_warnings()
    for vhost in vhosts:
        vhost_https_get(vhost)

    response = {
        "statusCode": 200,
        "body": "aaa"
    }

    return response
