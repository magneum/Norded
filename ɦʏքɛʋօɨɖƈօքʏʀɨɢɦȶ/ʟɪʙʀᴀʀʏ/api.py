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
from ɦʏքɛʋօɨɖƈօքʏʀɨɢɦȶ.ʜᴏᴍᴇ import *
from .variables import HEROKU





if HEROKU == "HEROKU":
    API_ID = os.environ.get('API_ID')
    API_HASH = os.environ.get('API_HASH')
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    XERONOID_SESSION = os.environ.get('XERONOID_SESSION')
    HEROKU_APP_NAME = os.environ.get('HEROKU_APP_NAME')
    HEROKU_API_KEY = os.environ.get('HEROKU_API_KEY')
elif HEROKU != "HEROKU":
    API_ID = 666666
    API_HASH = "7ed80948c3b7ed80948c3b7ed80948c3b7ed80948c3b7"
    BOT_TOKEN = "7ed80948c3b7ed80948c3b7ed80948c3b7ed80948c3b7ed80948c3b"
    XERONOID_SESSION = "7ed80948c3b7ed80948c3b7ed80948c3b7ed80948c3b7ed80948c3b7ed80948c3b7ed80948c3b7ed80948c3b7ed80948c3b" 
else:
    cprint('Please recheck all the needed variables and restart the bot.',on_color='on_red')
    cprint('Exiting Xeronoid now','magenta', attrs=['concealed'])
    sys.exit()
