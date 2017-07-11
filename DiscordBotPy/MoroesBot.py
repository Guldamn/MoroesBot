from discord.ext import commands
import discord
import asyncio
import logging
import json

description = """Hello I am a bot written by King WeakAura I to provide some sweet commands!"""

initial_extensions = [
    'cogs.admin',
    'cogs.armory',
    'cogs.icyveins',
    'cogs.boss']

logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(messages)s'))
logger.addHandler(handler)

help_attrs = dict(hidden=True)

prefix = ['!', '\N{HEAVY EXCLAMATION MARK SYMBOL}']
client = commands.Bot(command_prefix=prefix, description=description, pm_Help=None, help_attrs=help_attrs)

@client.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.NoPrivateMessage):
        await client.send_message(ctx.message.author, "This command cannot be used in private messages.")
    if isinstance(error, commands.DisabledCommand):
        await client.send_message(ctx.message.author, "This command has been disabled and cannot be used.")
    if isinstance(error, commands.CommandInvokeError):
        await client.send_message(ctx.message.author, "Something went horribly wrong executing this command. Contact King WeakAura I.")
        print(error)

@client.event
async def on_ready():
    print('Moroes is serving you using Discord.PY', discord.__version__)
    print('Moroes has enabled {} extensions!'.format(len(initial_extensions)))
    print('---------------------------------------------')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    await client.process_commands(message)

def load_config():
    with open('config.json') as c:
        return json.load(c)

if __name__ == '__main__':
    
    config = load_config()

    for extension in initial_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))

client.run('MjkxODczMjI2NDEyNTIzNTIw.DD0C1Q.4tqLZWXSiUrH4ODrj9W9AMW1Tag')

