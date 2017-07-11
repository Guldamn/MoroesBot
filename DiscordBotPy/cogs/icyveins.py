from discord.ext import commands
class IcyVeins:

    def __init__(self, client):
        self.client = client

    @commands.group(aliases=['class'], pass_context=True, invoke_without_command=True)
    async def intro(self):
      """Class commands"""  
    @intro.command(name='druid')
    async def druid(self):
        print('DK command invoked!')

    @intro.command(name='demonhunter', aliases=['dh'])
    async def demonhunter(self):
        print('DK command invoked!')

    @intro.command(name='deathknight', aliases=['dk'])
    async def deathknight(self):
        print('DK command invoked!')

    @intro.command(name='hunter')
    async def hunter(self):
        print('DK command invoked!')

    @intro.command(name='mage')
    async def mage(self):
        print('DK command invoked!')

    @intro.command(name='monk')
    async def monk(self):
        print('DK command invoked!')

    @intro.command(name='paladin', aliases=['pala'])
    async def paladin(self):
        print('DK command invoked!')

    @intro.command(name='rogue', aliases=['rouge'])
    async def rogue(self):
        print('DK command invoked!')

    @intro.command(name='shaman', aliases=['shammy'])
    async def shaman(self):
        print('DK command invoked!')

    @intro.command(name='warlock', aliases=['lock'])
    async def warlock(self):
        print('DK command invoked!')

    @intro.command(name='warrior', aliases=['warr'])
    async def warrior(self):
        print('DK command invoked!')


def setup(client):
    client.add_cog(IcyVeins(client))