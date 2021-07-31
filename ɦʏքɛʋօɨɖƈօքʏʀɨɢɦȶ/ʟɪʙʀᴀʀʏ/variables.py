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
import os
from termcolor import *
HEROKU = os.environ.get('HEROKU', None)
if HEROKU is not None and HEROKU == "HEROKU":  
    OWNER_USERNAME = os.environ.get('OWNER_USERNAME')
    if OWNER_USERNAME:
        OWNER_USERNAME_TEMP = OWNER_USERNAME.upper()
        OWNER_USERNAME = [OWNER_USERNAME]
        '⇜⊷°•♪🦋♪•°⊶⇝'
    BOT_USERNAME = os.environ.get('BOT_USERNAME')
    if BOT_USERNAME:
        BOT_USERNAME = BOT_USERNAME.upper()
        '⇜⊷°•♪🦋♪•°⊶⇝'
    MUSIC_ADMIN_USERNAMES = os.environ.get('MUSIC_ADMIN_USERNAMES')
    if MUSIC_ADMIN_USERNAMES:
        MUSIC_ADMIN_USERNAMES = MUSIC_ADMIN_USERNAMES.upper()
    #     if MUSIC_ADMIN_USERNAMES.startswith("'"):
    #         MUSIC_ADMIN_USERNAMES = MUSIC_ADMIN_USERNAMES
    #     elif MUSIC_ADMIN_USERNAMES.startswith('"'):
    #         MUSIC_ADMIN_USERNAMES = MUSIC_ADMIN_USERNAMES.replace('"',"'")
    #     else:
    #         print("MUSIC_ADMIN_USERNAMES Layout is wrong! Please fix it")
        # '⇜⊷°•♪🦋♪•°⊶⇝'
    LOGGER_ID_TEMP = os.environ.get('LOGGER_ID')
    if LOGGER_ID_TEMP:
        LOGGER_ID = int(LOGGER_ID_TEMP)
        '⇜⊷°•♪🦋♪•°⊶⇝'
    OWNER_ID_TEMP = os.environ.get('OWNER_ID')
    if OWNER_ID_TEMP:
        OWNER_ID= int(OWNER_ID_TEMP)
        '⇜⊷°•♪🦋♪•°⊶⇝'
else:
    OWNER_ID = [1848646989]
    OWNER_USERNAME = '@HYPEVOIDSOUL'
    BOT_USERNAME = "@XERONOIDBOT"
    LOGGER_ID = int("-1001513582173")
    MUSIC_ADMIN_USERNAMES = '@hypevoidsoul,@DEVLIXIE,@kalitronx'

    
'⇜⊷°•♪🦋♪•°⊶⇝'
XERO = '⇜⊷°•♪   🦋Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝'
MAX_MIN = 8
MAX_HOUR = 3
USERBOT_PLANEL = dict(root="ɦʏքɛʋօɨɖƈօքʏʀɨɢɦȶ/Gҽɳҽɾαƚσɾʂ/xᴇʀᴏ_ʜᴀɴᴅʟᴇʀꜱ")
BOT_PLANEL = dict(root="ɦʏքɛʋօɨɖƈօքʏʀɨɢɦȶ/Gҽɳҽɾαƚσɾʂ/xᴇʀᴏʙᴏᴛ_ʜᴀɴᴅʟᴇʀꜱ")
xeroobj = object
WHITE_COMMANDK = '/'
DYNO_COMMANDK = '/'
XEROPRINT = cprint
CLEAN_REMOVER = 2
CURRENT_REMOVER = 8
GROUP_REMOVER = 6
HELP_REMOVER = 30
JOIN_REMOVER = 4
LEAVE_REMOVER = 4
MUTE_REMOVER = 8
PAUSE_REMOVER = 8
PLAY_REMOVER = 8
REPLAY_REMOVER = 8
RESUME_REMOVER = 8
SKIP_REMOVER = 4
STOP_REMOVER = 6
UNMUTE_REMOVER = 6
VOLUME_REMOVER = 6
SERVER_REMOVER = 12
XEXO = "            **⇜⊷•♪ 🦋Ӽɛʀօռօɨɖ🦋 ♪•⊶⇝**\n`by` **🔥 ΉYPΣ VӨID LΛB 🔥**\n\n"
xerolink = "https://telegra.ph/file/cc35dba04ad629c0771b3.gif"
ON_OFF_FEED ="""
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