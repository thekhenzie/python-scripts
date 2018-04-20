import discord
import asyncio
import json
import time

client = discord.Client()

@client.event
async def on_message(message):

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.author.id == 'your user id' and message.content.startswith('!grinding'):
        loader = False
        if message.content.startswith('!grindingstart'):
            loader = True
            spam = message.content.split(' ')[1]

        if message.content.startswith('!grindingstop'):
            loader = False
            spam = 'aw'
           
        while True:
            await client.send_message(message.channel, spam)
            time.sleep(1)
  
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run('token', bot=False)
