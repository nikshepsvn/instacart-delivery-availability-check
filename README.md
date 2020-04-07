# instacart-delivery-availability-check
Tiny python script that check's instacart's delivery availability and notifies you if a slot opens up.

Note: I threw this together in a few mins so apologies for code quality etc.

### Quick setup guide:
- See `credentials_example.json` and fill out all the fields with values!
- You can setup a free mailgun account if you want email notifications, if you want another way of getting notified just modify the `send_simple_message` function!
- Setup as a cron job on your OS/Home Server etc. and let it run every 30mins/hour or so.

Feel free to open an issue if you have any questions!
