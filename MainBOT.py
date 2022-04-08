import discord
import ctx
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$test'):
        await message.channel.send('Bot is functioning')

    elif message.content.startswith('$chart'):
        await message.channel.send(file=discord.File('C:\\Users\\S9jammon\\Documents\\GitHub\\DiscordBOT\\chart.png'))

client.run('OTU2NTk0MjA5NjY0NjkyMjY0.YjyfyA.YgZ-S-6A8HBYNxW4qJphew3K0aA')
