from helium import *
from time import sleep
import json
import requests

# -- data -- #
credentials = json.loads(open("credentials.json"))
INSTACART_EMAIL = credentials["INSTACART_EMAIL"]
INSTACART_PASSWORD = credentials["INSTACART_PASSWORD"]
MAILGUN_URL = credentials["MAILGUN_URL"]
MAILGUN_API_KEY = credentials["MAILGUN_API_KEY"]
STORE_LIST = credentials["STORE_LIST"]
INSTACART_BASE_URL = credentials["INSTACART_BASE_URL"]
INSTACART_DELIVERY_URL = credentials["INSTACART_DELIVERY_URL"]
NOTIFICATION_EMAIL = credentials["NOTIFICATION_EMAIL"]

# -- login logic -- #
start_chrome(INSTACART_BASE_URL, headless=True)
click(Link("Log In"))
write(INSTACART_EMAIL, into="Email address")
write(INSTACART_PASSWORD, into="Password")
click(Button("Log In"))
wait_until(Link("See delivery times").exists)


# -- check store logic -- #
def check_delivery_times_for_store(store_name):
    go_to(INSTACART_DELIVERY_URL.format(store_name))
    sleep(2)
    if Text("No delivery times available").exists():
        return False, "No Delivery times available. Try again later?"
    else:
        return (
            True,
            "Delivery times found for {}! Please check soon :)".format(store_name),
        )


# -- send email -- #
def send_simple_message(message):
    return requests.post(
        "https://api.mailgun.net/v3/{}/messages".format(MAILGUN_DOMAIN),
        auth=("api", MAILGUN_API_KEY),
        data={
            "from": "Instacart Delivery Notifier <instacart_notify@{}>".format(
                MAILGUN_DOMAIN
            ),
            "to": NOTIFICATION_EMAIL,
            "subject": "Instacart Delivery Time Available!!",
            "text": message,
        },
    )


# -- check all stores in list and notify -- #
def main():
    for store in STORE_LIST:
        availability, message = check_delivery_times_for_store(store)
        if availability:
            send_simple_message(message)
        else:
            pass


if __name__ == "__main__":
    main()
