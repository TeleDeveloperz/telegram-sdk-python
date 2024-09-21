import os

# Function to create a directory if it doesn't exist
def create_directory(path):
    if path:  # Ensure that the path is not an empty string
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Created directory: {path}")
        else:
            print(f"Directory {path} already exists")

# Function to create a file with content
def create_file(file_path, content):
    create_directory(os.path.dirname(file_path))  # Now handles empty directory paths
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created file: {file_path}")

# Project structure
print("Setting up Python TWA SDK project...")

# Create directories
create_directory("teledeveloperz/twa_sdk")
create_directory("tests")

# Create setup.py
setup_py_content = '''from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='teledeveloperz',
    version='0.1.0',
    author='TeleDeveloperz',
    author_email='your.email@example.com',
    description='Enhanced Telegram Web Apps (TWA) SDK for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/teledeveloperz/telegram-sdk-python',
    packages=find_packages(),
    install_requires=[
        'requests',
        'aiohttp',
        'python-dotenv',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.7',
)
'''
create_file("setup.py", setup_py_content)

# Create __init__.py
init_py_content = '''from .twa_sdk import TWASDK
'''
create_file("teledeveloperz/__init__.py", init_py_content)

# Create twa_sdk.py
twa_sdk_content = '''from .user import TelegramUser
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
'''
create_file("teledeveloperz/twa_sdk/__init__.py", twa_sdk_content)

# Create user.py
user_py_content = '''from .utils import calculate_account_age

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
'''
create_file("teledeveloperz/twa_sdk/user.py", user_py_content)

# Create api.py
api_py_content = '''import os
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
'''
create_file("teledeveloperz/twa_sdk/api.py", api_py_content)

# Create utils.py
utils_py_content = '''import time

def calculate_account_age(user_id: int) -> int:
    creation_date = 1356998400  # January 1, 2013 (Telegram's launch date)
    return int((time.time() - creation_date) / 86400)

def validate_init_data(init_data: str) -> bool:
    # TODO: Implement proper validation logic
    return True
'''
create_file("teledeveloperz/twa_sdk/utils.py", utils_py_content)

# Create test_twa_sdk.py
test_py_content = '''import pytest
from teledeveloperz import TWASDK

@pytest.fixture
def mock_init_data():
    return str({
        'user': {
            'id': 123456789,
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'language_code': 'en',
            'is_premium': True
        },
        'auth_date': int(time.time()),
        'hash': 'mock_hash'
    })

def test_user_data(mock_init_data):
    sdk = TWASDK(mock_init_data)
    assert sdk.user.get_id() == 123456789
    assert sdk.user.get_username() == 'johndoe'
    assert sdk.user.get_full_name() == 'John Doe'
    assert sdk.user.get_language_code() == 'en'
    assert sdk.user.is_premium() == True
    assert isinstance(sdk.user.get_account_age(), int)

@pytest.mark.asyncio
async def test_get_bot_info(mock_init_data):
    sdk = TWASDK(mock_init_data)
    bot_info = await sdk.get_bot_info()
    assert isinstance(bot_info, dict)
    assert 'id' in bot_info
    assert 'first_name' in bot_info
    assert 'username' in bot_info
'''
create_file("tests/test_twa_sdk.py", test_py_content)

