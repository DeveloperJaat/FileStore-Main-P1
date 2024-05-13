#(©)codeflix_bots

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>DOCTORx𝟿𝟾</a>\n○ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/MoviesHubFree4You'>MᴏᴠɪᴇsHᴜʙFʀᴇᴇ𝟺Yᴏᴜ</a>\n○ ᴍᴏᴠɪᴇs ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/MoviesFree4You_Updates'>MᴏᴠɪᴇsFʀᴇᴇ𝟺Yᴏᴜ Uᴘᴅᴀᴛᴇs</a>\n○ Tʜᴇᴀᴛʀᴇ Mᴏᴠɪᴇs : <a href='https://t.me/+XOLcWbK66Gk2MTUy'>Mғ𝟺ʏ Tʜᴇᴀᴛʀᴇ Mᴏᴠɪᴇs 🎭</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🎭 Mғ𝟺ʏ Rᴇǫᴜᴇsᴛ', url='https://t.me/+9NJBWRn9BLliNjcy')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pas
