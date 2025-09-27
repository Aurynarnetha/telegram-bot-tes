import asyncio
from aiogram import Bot, Dispatcher, types, F

API_TOKEN = "8338685944:AAHJ7nX9h7pWvoAO4MO62RGgxCjx9PLUypk"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Command /start
@dp.message(F.text == "/start")
async def send_welcome(message: types.Message):
    await message.reply("Halo! Ini bot forum anak. Kamu bisa curhat di sini 😊")

# Jawab semua pesan teks biasa
@dp.message(F.text)
async def echo(message: types.Message):
    await message.answer(f"Kamu bilang: {message.text}\n(📌 pesanmu akan diteruskan ke admin juga)")

async def main():
    # Mulai polling
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())