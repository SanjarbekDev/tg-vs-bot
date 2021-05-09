# import logging
from pyrogram import Client, idle

API_ID = "2406175"
API_HASH = "fe5038b106043cfec0194366da9251c9"
SESSION_NAME = "AgDF7ddL96lyRbBuBtgh1eS-S9-ifI83znMDOjgWKtO6p1FZTCL7Iy_m5QtOa8PueY2h7xtuSLXO2QOVf_g1mrJ6Ee3wsfGO_Vmr2c-bzLbhvVKZaD_R0LSpBv_-zca4VCsuzAV4DA0km15-ab0C3p46HQ-XhlJjuxyt4L5OwfzPyWPoEcn5lWVKFlC9FcoLxSL5-aMKVKudUfzwJX1bPQfI2wM_-1R8amOU0AZ7YkpcLUmf3jYyG7BnEuaZUmdPuTntazwcIM0uzxeb9S-cgS1_ve-pu6OHjIuh8CFTMbWFFg0lyR4fBXn0HoDI-r4Wj2tNQJPNz992r4CjkvZL-u6FbV-IYwA"

PLUGINS = dict(
    root="plugins",
    include=[
        "vc.player",
        "ping",
        "sysinfo"
    ]
)

app = Client(SESSION_NAME, API_ID, API_HASH, plugins=PLUGINS)
# logging.basicConfig(level=logging.INFO)
app.start()
print('>>> USERBOT STARTED')
idle()
app.stop()
print('\n>>> USERBOT STOPPED')
