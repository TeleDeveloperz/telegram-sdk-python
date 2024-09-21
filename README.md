An enhanced Python SDK for Telegram Web Apps (TWA), providing easy access to user data and Telegram Bot API functionality.

## Features

- Easy access to TWA user data
- Integration with Telegram Bot API
- Utility functions for common TWA operations

## Installation

```bash
pip install teledeveloperz
```

## Usage

```python
from teledeveloperz import TWASDK
import asyncio

# Initialize the SDK with the TWA init data
sdk = TWASDK(web_app_init_data)

# Access user information
print(sdk.user.get_full_name())

# Make API calls
async def get_bot_info():
    bot_info = await sdk.get_bot_info()
    print('Bot info:', bot_info)

asyncio.run(get_bot_info())
```

## Development

To set up the project for development:

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests: `pytest tests/`
