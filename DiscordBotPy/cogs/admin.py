from discord.ext import commands
import asyncio, aiohttp
import discord


class Admin:
    """Admin-only commands that make the bot dynamic"""

    def __init__(self, client):
        self.client = client

    @commands.command(name='shutdown', hidden=True)
    async def shutdown(self):
        """Shuts down the current instance of the bot"""
        print('Test')
        await self.client.say(discord.__version__)
        
        

def setup(client):
    client.add_cog(Admin(client))

