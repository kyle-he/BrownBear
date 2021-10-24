import discord
from datetime import datetime

import config

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message_edit(before_message, after_message):
    if before_message.author == client.user:
        return

    if before_message.channel.id in config.CHANNEL_WATCHLIST:
        channel = client.get_channel(config.LOG_CHANNEL)

        attachments = [await file.to_file() for file in before_message.attachments]

        await channel.send(
            content = f"Edited Message in **{before_message.channel.name}** \n \n`{before_message.created_at.strftime('%m/%d/%Y, %H:%M:%S')}` {before_message.author.id}: \n `before`: {before_message.clean_content} \n `after`: {after_message.clean_content} " ,
            files = attachments
        )


@client.event
async def on_message_delete(message):
    if message.author == client.user:
        return

    if message.channel.id in config.CHANNEL_WATCHLIST:
        channel = client.get_channel(config.LOG_CHANNEL)

        attachments = [await file.to_file() for file in message.attachments]

        await channel.send(
            content = f"Deleted Message in **{message.channel.name}** \n \n`{message.created_at.strftime('%m/%d/%Y, %H:%M:%S')}` {message.author.id}: {message.clean_content}",
            files = attachments
        )

client.run(config.TOKEN)