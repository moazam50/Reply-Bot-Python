import discord
import requests
import json
import os

def get_meme():
    """Fetch a random meme URL from the Meme API."""
    try:
        response = requests.get('https://meme-api.com/gimme', timeout=5)
        response.raise_for_status()
        json_data = response.json()
        return json_data.get('url', 'No meme found.')
    except (requests.RequestException, KeyError) as e:
        print(f"Error fetching meme: {e}")
        return "Couldn't fetch a meme at the moment. Try again later!"

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}!')

    async def on_message(self, message):
        # Ignore messages from the bot itself
        if message.author == self.user:
            return

        # Handle the $meme command
        if message.content.startswith('$meme'):
            meme_url = get_meme()
            await message.channel.send(meme_url)

        # Respond to "hello" (case-insensitive) in messages
        if 'hello' in message.content.lower():
            await message.channel.send('Hello World!')

        # Respond to "Hello" (case-sensitive)
        if message.content.startswith('Hello'):
            await message.channel.send('Bye Bye!')

# Set up intents
intents = discord.Intents.default()
intents.message_content = True

# Initialize client
client = MyClient(intents=intents)

# Run the bot using a token from an environment variable
TOKEN = os.getenv('DISCORD_TOKEN')
if TOKEN:
    client.run(TOKEN)
else:
    print("Error: DISCORD_TOKEN environment variable not set.")