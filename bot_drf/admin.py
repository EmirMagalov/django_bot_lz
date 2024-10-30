from aiogram import Router,types,F,Bot
admin_router=Router()
from get_post_data import *
import os
from dotenv import load_dotenv
load_dotenv()
CHANNEL_ID =os.getenv("CHANNEL_ID")
@admin_router.callback_query(F.data.startswith("approve_"))
async def approve(callback:types.CallbackQuery,bot:Bot):
    message_data = callback.data.split('_')
    message_id = int(message_data[1])
    user_id = int(message_data[2])
    sent_message =await bot.forward_message(chat_id=CHANNEL_ID, from_chat_id=callback.message.chat.id, message_id=callback.message.message_id)


    new_data={
        "message_id":sent_message.message_id,
        "user_id":user_id
    }

    await putonepostadmin(int(message_id),new_data)

    await callback.message.delete()


@admin_router.callback_query(F.data.startswith("reject_"))
async def reject(callback:types.CallbackQuery,bot:Bot):
    await callback.message.delete()