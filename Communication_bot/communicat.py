import discord
import random
from discord.ext import tasks # needed for tasks
import datetime # for dat time objects
import os

client = discord.Client()

TOKEN = 'OTI4NDMwMTk1NzEzNjcxMjQ5.YdYqAA.YkiTkHjKImz2lUgO2zNCnnBux5o'
@client.event
async def on_ready():
    print(f'{client.user.name} Ready to talk')
@client.event
async def on_member_join(member):
    print(f"{member} Welcome!")

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)  # which channel the message is coming
    print(f'{username}: {user_message} ({channel})')  # showing in code everything.

    if message.author == client.user:  # so the bot don't keep answering itself.
        return

    if message.channel.name == 'general':
        if user_message.lower() == '!hello':
            await message.channel.send(f'Hello {username}')
            return
        elif user_message.lower() == '!name':
            response = f'My Name is RoboKrupp'
            await message.channel.send(response)
            return
        elif user_message.lower() == '!random':
            response = f'This is your number : {random.randrange(1000)}'
            await message.channel.send(response)
        elif user_message.lower() == '!q':
            response = f'How may i assist you {username} ?'
            await message.channel.send(response)
            return

@client.event
async def on_member_remove(member):
    print(f"{member} Good bye!")

client.run(TOKEN)