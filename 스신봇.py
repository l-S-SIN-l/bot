import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.command()
async def 안녕(ctx):
    await ctx.send('안녕하세요')

client.run('ODE2NjUyMDc1OTc0NTI0OTY4.YD-Egw.5IIfT4XFiTX0Z5Uqd91c-3fHBK4')