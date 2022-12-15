# This example requires the 'message_content' intent.

import logging
import discord

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Hello'):
        await message.channel.send('Hello there! :sunglasses:')  
    
    if message.content.startswith('.zoom Eoji.name'):
        await message.channel.send(Emoji.name.url)

client.run('MTA0MTI2NTIyOTA5MjM3NjYyNg.Ge1JF_.2hhWSuAGtuwFOf_of9gHORihwxF4WTDNavGkMk', log_handler=handler)
