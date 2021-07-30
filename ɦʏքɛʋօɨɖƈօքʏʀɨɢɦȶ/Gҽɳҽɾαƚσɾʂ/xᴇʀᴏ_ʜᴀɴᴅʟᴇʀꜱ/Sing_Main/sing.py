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
from ɦʏքɛʋօɨɖƈօքʏʀɨɢɦȶ.ᴘᴜʀɢᴇ_ᴍᴇᴄʜᴀɴɪꜱᴍ import * 
from ɦʏքɛʋօɨɖƈօքʏʀɨɢɦȶ.ᴍᴜꜱɪᴄ_ᴄᴏɴᴛᴇɴᴛ import *
from ɦʏքɛʋօɨɖƈօքʏʀɨɢɦȶ.xᴇʀᴏꜰɪʟᴇᴛꜱ import *
from ɦʏքɛʋօɨɖƈօքʏʀɨɢɦȶ.ʟɪʙʀᴀʀʏ import *
from ɦʏքɛʋօɨɖƈօքʏʀɨɢɦȶ.ʜᴏᴍᴇ import *



@Client.on_message(
filters.group
& ~filters.edited
& Known_admins
& Xero_Singer
& filters.command("sing", prefixes="/"))
async def play_track(client, XS: XeroSpeak):
    group_call = XePlay.group_call
    playlist = XePlay.playlist   
   
    
    "Check Wherether audio duration matches with the specified time mentioned in the code"
    if XS.audio:
        if XS.audio.duration > (MAX_MIN * 60):
            reply = await XS.reply_animation(
                animation=xerolink,
                caption=f"{XEXO}🎧 𝗔𝘂𝗱𝗶𝗼 𝘄𝗵𝗶𝗰𝗵 𝗱𝘂𝗿𝗮𝘁𝗶𝗼𝗻 𝗹𝗼𝗻𝗴𝗲𝗿 𝘁𝗵𝗮𝗻 {str(MAX_MIN)} 𝗺𝗶𝗻 𝘄𝗼𝗻'𝘁 𝗯𝗲 𝗮𝘂𝘁𝗼𝗺𝗮𝘁𝗶𝗰𝗮𝗹𝗹𝘆 𝗮𝗱𝗱𝗲𝗱 𝘁𝗼 𝗽𝗹𝗮𝘆𝗹𝗶𝘀𝘁",
                reply_markup = MIB
            )
            await xeronoid_sing_purge(
                (reply,),
                PLAY_REMOVER)
            return
        m_audio = XS
    elif XS.reply_to_message and XS.reply_to_message.audio:
        m_audio = XS.reply_to_message
        if m_audio.audio.duration > (MAX_HOUR * 60 * 60):
            reply = await XS.reply_animation(
                animation=xerolink,
                caption=f"{XEXO}🎧 𝗔𝘂𝗱𝗶𝗼 𝘄𝗵𝗶𝗰𝗵 𝗱𝘂𝗿𝗮𝘁𝗶𝗼𝗻 𝗹𝗼𝗻𝗴𝗲𝗿 𝘁𝗵𝗮𝗻 {str(MAX_HOUR)} 𝗵𝗼𝘂𝗿𝘀 𝘄𝗼𝗻'𝘁 𝗯𝗲 𝗮𝗱𝗱𝗲𝗱 𝘁𝗼 𝗽𝗹𝗮𝘆𝗹𝗶𝘀𝘁",
                reply_markup = MIB
            )
            await xeronoid_sing_purge(
                (reply,),
                PLAY_REMOVER)
            return
    else:
        await XePlay.send_playlist()
        await XS.delete()
        return
    
    
        
    
    
    "Check Wherether audio is already added in the playlist or not"
    if playlist and playlist[-1].audio.file_unique_id \
            == m_audio.audio.file_unique_id:
        reply = await XS.reply_animation(
            animation=xerolink,
            caption=f"{XEXO}🎧  𝗧𝗵𝗮𝘁 𝗺𝘂𝘀𝗶𝗰 𝗶𝘀 𝗮𝗹𝗿𝗲𝗮𝗱𝘆 𝗮𝗱𝗱𝗲𝗱 𝘁𝗼 𝘁𝗵𝗲 𝘅𝗲𝗿𝗼𝗻𝗼𝗶𝗱 𝗽𝗹𝗮𝘆𝗹𝗶𝘀𝘁",
            reply_markup = MIB
            )
        await xeronoid_sing_purge(
            (reply,),
            PLAY_REMOVER)
        return
    
    
        
    
    "Download the raw audio file and send to the server and return"
    playlist.append(m_audio)
    if len(playlist) == 1:
        m_status = await client.send_animation(
            animation=xerolink,
            duration=10,
            chat_id=LOGGER_ID,
            caption=f"{XEXO}🎧 𝗠𝘂𝘀𝗶𝗰 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝘀𝗲𝗻𝘁 𝘁𝗼 𝘁𝗵𝗲 𝘀𝗲𝗿𝘃𝗲𝗿...\n𝙋𝙡𝙚𝙖𝙨𝙚 𝙬𝙖𝙞𝙩"
        )
        
        
        m_status = await XS.reply_animation(
            animation=xerolink,
            caption=f"{XEXO}🎧 𝗣𝗹𝗲𝗮𝘀𝗲 𝘄𝗮𝗶𝘁 𝗳𝗼𝗿 𝘅𝗲𝗿𝗼𝗻𝗼𝗶𝗱 𝘁𝗼 𝗹𝗶𝗻𝗸 𝘄𝗶𝘁𝗵 𝘂𝘀𝗲𝗿𝗯𝗼𝘁'𝘀 𝘀𝗲𝗿𝘃𝗲𝗿...\n𝙂𝙧𝙚𝙖𝙩𝙚𝙧 𝙖𝙪𝙙𝙞𝙤 𝙨𝙞𝙯𝙚, 𝙢𝙤𝙧𝙚 𝙩𝙞𝙢𝙚 𝙩𝙤 𝙖𝙙𝙙 𝙩𝙤 𝙨𝙚𝙧𝙫𝙚𝙧",
            reply_markup = MIB
        )
        await download_audio(playlist[0])
        
        
        group_call.input_filename = os.path.join(
            client.workdir,
            DEFAULT_DOWNLOAD_DIR,
            f"{playlist[0].audio.file_unique_id}.raw"
        )
        await XePlay.update_start_time()
        await m_status.delete()
        
        
        
        
        "Log the audio being transcoded and played in the group..."
        await client.send_animation(
            animation=xerolink,
            duration=10,
            chat_id=LOGGER_ID,
            caption=f"{XEXO}🎧  𝗫𝗲𝗿𝗼𝗻𝗼𝗶𝗱 𝘂𝘀𝗲𝗿𝗯𝗼𝘁 𝗵𝗮𝘀 𝘀𝘁𝗮𝗿𝘁𝗲𝗱 𝗽𝗹𝗮𝘆𝗶𝗻𝗴:\n\n{playlist[0].audio.title}"
        )
        # Only userbot is going to log this event. So we need not to worry about Xeronoidbot
        
    await XePlay.send_playlist()
    for track in playlist[:2]:
        await download_audio(track)
    if not XS.audio:
        await XS.delete()
        
