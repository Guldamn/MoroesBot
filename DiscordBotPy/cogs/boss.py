from discord.ext import commands
import json
import sqlite3

class Boss:
    # ToS boss module.
    # Written by Suurikarhu (Draenor EU)
    # This code has been produced with the help of Alusen, Arkh, and Blankies of the Learning Warcraft Discord community.

    def __init__(self, client):
        self.client = client
        

    @commands.command(name='boss', pass_context=True, invoke_without_command=False)
    async def boss(self, ctx, *, query : str):
        """Shows a basic list of guidelines to the Tomb of Sargeras raid encounters"""
        boss = query.lower()
        conn = sqlite3.connect('moroes.db')
        db = conn.cursor()
        db.execute("SELECT * FROM bosses WHERE name=?", (boss,))
        data = db.fetchone()

        if data is None:
            await self.client.say("There is no boss called {}".format(boss))
        else:
            await self.client.say(data[2])


def setup(client):
    client.add_cog(Boss(client))



