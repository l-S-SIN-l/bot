import discord
improt os

from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.command()
async def 안녕(ctx):
    await ctx.send('안녕하세요')

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
