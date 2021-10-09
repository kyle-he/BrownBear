import discord
from datetime import datetime

import config

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message_delete(message):
    if message.author == client.user:
        return

    if message.channel.id in config.CHANNEL_WATCHLIST:
        channel = client.get_channel(config.LOG_CHANNEL)

        attachments = [await file.to_file() for file in message.attachments]

        await channel.send(
            content = f"Deleted Message in **{message.channel.name}** \n \n`{message.created_at.strftime('%m/%d/%Y, %H:%M:%S')}` {message.author.name}: {message.clean_content}",
            files = attachments
        )

client.run(config.TOKEN)