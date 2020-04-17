# instacart-delivery-availability-check
Tiny python script that check's instacart's delivery availability and notifies you if a slot opens up.

### Setup guide:
- Python3 is required
- Chromium based browser required.
- See `credentials_example.json` to create a `credentials.json` file and fill out all the fields with values!
- Install `helium`
- You can setup a free mailgun account if you want email notifications
- Extra: you can change the voice for the voice notifications, here's some other options: https://gist.github.com/mculp/4b95752e25c456d425c6

### Installation & Setup

- Fill `credentials_example.json` (rename file to `credentials.json`)

```sh
$ pip install tox
$ pip install helium
$ pip install requests
$ python check.py
```

### Notification settings

You can toggle which notifications you prefer in lines 79 & 80 in `check.py`. A free Mailgun account is required for email, see notion article below.

```sh
voiceNotification = True
emailNotification = True
```

### Non-technical setup guide: 
- You can head over to: https://www.notion.so/Instacart-Availability-Script-6b4372a81dd645e697088d5d82845227 for a complete run down of the set up 

NOTE: 
If you're using Instacart in the US, you'll have to change the base URLs for Instacart in the `credentials.json`, we've only made this Canadian friendly (sorry, sorry, sorry lol)

Feel free to open an issue if you have any questions!

### Project Maintainers
Nikshep Svn: @nikshepsvn

Ali Naqi: @anaqi

Alison Nham: @nhamalison 
