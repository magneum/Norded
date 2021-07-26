"""⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝
|•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••| 
                          GNU GENERAL PUBLIC LICENSE
                            Version 3, 29 June 2007
                            
        Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.

                        ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝,
                        Telegram Music player userbot 
                has been licensed under GNU General Public License
            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
|•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••|        
⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝"""
from Ӽɛʀօռօɨɖʍʊֆɨƈ import *
from ƈʊֆȶօʍ_ʄɨʟȶɛʀֆ import *
from ɖօօʍ_ʀօօʍ import *
from ǟʊȶօ_քʊʀɢɛʀ import *
from ʟɨɮʀǟʀʏ_ʀօօʍ import *
'⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝    ••••••••|••••••••    ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝'



# @Ӽɛʀօռօɨɖ.on_message(
# xerofil.group
# & ~xerofil.edited
# & xeronoid_chat_check
# & xerofil.command("play") | xerofil.audio)
# async def play_track(client, xemsg: xeromsg):
#     group_call = xep.group_call
#     if xemsg.audio:
#         if xemsg.audio.duration > (MAX_MIN * 60):
#             cprint('🎧 𝗨𝘀𝗲𝗿 𝗮𝘀𝗸𝗲𝗱 𝘁𝗼 𝗽𝗹𝗮𝘆 𝗮𝘂𝗱𝗶𝗼 𝗯𝘂𝘁 𝗮𝘂𝗱𝗶𝗼 𝗱𝘂𝗿𝗮𝘁𝗶𝗼𝗻 𝗻𝗼𝘁 𝗺𝗲𝘁', 'yellow', attrs=['reverse'])
#             xeronoid_throw = await xemsg.reply_animation(
#             animation=xerolink,
#             caption=f"{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n🎧 𝙎𝙤𝙧𝙧𝙮 𝙖𝙪𝙙𝙞𝙤 𝙬𝙝𝙞𝙘𝙝 𝙙𝙪𝙧𝙖𝙩𝙞𝙤𝙣 𝙡𝙤𝙣𝙜𝙚𝙧 𝙩𝙝𝙖𝙣 {str(MAX_MIN)} 𝗺𝗶𝗻 𝘄𝗼𝗻'𝘁 𝗯𝗲 𝗮𝘂𝘁𝗼𝗺𝗮𝘁𝗶𝗰𝗮𝗹𝗹𝘆 𝗮𝗱𝗱𝗲𝗱 𝘁𝗼 𝘅𝗲𝗿𝗼𝗻𝗼𝗶𝗱 𝗺𝘂𝘀𝗶𝗰 𝗹𝗶𝘀𝘁."
#             )
#             await delay_play_messages((xeronoid_throw,), PLAY_REMOVER)
#             return
#         m_audio = xemsg
#     elif xemsg.reply_to_message and xemsg.reply_to_message.audio:
#         m_audio = xemsg.reply_to_message
#         if m_audio.audio.duration > (MAX_HOUR * 60 * 60):
#             cprint('🎧 𝗨𝘀𝗲𝗿 𝗮𝘀𝗸𝗲𝗱 𝘁𝗼 𝗽𝗹𝗮𝘆 𝗮𝘂𝗱𝗶𝗼 𝗯𝘂𝘁 𝗮𝘂𝗱𝗶𝗼 𝗱𝘂𝗿𝗮𝘁𝗶𝗼𝗻 𝗻𝗼𝘁 𝗺𝗲𝘁', 'yellow', attrs=['reverse'])
#             xeronoid_throw = await xemsg.reply_animation(
#             animation=xerolink,
#             caption=f"{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n🎧 𝙎𝙤𝙧𝙧𝙮 𝙖𝙪𝙙𝙞𝙤 𝙬𝙝𝙞𝙘𝙝 𝙙𝙪𝙧𝙖𝙩𝙞𝙤𝙣 𝙡𝙤𝙣𝙜𝙚𝙧 𝙩𝙝𝙖𝙣 {str(MAX_HOUR)} 𝗵𝗼𝘂𝗿𝘀 𝘄𝗼𝗻'𝘁 𝗯𝗲 𝗮𝗱𝗱𝗲𝗱 𝘁𝗼 𝘅𝗲𝗿𝗼𝗻𝗼𝗶𝗱 𝗺𝘂𝘀𝗶𝗰 𝗹𝗶𝘀𝘁."
#             )
#             await delay_play_messages((xeronoid_throw,), PLAY_REMOVER)
#             return
#     else:
#         await xep.xeronoid_show_playlist()
#         await xemsg.delete()
#         return
#     if group_call and group_call[-1].audio.file_unique_id \
#             == m_audio.audio.file_unique_id:
#         xeronoid_throw = await xemsg.reply_animation(
#         animation=xerolink,
#         caption=f"{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n🎧 𝙈𝙪𝙨𝙞𝙘 𝙖𝙡𝙧𝙚𝙖𝙙𝙮 𝙖𝙙𝙙𝙚𝙙. 𝙎𝙠𝙞𝙥𝙥𝙞𝙣𝙜!"
#         )
#         await delay_play_messages((xeronoid_throw, xemsg), PLAY_REMOVER)
#         return
#     group_call.append(m_audio)
#     if len(group_call) == 1:
#         cprint('🎧 𝗨𝘀𝗲𝗿 𝗮𝘀𝗸𝗲𝗱 𝘁𝗼 𝗽𝗹𝗮𝘆 𝗮𝘂𝗱𝗶𝗼', 'yellow', attrs=['reverse'])
#         m_status = await xemsg.reply_animation(
#         animation=xerolink,
#         caption=f"{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n🎧 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗶𝗻𝗴 𝗮𝗻𝗱 𝘁𝗿𝗮𝗻𝘀𝗰𝗼𝗱𝗶𝗻𝗴..."
#         )
#         await xeronoid_music_dl_handler(group_call[0])
#         group_call.input_filename = os.path.join(
#             client.workdir,
#             xeronoid_dl_dir,
#             f"{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n🎧 {group_call[0].audio.file_unique_id}.raw"
#             )
#         await xep.xeronoid_begin_clock()
#         await m_status.delete()
#         print(f"{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n🎧 𝗫𝗲𝗿𝗼𝗻𝗼𝗶𝗱 𝗶𝘀 𝗻𝗼𝘁 𝗽𝗹𝗮𝘆𝗶𝗻𝗴: {group_call[0].audio.title}" + f"\n𝗶𝗻 𝘁𝗵𝗲 𝗴𝗿𝗼𝘂𝗽 `{CHAT_ID}'s` 𝙫𝙤𝙞𝙘𝙚 𝙘𝙝𝙖𝙩'")
#     await xep.xeronoid_show_playlist()
#     for track in group_call[:2]:
#         await xeronoid_music_dl_handler(track)
#     if not xemsg.audio:
#         await xemsg.delete()
        
        
@Ӽɛʀօռօɨɖ.on_message(
xerofil.group
& ~xerofil.edited
& xeronoid_chat_check
& xerofil.command("play") | xerofil.audio)
async def play_track(client, xemsg: xeromsg):
    group_call = xep.group_call
    playlist_temp = xep.playlist_temp
    # check audio
    if xemsg.audio:
        if xemsg.audio.duration > (MAX_MIN * 60):
            reply = await xemsg.reply_text(
                f"audio which duration longer than "
                f"{str(MAX_MIN)} min won't be automatically "
                "added to playlist_temp"
            )
            await delay_play_messages((reply,), PLAY_REMOVER)
            return
        m_audio = xemsg
    elif xemsg.reply_to_message and xemsg.reply_to_message.audio:
        m_audio = xemsg.reply_to_message
        if m_audio.audio.duration > (MAX_HOUR * 60 * 60):
            reply = await xemsg.reply_text(
                f"audio which duration longer than "
                f"{str(MAX_HOUR)} hours won't be added to playlist_temp"
            )
            await delay_play_messages((reply,), PLAY_REMOVER)
            return
    else:
        await xep.send_playlist()
        await xemsg.delete()
        return
    # check already added
    if playlist_temp and playlist_temp[-1].audio.file_unique_id \
            == m_audio.audio.file_unique_id:
        reply = await xemsg.reply_text(f"already added")
        await delay_play_messages((reply, xemsg), PLAY_REMOVER)
        return
    # add to playlist_temp
    playlist_temp.append(m_audio)
    if len(playlist_temp) == 1:
        m_status = await xemsg.reply_text(
            f" downloading and transcoding..."
        )
        await xeronoid_music_dl_handler(playlist_temp[0])
        group_call.input_filename = os.path.join(
            client.workdir,
            xeronoid_dl_dir,
            f"{playlist_temp[0].audio.file_unique_id}.raw"
        )
        await xep.xeronoid_begin_clock()
        await m_status.delete()
        print(f"- START PLAYING: {playlist_temp[0].audio.title}")
    await xep.send_playlist()
    for track in playlist_temp[:2]:
        await xeronoid_music_dl_handler(track)
    if not xemsg.audio:
        await xemsg.delete()