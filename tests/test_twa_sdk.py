import pytest
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
