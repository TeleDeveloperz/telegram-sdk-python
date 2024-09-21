from setuptools import setup, find_packages

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
