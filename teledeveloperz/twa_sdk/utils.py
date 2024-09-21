import time

def calculate_account_age(user_id: int) -> int:
    creation_date = 1356998400  # January 1, 2013 (Telegram's launch date)
    return int((time.time() - creation_date) / 86400)

def validate_init_data(init_data: str) -> bool:
    # TODO: Implement proper validation logic
    return True
