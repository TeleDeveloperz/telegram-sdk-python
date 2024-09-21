from .utils import calculate_account_age

class TelegramUser:
    def __init__(self, web_app_info):
        self.user = web_app_info.get('user', {})

    def get_id(self):
        return self.user.get('id')

    def get_username(self):
        return self.user.get('username')

    def get_full_name(self):
        return f"{self.user.get('first_name', '')} {self.user.get('last_name', '')}".strip()

    def get_language_code(self):
        return self.user.get('language_code')

    def is_premium(self):
        return self.user.get('is_premium', False)

    def get_account_age(self):
        return calculate_account_age(self.get_id())
