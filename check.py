from helium import *
from time import sleep
import json
import requests
import time
import datetime

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
start_chrome(INSTACART_BASE_URL, headless=True)
click(Button("Log In"))
write(INSTACART_EMAIL, into="Email address")
write(INSTACART_PASSWORD, into="Password")
click(Button("Log In"))
wait_until(Link("See delivery times").exists)


# -- check store logic -- #
def check_delivery_times_for_store(store_name):
    go_to(INSTACART_DELIVERY_URL.format(store_name))
    sleep(2)
    if Text("No delivery times available").exists():
        #print("No Delivery times available")
        return False, "No Delivery times available for {}".format(store_name)
    elif Text("There was a problem loading this page").exists():
        return False, "There was a problem loading this page"
    else:
        #print("Delivery times found")
        return (
            True,
            "Delivery times found for {}! Please check soon :)".format(store_name)
        )


# -- send email -- #
def send_simple_message(message):
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
    status = False

    while status == False:
        print("---------------"+str(datetime.datetime.now())+"------------")

        for store in STORE_LIST:
            availability, message = check_delivery_times_for_store(store)
            
            print (message)

            if availability:
                send_simple_message(message)
                print(message)

                #status = True 
            else:
                pass

        time.sleep(900)


if __name__ == "__main__":
    main()
