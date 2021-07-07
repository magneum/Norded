from HEIST import *
from ᴠᴏᴋᴀʟɪᴢᴇ import *
from ᴇᴘɪꜱᴛʟᴇ import *
from VEhJU0lTVVNFREZPUlhFUk9OT0lE import *


@ɦɖɛ.on_message(
demon_killer_sigki
& senzo_kryo_ni
& misa_misa
&filters.command(
"usage",
prefixes="/"))
async def usage(_, ryui: Message):
    drip = await ryui.reply_text("ᴀꜱᴋɪɴɢ ʜᴇʀᴏᴋᴜ ᴛᴏ ꜱᴇɴᴅ ᴛʜᴇ ꜱᴇʀᴠᴇʀ ꜰᴇᴇᴅꜱ")
    await asyncio.sleep(2)
    await drip.edit("🕐")
    await drip.edit("🕑")
    await drip.edit("🕒")
    await drip.delete()
    useragent = (UAA,UAB,UAC)
    user_id = Heroku.account().id
    headers = {
        "User-Agent":
        useragent,
        "Authorization":
        f"Bearer {HPI}",
        "Accept":
        HPJN,
    }
    path = "/accounts/" + user_id + "/actions/get-quota"
    r = requests.get(heroku_api + path, headers=headers)
    if r.status_code != 200:
        return await ryui.edit(
            "`Error: something bad happened`\n\n" f">.`{r.reason}`\n"
        )
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]

    """ - Used - """
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)

    """ - Current - """
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)
    cate = await ryui.reply_photo(
    ZV0,
    caption=f"""
一═デ🦋 **Ӽɛʀօռօɨɖ** 🦋デ═一
**🍑ʏᴏᴜʀ ʜᴇʀᴏᴋᴜ ᴜꜱᴀɢᴇ ꜰᴏʀ ᴛʜɪꜱ ᴍᴏɴᴛʜ🍑**
    𝕆山ᑎER: {HON}

** 𝘋𝘺𝘯𝘰 𝘜𝘴𝘦𝘥 𝘶𝘱 𝘣𝘺**  
{HPN}** 
    `{AppHours}hrs` | `{AppMinutes}mins` | `{AppPercentage}%`

🍇𝘋𝘺𝘯𝘰 𝘓𝘦𝘧𝘵 𝘧𝘰𝘳 𝘵𝘩𝘪𝘴 𝘮𝘰𝘯𝘵𝘩🍇
    `{hours}hrs` | `{minutes}mins` | `{percentage}%`


**Dҽʋ Mҽɳƚισɳ:**
    @hypevoidsoul
一═デ🦋 **Ӽɛʀօռօɨɖ** 🦋デ═一
""")
    await asyncio.sleep(8)
    await cate.delete()
    return 