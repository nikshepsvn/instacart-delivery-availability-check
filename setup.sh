#!/usr/bin/env python3
import subprocess
import json

subprocess.run(['python3', '-m pip install --upgrade pip'], capture_output=True)
subprocess.run(['pip3', 'install -r requirements.txt'], capture_output=True)

INSTACART_EMAIL = input('Your Instacart Login Email:\n')
INSTACART_PASSWORD = input('Your Instacart Password:\n')
MAILGUN_URL = input('Your Mailgun Domain:\n')
MAILGUN_API_KEY = input('Mailgun App Secret\n')
STORE_LIST = ["walmart-canada", "real-canadian-superstore", "zehrs-markets","real-canadian-wholesale-club","valumart","t-t","shoppers-drug-mart","m-m-food-market"]
INSTACART_BASE_URL = "instacart.ca"
INSTACART_DELIVERY_URL = "https://www.instacart.ca/store/{}/info?tab=delivery"
NOTIFICATION_EMAIL = input('The email to send notifications to:\n')
reload_timer = int(input('Time between recheck, in minutes:\n'))*60

dict = {
"INSTACART_EMAIL": INSTACART_EMAIL,
"INSTACART_PASSWORD": INSTACART_PASSWORD,
"MAILGUN_API_KEY": MAILGUN_API_KEY,
"STORE_LIST": STORE_LIST,
"INSTACART_BASE_URL": INSTACART_BASE_URL,
"INSTACART_DELIVERY_URL": INSTACART_DELIVERY_URL,
"NOTIFICATION_EMAIL": NOTIFICATION_EMAIL,
"MAILGUN_DOMAIN": MAILGUN_URL,
"Update_Timer": reload_timer
}



with open('credentials.json', 'w') as outfile:
    json.dump(dict, outfile, indent = 6)