import os
from aiogram import Router,types,F,Bot
from aiogram.filters import StateFilter
from aiogram.fsm.state import StatesGroup,State
from aiogram.fsm.context import FSMContext
from get_post_data import *
import inline_kbds
from dotenv import load_dotenv
load_dotenv()
CHANNEL_ID =os.getenv("CHANNEL_ID")
fsm=Router()
ADMIN_LIST=[1059422557,]
class AddData(StatesGroup):
    title=State()
    content = State()
    user_id = State()
    message_id=State()


@fsm.message(AddData.title,F.text)
async def fsm_title(message:types.Message, state:FSMContext):
    current_state = await state.get_state()
    if current_state:
        if len(message.text)<=30:
            await state.update_data(title=message.text)
            await message.answer("Напиши текст к посту")
            await state.set_state(AddData.content)
        else:
            await message.answer("Много символов (до 30)")
@fsm.message(AddData.content,F.text)
async def fsm_content(message:types.Message, state:FSMContext,bot:Bot):
    current_state = await state.get_state()
    if current_state:
        if len(message.text)<2000:
            await state.update_data(content=message.text)
            await finish(message, state, bot)

        else:
            await message.answer("Много символов (до 500)")

def escape_markdown(text):
    replacements = {
        "_": "\\_",
        "*": "\\*",
        "[": "\\[",
        "]": "\\]",
        "(": "\\(",
        ")": "\\)",
        "~": "\\~",
        "`": "\\`",
        ">": "\\>",
        "#": "\\#",
        "+": "\\+",
        "-": "\\-",
        "=": "\\=",
        "|": "\\|",
        "{": "\\{",
        "}": "\\}",
        ".": "\\.",
        "!": "\\!"
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text
async def finish(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()




    message_id = None
    sent_message = await message.answer(f"Пост {data['title']} отправлен на проверку")
    link=f"[ссылка на пользователя](tg://user?id={message.from_user.id})"
    title = escape_markdown(data['title'])
    content = escape_markdown(data['content'])
    message_text = f"\n\n{title}\n\n{content}\n\n{link}\n\n"

    for ad in ADMIN_LIST:
        await bot.send_message(ad, message_text, parse_mode="MarkdownV2",
                               reply_markup=inline_kbds.get_callback_btns({"Одобрить": f"approve_{sent_message.message_id}_{message.from_user.id}",
                                                                            "Отклонить": "reject_"}))

        if message_id is None:
            message_id = sent_message.message_id
            await state.update_data(message_id=message_id)
            print(sent_message)
    data = await state.get_data()
    await postposts(data)

    await state.clear()


