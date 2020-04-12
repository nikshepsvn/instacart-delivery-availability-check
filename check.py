from helium import *
from time import sleep
from datetime import datetime
import json
import requests
import time
import os
import sys

# -- data -- #
credentials = json.load(open("credentials.json"))
INSTACART_EMAIL = credentials["INSTACART_EMAIL"]
INSTACART_PASSWORD = credentials["INSTACART_PASSWORD"]
MAILGUN_URL = credentials["MAILGUN_DOMAIN"]
MAILGUN_API_KEY = credentials["MAILGUN_API_KEY"]
STORE_LIST = credentials["STORE_LIST"]
INSTACART_BASE_URL = credentials["INSTACART_BASE_URL"]
INSTACART_DELIVERY_URL = credentials["INSTACART_DELIVERY_URL"]
NOTIFICATION_EMAIL = credentials["NOTIFICATION_EMAIL"]

# -- login logic -- #
print("Logging into Instacart...")
start_chrome(INSTACART_BASE_URL, headless=True)
click(Button("Log In"))
write(INSTACART_EMAIL, into="Email address")
write(INSTACART_PASSWORD, into="Password")
click(Button("Log In"))
wait_until(Link("Your Items").exists)
print("Checking available delivery slots...\n")


# -- check store logic -- #
def check_delivery_times_for_store(store_name):
    go_to(INSTACART_DELIVERY_URL.format(store_name))
    sleep(5)

    if (Text("Saturday").exists() or Text("Sunday").exists() or Text("Monday").exists() or Text("Tuesday").exists() or Text("Wednesday").exists() or Text("Thursday").exists() or Text("Friday").exists()):
        return True, "Delivery times found for {}!".format(store_name)
    elif Text("Fast & Flexible").exists():
        return True, "Delivery times found for {}!".format(store_name)
    elif Link("More times").exists():
        return True, "Delivery times found for {}!".format(store_name)
    elif (Text("Today").exists() or Text("Tomorrow").exists()):
        return True, "Delivery times found for {}!".format(store_name)
    elif Text("There was a problem loading this page").exists():
        return False, "There was a problem loading {}".format(store_name)
    elif Text("No delivery times available").exists():
        return False, "No Delivery times available for {}".format(store_name)
    else:
        #unexpected response, generate screenshot, return generic error
        return False, "Unexpected response"


# -- send email -- #
def send_simple_message(message):

    if (MAILGUN_API_KEY=="") or (MAILGUN_API_KEY=="xxx") or (MAILGUN_URL=="") or (MAILGUN_URL=="xxx.mailgun.org") or (NOTIFICATION_EMAIL=="") or (NOTIFICATION_EMAIL=="xxx@gmail.com"):
        print ("ERROR: Can't sent email notification. Invalid Mailgun API Key, URL or Notification Email")
        return null

    return requests.post(
        "https://api.mailgun.net/v3/{}/messages".format(MAILGUN_URL),
        auth=("api", MAILGUN_API_KEY),
        data={
            "from": "Instacart Delivery Notifier <instacart_notify@{}>".format(
                MAILGUN_URL
            ),
            "to": NOTIFICATION_EMAIL,
            "subject": "Instacart Delivery Time Available!!",
            "text": message,
        },
    )


# -- check all stores in list and notify -- #
def main():
    flag = False

    while flag == False: 
        print("--------------- "+str(datetime.now().strftime("%b %d, %Y %H:%M:%S"))+" ------------")

        for store in STORE_LIST:
            availability, message = check_delivery_times_for_store(store)
            if availability == True:
                #os.system('say -v Samantha "Delivery is available at {}!"'.format(store))
                send_simple_message(message)
                flag = True

            print (message)

        print("\nNext update in 15 minutes...\n")
        time.sleep(900)


if __name__ == "__main__":
    main()
