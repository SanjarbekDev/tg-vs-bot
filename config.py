HEROKU = False   # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku.
if HEROKU:
    from os import environ
    API_ID = int(environ["API_ID"])
    API_HASH = environ["API_HASH"]
    SUDO_CHAT_ID = int(environ["SUDO_CHAT_ID"]) # Chat where the bot will play the music.
    SUDOERS = list(int(x) for x in environ.get("SUDOERS", "").split()) # Users which have special control over the bot.
    SESSION_STRING = environ["SESSION_STRING"] # Check Readme for session

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 2406175
    API_HASH = "fe5038b106043cfec0194366da9251c9"
    SUDO_CHAT_ID = -1001278644380
    SUDOERS = [708888699, 13216546]

# don't make changes below this line
ARQ_API = "https://thearq.tech"
