HEROKU = True   # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku.
if HEROKU:
    API_ID = 2406175
    API_HASH = "fe5038b106043cfec0194366da9251c9"
    SUDO_CHAT_ID = -1001278644380
    SUDOERS = [708888699, 1234567]
    SESSION_STRING = "AgC4or_NiE5ur9b7-ojvPRNTn7BYPJyA8L4z-eBrGJrDTBqhkXMHGzcGGtwXGuMtJ4riCRJVzKqbL5vBQsOVXBt_2ZjwcSD-1AhoC09x4zpH2PBFww3PVJLpCKQI6GiVB7EOtSVDKMiFNJj8sfBE-6uphTUNvygSY-X8wMyDa2f_0GTWrntsz8F8Z5Q1qA53k7-a63EjgiFsdZIEaScid423kXnyrB1d72_P6kvuZmnaOZctmKqRsV2yyqYDBe2bwP7L-LCZsiiCht_q4s7FaOIjgituHNecmtvUWnCoMkd25F3HokNxBJOGhcGdu_oPOXWGRnLy8jf5_0o6flFmSMqzbV-IYwA"

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 12345
    API_HASH = "As,1ddAda1ADda4d5dsaSSasd4ad5ad4asdADFDS"
    SUDO_CHAT_ID = -1001278644380
    SUDOERS = [708888699, 13216546]

# don't make changes below this line
ARQ_API = "https://thearq.tech"
