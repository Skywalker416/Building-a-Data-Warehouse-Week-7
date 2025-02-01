from telethon.sync import TelegramClient
import json
import os

# Set your Telegram API credentials
API_ID = '25466824'  # Replace with your API ID
API_HASH = 'f13acb9c667058fd14308c84236152bd'  # Replace with your API Hash
SESSION_NAME = 'telegram_scraper'

# List of channels to scrape
CHANNELS = [
    'DoctorsET',
    'lobelia4cosmetics',
    'yetenaweg',
    'EAHCI'
]

# Create a directory to store images
os.makedirs("images", exist_ok=True)

# Connect to Telegram API
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

async def fetch_messages():
    scraped_data = []
    async with client:
        for channel in CHANNELS:
            async for message in client.iter_messages(channel, limit=100):
                message_data = {
                    "channel": channel,
                    "message_id": message.id,
                    "date": message.date.strftime('%Y-%m-%d %H:%M:%S'),
                    "text": message.text if message.text else "",
                    "sender_id": message.sender_id,
                    "image_path": None
                }
                
                # Download image if available
                if message.photo:
                    image_path = f"images/{channel}_{message.id}.jpg"
                    await message.download_media(file=image_path)
                    message_data["image_path"] = image_path

                scraped_data.append(message_data)

    # Save raw data to JSON
    with open("raw_data.json", "w", encoding="utf-8") as file:
        json.dump(scraped_data, file, indent=4, ensure_ascii=False)

client.loop.run_until_complete(fetch_messages())
