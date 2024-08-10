import logging

from aiogram import Bot, Dispatcher, executor, types
import requests

API_TOKEN = '7264394321:AAHGdiRAb8qWlp0hh_4tC94UMBhmVaqgdEk'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("""Hi!\nI'm Spotify!\nPowered by aiogram.
        /artist
        /album
        /song
    """)


@dp.message_handler(commands=['song'])
async def send_welcome(message: types.Message):
    song = requests.get(f'http://127.0.0.1:8000/api/song/')
    for song in song.json():
        await message.reply(f"""
        Title:{song['title']}\n
        Image:{song['image']}\n
        Artist:{song['album']['artist']}\n
        Album:{song['album']}
        """)


@dp.message_handler(commands=['album'])
async def send_welcome(message: types.Message):
    album = requests.get(f'http://127.0.0.1:8000/api/album/')
    for album in album.json():
        await message.reply(f"""
        Title:{album['title']}\n
        Artist:{album['artist']}
        """)


@dp.message_handler(commands=['artist'])
async def send_welcome(message: types.Message):
    artist = requests.get('http://127.0.0.1:8000/api/artist/')
    for artist in artist.json():
        await message.reply(f"""
        Name:{artist['first_name']}\n
        Last_name:{artist['last_name']}
        """)


@dp.message_handler()
async def send_welcome(message: types.Message):
    search_data = message.text
    song = requests.get(f'http://127.0.0.1:8000/api/song?search={search_data}')
    if song.json():
        for song in song.json():
            await message.reply(f"""
            Album:{song['album']['title']}\n
            Artist:
            First name:{song['album']['artist']['first_name']}\n
            Last name:{song['album']['artist']['last_name']}
            Title:{song['title'].title()}
            """)
    else:
        await message.reply("qoshiq topilmadi")


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
