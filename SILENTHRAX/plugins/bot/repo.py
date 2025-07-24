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
async def repo(_, msg):
    buttons = [
        [ 
            InlineKeyboardButton("💠 𝖠ᴅᴅ ᴍᴇ 𝖡ᴀʙʏ 💠", url="https://t.me/PakhiMusic_Bot?startgroup=true")
        ],
        [
            InlineKeyboardButton("𝑷𝑨𝑲𝑯𝑰 𝑴𝑼𝑺𝑰𝑪", url="https://t.me/UFC_UPDATES"),
            InlineKeyboardButton("𝚻꯭ᴀᴍᴀɴɴᴀ ꭙ 𝚳꯭ᴜꜱɪᴄ", url="https://t.me/TAMANNA_MUSIC_BOT?start=_tgr_fBSoVjdmODhl")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    await msg.reply_video(
        video="https://files.catbox.moe/9o3s0u.mp4",
        caption=start_txt,
        reply_markup=reply_markup
    )
