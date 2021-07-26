"""
|•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••| 
⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝

                          GNU GENERAL PUBLIC LICENSE
                            Version 3, 29 June 2007
                            
        Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                        ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝,
                        Telegram Music player userbot 
                has been licensed under GNU General Public License
            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝
|•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••|        
"""
from ʜᴏᴍᴇ import *
from .variables import HEROKU





if HEROKU is not None and HEROKU == "HEROKU":
    API_ID = os.environ.get('API_ID')
    API_HASH = os.environ.get('API_HASH')
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    XERONOID_SESSION = os.environ.get('XERONOID_SESSION')
elif HEROKU != "HEROKU":
    API_ID = 6372795 
    API_HASH = "4b7731b0a6d8e15bef82863887feb293"
    BOT_TOKEN = "1631463971:AAG8m2_kx-fxfWlOq8NA7pq5_rSxHWLzn9Y"
    XERONOID_SESSION = "BQAO0V1Yuir9Lv-OPW-vJEc9Rwo4UsmGjN-8QygT-rPWVjtriObqp2ivthicAQLGSswOaR1l8I3o-uXDPaJEhPygx_AvAc3TaApqNp4kTQZYki8gFFLeqAQ5ghpakW9hZ0T5r3n1Kzru2DLyFB0pONy1RTyOXGlU5qxIct7MY3SLLXW7ajFYLoAfqL2voTB1Sqw33TdxGC7UnTBUyv_Wg_HF8-rlFdW4wJPu4-CPUlvpBkpkhOmEdUd-yZ1AGEf-yEK5us462a98Cg7nVJhlJ6j0OI5PbdTsb-N2Gks_LE-_jiq3nFDyDmlB_Iq9LoM6eqyrbVN4Tsd2CgI-EEbqyXbdbXPecgA" 
else:
    cprint('Please recheck all the needed variables and restart the bot.',on_color='on_red')
    cprint('Exiting Xeronoid now','magenta', attrs=['concealed'])
    sys.exit()
