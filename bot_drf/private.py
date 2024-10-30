from aiogram import Router, types, F,Bot
from aiogram.filters import CommandStart
from get_post_data import *
from fsm import AddData
import kbds
import inline_kbds
from aiogram.filters import StateFilter
from aiogram.fsm.state import StatesGroup,State
from aiogram.fsm.context import FSMContext
import os
from dotenv import load_dotenv
load_dotenv()
user_private_router=Router()
CHANNEL_ID =os.getenv("CHANNEL_ID")



@user_private_router.message(CommandStart())
async def start(message:types.Message,bot:Bot):

    user_id = message.from_user.id

    if await secur(user_id,bot):
        await message.answer(
            f"Привет {message.from_user.first_name}\nЭтот бот будет публиковать твои посты в канал \nhttps://t.me/tz_drf_lz",
            reply_markup=kbds.menu.as_markup(resize_keyboard=True))
    else:
        await message.answer(f"Пожалуйста, подпишитесь на канал https://t.me/tz_drf_lz, чтобы использовать бота!")
    # await bot.forward_message(CHANNEL_ID,from_chat_id=message.chat.id,message_id=message.message_id)

@user_private_router.message(F.text=="Добавить пост")
async def addpost(message:types.Message,state:FSMContext,bot:Bot):
    user_id = message.from_user.id
    if await secur(user_id,bot):
        await state.clear()
        await message.answer("Введите название поста")
        await state.set_state(AddData.title)
    else:
        await message.answer(f"Пожалуйста, подпишитесь на канал https://t.me/tz_drf_lz, чтобы использовать бота!")

@user_private_router.message(F.text=="Посты")
async def postsall(message:types.Message,state:FSMContext,bot:Bot):
    await state.clear()
    user_id=message.from_user.id
    if await secur(user_id,bot):
        p=await getpostusers(user_id)
        if p:
            for i in p:
                message_text = f"<b>{i['title']}</b>\n\n{i['content']}"
                await message.answer(message_text,parse_mode="HTML",reply_markup=inline_kbds.get_callback_btns({"Удалить":f"del_{i['id']}_{i['message_id']}"}))
        else:
            await message.answer("У вас нет ни одного поста")
    else:
        await message.answer(f"Пожалуйста, подпишитесь на канал https://t.me/tz_drf_lz, чтобы использовать бота!")
# @user_private_router.callback_query(F.data.startswith("red_"))
# async def red(callback:types.CallbackQuery,state:FSMContext):
#     post_id=int(callback.data.split('_')[-1])
#     user_post = await getonepost(post_id)
#     await callback.message.answer("Введите заголовок поста:")
#     await state.update_data(user_fsm_data=post_id)
#     await state.set_state(AddData.title)

@user_private_router.callback_query(F.data.startswith("del_"))
async def delete(callback:types.CallbackQuery,bot:Bot):
    post_data=callback.data.split('_')
    post_id=int(post_data[1])
    post_message_id=int(post_data[2])

    await del_post(post_id)
    await callback.message.delete()
    await bot.delete_message(CHANNEL_ID, post_message_id)



async def secur(user_id,bot):

    user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)

    if user_channel_status.status in ["member", "administrator", "creator"]:
        # await message.answer(f"Привет {message.from_user.first_name}\nЭтот бот будет публиковать твои посты в канал \nhttps://t.me/tz_drf_lz",reply_markup=kbds.menu.as_markup(resize_keyboard=True))
        return True
    else:
        # await message.answer(f"Пожалуйста, подпишитесь на канал https://t.me/tz_drf_lz, чтобы использовать бота!")
        return False


