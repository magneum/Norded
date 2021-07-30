import os
HEROKU = os.environ.get('HEROKU', None)
'|•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••|'
if HEROKU is not None and HEROKU == "HEROKU":
    '_______________________________________________'
    CHAT_ID = os.environ.get('CHAT_ID')
    CHAT_ID_TEMP = list(map(int, CHAT_ID.split()))
    CHAT_ID = CHAT_ID_TEMP
    '_______________________________________________'
    OWNER_ID = os.environ.get('CHAT_ID')
    OWNER_ID_TEMP = list(map(int, OWNER_ID))
    OWNER_ID = OWNER_ID_TEMP
    '_______________________________________________'
    OWNER_USERNAME = os.environ.get('OWNER_USERNAME')
    BOT_USERNAME = os.environ.get('BOT_USERNAME')
    '_______________________________________________'
    MUSIC_ADMIN_IDS = os.environ.get('MUSIC_ADMIN_IDS')
    MUSIC_ADMIN_IDS_TEMP = list(map(int, MUSIC_ADMIN_IDS.split()))
    MUSIC_ADMIN_IDS = MUSIC_ADMIN_IDS
    '_______________________________________________'
    LOGGER_ID = os.environ.get('LOGGER_ID')
    LOGGER_ID_TEMP = list(map(int, LOGGER_ID.split()))
    LOGGER_ID = LOGGER_ID_TEMP
    '_______________________________________________'
else:
    OWNER_ID = [1848646989]
    OWNER_USERNAME = '@HypeVoidSoul'
    BOT_USERNAME = "@XERONOIDBOT"
    LOGGER_ID = (-1001513582173)
    CHAT_ID = [-1001561595012,-1001472203238,-1001549079508]
    MUSIC_ADMIN_IDS = [1650583471,1848646989]
'|•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••|'