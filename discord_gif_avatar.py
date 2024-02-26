import discord

intents = discord.Intents.default()
intents.messages = True
# Initialize the bot client
client = discord.Client(intents=intents)

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = 'YOUR_BOT_TOKEN'

# replace '/path/to/gif' with the Path to the image file you want to use as the new avatar
avatar_path = '/path/to/gif'

# Read the image file as bytes
with open(avatar_path, 'rb') as avatar_file:
    avatar_bytes = avatar_file.read()


@client.event
async def on_ready():
    # Change the bot's avatar
    await client.user.edit(avatar=avatar_bytes)
    print(f"Bot's avatar changed successfully!")

# Run the bot
client.run(TOKEN)
