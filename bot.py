from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user = message.from_user

    link = await bot.create_chat_invite_link(
        chat_id=CHANNEL_ID,
        member_limit=1,
        name=f"invite_for_{user.id}"
    )

    join_btn = InlineKeyboardMarkup().add(
        InlineKeyboardButton("👉 Click Here to Join", url=link.invite_link)
    )

    text = (
        f"🔥 **Wᴇʟᴄᴏᴍᴇ {user.first_name}!**\n\n"
        f"vᴀʟɪᴅ Fᴏʀ Oɴᴇ Uꜱᴇʀ Oɴʟʏ. Kᴇᴇᴘ Iᴛ Sᴀꜰᴇ!"
    )

    await message.answer(text, reply_markup=join_btn, parse_mode="Markdown")

if __name__ == '__main__':
    print("Bot is running... ✅")
    executor.start_polling(dp, skip_updates=True)
