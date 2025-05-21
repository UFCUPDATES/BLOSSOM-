from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SILENTHRAX import app
from config import BOT_USERNAME
from SILENTHRAX.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
❥ ωєℓ¢σмє тσ 𝙱𝙻𝙾𝚂𝚂𝙾𝙼 𝐌ᴜsɪᴄ 

❥ ʙᴏᴛ ᴡɪᴛʜ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs
│❍ • ʏᴏᴜ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜꜱɪᴄ + ᴠɪᴅᴇᴏ •
│❍ • ʙᴇsᴛ ǫᴜɪʟɪᴛʏ ᴍᴜsɪᴄ sᴏᴜɴᴅ •
│❍ • ɴᴏ ʟᴀɢs + ɴᴏ ᴀᴅs •
│❍ • 24x7 ᴏɴʟɪɴᴇ sᴜᴘᴘᴏʀᴛ •
├──────────────

"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("💠 𝖠ᴅᴅ ᴍᴇ 𝖡ᴀʙʏ 💠", url=f"https://t.me/BLOSSOM_MUSIC_BOT?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗕𝗟𝗢𝗦𝗦𝗢𝗠 𝗠𝗨𝗦𝗜𝗖 ♪", url="https://t.me/UFC_UPDATES"),
          InlineKeyboardButton("𝚻꯭ᴀᴍᴀᴎᴎᴀ ꭙ 𝚳꯭ᴜᴤᴉᴒ", url="https://t.me/TAMANNA_MUSIC_BOT?start=_tgr_fBSoVjdmODhl"),
          ],
               [
                InlineKeyboardButton("𝚻꯭ᴀᴍᴀᴎᴎᴀ ꭙ 𝚳꯭ᴜᴤᴉᴒ", url=f"https://t.me/TAMANNA_MUSIC_BOT?start=_tgr_fBSoVjdmODhl"),
],
    ]
        
[
InlineKeyboardButton("𝗕𝗟𝗢𝗦𝗦𝗢𝗠 𝗠𝗨𝗦𝗜𝗖", url=f"https://t.me/BLOSSOM_MUSIC_BOT?startgroup=true"),

]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_video(
        video="https://files.catbox.moe/f1b5ye.mp4",
        caption=start_txt,
        reply_markup=reply_markup
    )
