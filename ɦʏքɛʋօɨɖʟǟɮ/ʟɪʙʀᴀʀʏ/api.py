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
from ɦʏքɛʋօɨɖʟǟɮ.ʜᴏᴍᴇ import *
from .variables import HEROKU





if HEROKU == "HEROKU":
    API_ID = os.environ.get('API_ID')
    API_HASH = os.environ.get('API_HASH')
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    XERONOID_SESSION = os.environ.get('XERONOID_SESSION')
    HEROKU_APP_NAME = os.environ.get('HEROKU_APP_NAME')
    HEROKU_API_KEY = os.environ.get('HEROKU_API_KEY')
elif HEROKU != "HEROKU":
    API_ID = 6372795 
    API_HASH = "4b7731b0a6d8e15bef82863887feb293"
    BOT_TOKEN = "1631463971:AAFtMq4iEdHrdY7OkExEeogPnbW-yWX3uhk"
    XERONOID_SESSION = "BQAPdAWmIn8T5v7JZLVxv0o8MLdAqY5uvzDpsGXlaP1dbxTltXuInJZUFDgixX5c9cA1HRBTELueE52HkJLawGR3ebkleU5WsB6s3Ir8Oviy45zfnaeBwbDWkT0VYofkswxvI29lWWNkq_ovzH0RpexEavvlxr1yX9BD5jwp0O5FCSTl5Mi3noqNNqD5KPtzMAARa23dJBNc5uln9WOAG0AdvXKotiBuOXOWX2U0WluepUmXPO_GX3lvMQVhqr1YbR8wdzIYW4djtOdo8_563JSVXkP4Vixgcj8FEQNaYOoLbzNJMpqKLA-L8dUORKKUWNelejjkv-v7ow7o15ZiE5wUbXPecgA" 
else:
    cprint('Please recheck all the needed variables and restart the bot.',on_color='on_red')
    cprint('Exiting Xeronoid now','magenta', attrs=['concealed'])
    sys.exit()
