#from Ӽɛʀօռօɨɖ import *
#from HEIST import *
#from ᴠᴏᴋᴀʟɪᴢᴇ import *
#from ᴇᴘɪꜱᴛʟᴇ import *
#from VEhJU0lTVVNFREZPUlhFUk9OT0lE import *
#group_calls = GroupCall(None, path_to_log_file='')


#@Ӽɛռ.on_message(
#filters.group
#& ~filters.edited
#& misa_misa
#& (filters.command(
#"vol",
#prefixes=WHITE_COMMAND) | filters.audio | filters.video))
#async def volume(_, message):
#    if len(message.command) < 2:
#        await message.reply_text('You forgot to pass volume (1-200)')
#    await group_calls.set_my_volume(volume=int(message.command[1]))
#    await message.reply_text(f'Volume changed to {message.command[1]}')
