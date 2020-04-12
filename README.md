# instacart-delivery-availability-check
Tiny python script that check's instacart's delivery availability and notifies you if a slot opens up.

### Quick setup guide:
- See `credentials_example.json` to create a `credentials.json` file and fill out all the fields with values!
- Install `helium`, `requests`, `time`, `datetime` modules
- You can setup a free mailgun account if you want email notifications, if you want another way of getting notified just modify the `send_simple_message` function!
- Extra: you can change the voice for the voice notifications, here's some other options: https://gist.github.com/mculp/4b95752e25c456d425c6

### Non-technical setup guide: 
- You can head over to: https://www.notion.so/Instacart-Availability-Script-6b4372a81dd645e697088d5d82845227 for a complete run down of the set up 

NOTE: 
If you're using Instacart in the US, you'll have to change the base URLs for Instacart in the `credentials.json`, we've only made this Canadian friendly (sorry, sorry, sorry lol)

Feel free to open an issue if you have any questions!
