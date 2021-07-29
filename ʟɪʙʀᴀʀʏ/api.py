"""
|•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••| 
⇜⊷°•♪   🦋Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝

                          GNU GENERAL PUBLIC LICENSE
                            Version 3, 29 June 2007
                            
        Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                        ⇜⊷°•♪   🦋Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝,
                        Telegram Music player userbot 
                has been licensed under GNU General Public License
            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
⇜⊷°•♪   🦋Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝
|•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••|        
"""
from ʜᴏᴍᴇ import *
from .variables import HEROKU





if HEROKU == "HEROKU":
    API_ID = os.environ.get('API_ID')
    API_HASH = os.environ.get('API_HASH')
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    XERONOID_SESSION = os.environ.get('XERONOID_SESSION')
    HEROKU_APP_NAME = os.environ.get('HEROKU_APP_NAME')
    HEROKU_API_KEY = os.environ.get('HEROKU_API_KEY')
elif HEROKU != "HEROKU":
    API_ID = 5397317 
    API_HASH = "7ed80948c3b916010963407eaccd1752"
    BOT_TOKEN = "1631463971:AAFtMq4iEdHrdY7OkExEeogPnbW-yWX3uhk"
    XERONOID_SESSION = "BQDF2H8tazqK34_7MJS2jTKRId_v3A7EN7lmFUGTSmIJTCyltEsGoTglzsty9XeaMut495fsmlF9KiVszVjSsnkbHYsQjw1dbact5pwTAtnMqXFyo-BqYmYDgFkKz9kKtaPum_3Vuq5e-0N9grgVpvwBM-XPmnqeL1lYwhw1JWXxSHCpG3eGfNfDzJVx8Zjym9bMAcH7cGQjs-RUlcltzSDd-_sQEhA4--TmNA0m85HyWccSS5nYJtAWEEnnUDaxoPJ7zpw0W6KIRl--d0GCEwlUyuHgqR_2_2pJTx40Vr9Qba_DcDYHp1BiFLS3agwpV6ErRGhnYjA-IofGc135L4ErbjAdTQA" 
else:
    cprint('Please recheck all the needed variables and restart the bot.',on_color='on_red')
    cprint('Exiting Xeronoid now','magenta', attrs=['concealed'])
    sys.exit()
