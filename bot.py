import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.types import Message
from prepare_data import get_message

TOKEN = os.environ.get('NBT_ACCESS_TOKEN')

# All handlers should be attached to the Router (or Dispatcher)
router = Router()


@router.message(Command(commands=["start"]))
async def command_start_handler(message: Message) -> Message:
    return await message.answer(get_message())


@router.message()
async def echo_handler(message: types.Message) -> None:
    try:
        # Send copy of the received message
        await message.answer("Для получения курсов валют отправь команду старт")
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Для получения курсов валют отправь команду старт")


async def main() -> None:
    # Dispatcher is a root router
    dp = Dispatcher()
    # ... and all other routers should be attached to Dispatcher
    dp.include_router(router)

    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode="HTML")
    # And the run events dispatching
    await dp.start_polling(bot)


def run():
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


if __name__ == '__main__':
    run()
