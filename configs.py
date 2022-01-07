# (c) @MRK_YT

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("MT_BOT_TOKEN")
	BOT_USERNAME = os.environ.get("MT_BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("MT_BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("MT_UPDATES_CHANNEL", None)
	LOG_CHANNEL = int(os.environ.get("MT_LOG_CHANNEL"))
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("MO_TECH_YT", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [𝐇𝐚𝐫𝐮𝐤𝐚](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍ **Developer:** [Amal Nath](https://t.me/Unni0240)

 **Movie Group:** @cinima_lokham

 **Helper bot:** [Helper bot](https://t.me/amal_nath_05)

🗣️ **Helper bot:** [Helper bot](https://t.me/amal_nath_05)

📢 **Movie Channel:** [channel](https://t.me/+3NC6XL1s-pc4MjRl)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍ **Developer:** [Amal Nath](https://t.me/Unni0240)

💻 **Developer Details:** [Clcik Here](https://github.com/Masterrockiei)

👨‍💻 **Editing:** @cinima_lokham

🗣️ **Helper bot:** [Helper bot](https://t.me/amal_nath_05)

 **

🗣️ **Helper bot:** [Helper bot](https://t.me/amal_nath_05)

📢 **Movie Channel:** [channel](https://t.me/+3NC6XL1s-pc4MjRl)

Donate Now (coming soon)
"""
	HOME_TEXT = """
**👋Hi**, [{}](tg://user?id={})\n\n**This is Permanent** **MT FileStoreBot**.

**Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check About Bot Button**.
"""

