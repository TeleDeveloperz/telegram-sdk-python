import os
import aiohttp
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
API_BASE_URL = f'https://api.telegram.org/bot{BOT_TOKEN}'

async def get_me():
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{API_BASE_URL}/getMe') as response:
            return await response.json()

async def get_user_profile_photos(user_id: int):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{API_BASE_URL}/getUserProfilePhotos', params={'user_id': user_id}) as response:
            return await response.json()
