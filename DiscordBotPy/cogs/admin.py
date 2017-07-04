from discord.ext import commands
import asyncio, aiohttp
import discord


class Admin:
    """Admin-only commands that make the bot dynamic"""

    def __init__(self, client):
        self.client = client

    @commands.command(hidden=True)
    async def load(self, *, module : str):
        """Loads a module."""
        module = module.lower()
        try:
            self.client.load_extension(module)
        except Exception as e:
            await self.client.say('\N{FIRE} {}: {}'.format(type(e).__name__, e))
        else:
            await self.client.say('Module: **{}** is now enabled!'.format(module))

    @commands.command(hidden=True)
    async def unload(self, *, module : str):
        """Unloads a module."""
        module = module.lower()
        try:
            self.client.unload_extension(module)
        except Exception as e:
            await self.client.say('\N{FIRE} {}: {}'.format(type(e).__name__, e))
        else:
            await self.client.say('Module: **{}** is now disabled!'.format(module))


def setup(client):
    client.add_cog(Admin(client))

