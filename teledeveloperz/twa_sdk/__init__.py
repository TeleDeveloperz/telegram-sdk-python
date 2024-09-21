from .user import TelegramUser
from .api import get_me, get_user_profile_photos
from .utils import validate_init_data

class TWASDK:
    def __init__(self, init_data: str):
        if not validate_init_data(init_data):
            raise ValueError('Invalid init data')
        self.web_app_info = eval(init_data)
        self.user = TelegramUser(self.web_app_info)

    async def get_bot_info(self):
        return await get_me()

    async def get_user_profile_photos(self, user_id: int):
        return await get_user_profile_photos(user_id)
