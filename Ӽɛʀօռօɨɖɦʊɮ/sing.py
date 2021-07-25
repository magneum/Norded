"""⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝
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
⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝"""


from ɖօօʍ_ʀօօʍ import *
from ǟʊȶօ_քʊʀɢɛʀ import *
from ʟɨɮʀǟʀʏ_ʀօօʍ import *
from Ӽɛʀօռօɨɖʍʊֆɨƈ import *
from ƈʊֆȶօʍ_ʄɨʟȶɛʀֆ import *


@Client.on_message(
    filters.group
    & ~filters.edited
    & current_vc
    & (filters.regex("^(\\/|!)sing$") | filters.audio)
)
async def play_track(client, m: Message):
    group_call = xep.group_call
    playlist = xep.playlist
    # check audio
    if m.audio:
        if m.audio.duration > (MAX_MIN * 60):
            reply = await m.reply_text(
                f"{emoji.ROBOT} audio which duration longer than "
                f"{str(MAX_MIN)} min won't be automatically "
                "added to playlist"
            )
            await delay_sing_messages((reply,), CLEAN_REMOVER)
            return
        m_audio = m
    elif m.reply_to_message and m.reply_to_message.audio:
        m_audio = m.reply_to_message
        if m_audio.audio.duration > (MAX_HOUR * 60 * 60):
            reply = await m.reply_text(
                f"{emoji.ROBOT} audio which duration longer than "
                f"{str(MAX_HOUR)} hours won't be added to playlist"
            )
            await delay_sing_messages((reply,), CLEAN_REMOVER)
            return
    else:
        await xep.send_playlist()
        await m.delete()
        return
    # check already added
    if playlist and playlist[-1].audio.file_unique_id \
            == m_audio.audio.file_unique_id:
        reply = await m.reply_text(f"{emoji.ROBOT} already added")
        await delay_sing_messages((reply, m), CLEAN_REMOVER)
        return
    # add to playlist
    playlist.append(m_audio)
    if len(playlist) == 1:
        m_status = await m.reply_text(
            f"{emoji.INBOX_TRAY} downloading and transcoding..."
        )
        await download_audio(playlist[0])
        group_call.input_filename = os.path.join(
            client.workdir,
            DEFAULT_DOWNLOAD_DIR,
            f"{playlist[0].audio.file_unique_id}.raw"
        )
        await xep.update_start_time()
        await m_status.delete()
        print(f"- START PLAYING: {playlist[0].audio.title}")
    await xep.send_playlist()
    for track in playlist[:2]:
        await download_audio(track)
    if not m.audio:
        await m.delete()