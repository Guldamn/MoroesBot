from discord.ext import commands
import asyncio, aiohttp
import discord
from collections import namedtuple
import json
import urllib3



class Armory:
    """Commands that allow the user to interact with the Raider.IO API."""

    
    
    def __init__(self, client):
        self.client = client

    @commands.command(name='affixes', hidden=True)
    async def affixes(self):
        """Shows the weekly Mythic+ affixes and their description"""

        http = urllib3.PoolManager
        r = http().request(
            'GET',
            'https://raider.io/api/v1/mythic-plus/affixes?region=us',
            fields = {},
            headers = {}
            )
        data = json.loads(r.data.decode('utf-8'))
        msg = 'This week: **' +data['title'] + '**\n'
        for i in data['affix_details']:
            msg = msg + '*' + i['description'] + '*\n'

        await self.client.say(msg)

        


    @commands.command(name='armory', hidden=True)
    async def armory(self, *, query : str):
        """Shows information from the characters armory if found"""
        
        args = query.split(" ")
        if len(args) < 3:
            await self.client.say('Please provide the region, realm, and name (Example: !armory eu draenor suurikarhu).')
            return
        http = urllib3.PoolManager
        r = http().request(
            method = 'GET',
            url = 'https://raider.io/api/v1/characters/profile',
            fields={'region': args[0],
                    'realm': args[1],
                    'name': args[2],
                    'fields': 'gear,raid_progression,mythic_plusscores'},
            headers={})
        data = json.loads(r.data.decode('utf-8'))
        await self.client.say('__{0} - {1} {2} ({3}/{4})__'.format(data['name'], data['active_spec_name'], data['class'], data['gear']['item_level_equipped'], data['gear']['item_level_total']))
        await self.client.say('Raid Progress \nEN: {0}, TOV: {1}, NH: {2}, TOS: {3}'.format(data['raid_progression']['the-emerald-nightmare']['summary'], data['raid_progression']['trial-of-valor']['summary'], data['raid_progression']['the-nighthold']['summary'], data['raid_progression']['tomb-of-sargeras']['summary']))
        
        

def setup(client):
    client.add_cog(Armory(client))
