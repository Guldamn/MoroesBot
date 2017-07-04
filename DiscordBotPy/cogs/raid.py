from discord.ext import commands
import json

import re
import json
import discord
import enum
import datetime
import asyncio
import argparse, shlex
import logging

class Raid:
    """Controls the anti-raid protection"""

    def __init__(self, client):
        self.client = client

    @commands.group(aliases=['raids'], pass_context=True, invoke_without_command=True, no_pm=True)
    async def raid(self, ctx):
        """Controls the defensive measures against a Discord raid.
        Calling this command with no arguments will inform the user of the dangers of this command.
        You must have Manage Server permissions or the Bot Admin role to invoke any of these commands.
        """

    @raid.command(name='on', aliases=['enable', 'enabled'], pass_context=True, no_pm=True)
    async def raid_on(self, ctx, *, channel: discord.Channel = None):
        
        if channel is None:
            channel = ctx.message.channel
            if channel.type is not discord.ChannelType.text:
                return await self.client.say('That is not a text channel.')

            guild = ctx.message.server
            try:
                await self.client.edit_server(guild, verification_level=discord.VerificationLevel.table_flip)
                await self.client.say(':crossed_swords: Raid mode has been enabled.')
            except discord.HTTPException:
                await self.client.say('\N{FIRE}: Could not set verification level.')

    @raid.command(name='off', aliases=['disable', 'disabled'], pass_context=True, no_pm=True)
    async def raid_off(self, ctx):
        
        guild = ctx.message.server
           
        try:
            await self.client.edit_server(guild, verification_level=discord.VerificationLevel.low);
            await self.client.say(':dove: Peace has been restored.')
        except discord.HTTPException:
            await self.client.say("\N{WARNING SIGN}: Could not set verification level.")





def setup(client):
    client.add_cog(Raid(client))
