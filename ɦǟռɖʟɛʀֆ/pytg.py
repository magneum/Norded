""" 
⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝
|----------------------------------------------------------------------------------------|
                          GNU GENERAL PUBLIC LICENSE
                            Version 3, 29 June 2007
                            
        Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.

                        ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝,
                        Telegram Music player userbot 
                has been licensed under GNU General Public License
            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
|----------------------------------------------------------------------------------------|       
⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝
"""
from ɖօօʍ_ʀօօʍ import *
from ʟɨɮʀǟʀʏ_ʀօօʍ import *
from .xeroobj import xeronoid_show_playlist, xeroclip


async def xeronoid_msg_sender(text):
    xeronoid_musical_xhat = xeroclip.xeronoid_musical_xhat
    client = xeronoid_musical_xhat.client
    xeronoid_chatid = xeroclip.xeronoid_chatid
    xero_send_msgnr = await client.send_animation(
    xeronoid_chatid,
    text,
    animation=xerolink,
    disable_web_page_preview=False,
    disable_notification=False
    )
    return xero_send_msgnr

async def xeronoid_bot_msg_sender(text):
    xeronoid_musical_xhat = xeroclip.xeronoid_musical_xhat
    client = xeronoid_musical_xhat.client
    xeronoid_chatid = LOGGER_ID
    xero_send_msgnr = await client.send_animation(
    xeronoid_chatid,
    text,
    animation=xerolink,
    disable_web_page_preview=False,
    disable_notification=False
    )
    return xero_send_msgnr


async def network_status_changed_handler(context, is_connected: bool):
    if is_connected:
        xeroclip.xeronoid_chatid = macid - context.full_chat.id
        await xeronoid_msg_sender(
        f"""{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n|========	🎧 𝙐𝙨𝙚𝙧𝙗𝙤𝙩 𝙝𝙖𝙨 𝙗𝙚𝙚𝙣 𝙥𝙡𝙪𝙜𝙜𝙚𝙙 𝙞𝙣 𝙩𝙝𝙚 𝙜𝙧𝙤𝙪𝙥 
        `{CHAT_ID}`'s 𝙫𝙤𝙞𝙘𝙚 𝙘𝙝𝙖𝙩
        """)
        await xeronoid_bot_msg_sender(
        f"{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n|========	🎧 𝙐𝙨𝙚𝙧𝙗𝙤𝙩 𝙝𝙖𝙨 𝙗𝙚𝙚𝙣 𝙥𝙡𝙪𝙜𝙜𝙚𝙙"
        )
    else:
        await xeronoid_msg_sender(
        f"""{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n|========	🎧 𝙐𝙨𝙚𝙧𝙗𝙤𝙩 𝙝𝙖𝙨 𝙗𝙚𝙚𝙣 𝙪𝙣𝙥𝙡𝙪𝙜𝙜𝙚𝙙 𝙛𝙧𝙤𝙢 𝙩𝙝𝙚 𝙜𝙧𝙤𝙪𝙥 
        `{CHAT_ID}`'s 𝙫𝙤𝙞𝙘𝙚 𝙘𝙝𝙖𝙩
        """)
        await xeronoid_bot_msg_sender(
        f"{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n|========	🎧 𝙐𝙨𝙚𝙧𝙗𝙤𝙩 𝙝𝙖𝙨 𝙗𝙚𝙚𝙣 𝙪𝙣𝙥𝙡𝙪𝙜𝙜𝙚𝙙"
				)
        xeroclip.xeronoid_chatid = None


async def xeronoid_music_over_handler(_, __):
    await xeronoid_show_playlist()