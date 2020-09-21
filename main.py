import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import os


bot = commands.Bot(command_prefix='?')


@bot.event
async def on_ready():
    print('im ready')


@bot.command()
async def ping(ext):
    await ext.send('man hamishe onlinam koskhol ! {0} ms'.format(round(bot.latency*1000)))


@bot.command()
@has_permissions(administrator=True)
async def start(ext):
    if ext.author.voice is not None:
        await ext.author.voice.channel.set_permissions(ext.guild.default_role, speak=False)
        await ext.send(
            'Done! hamaro mute krdm tokhm dary harf bezan kale kiri :red_circle: :angry:')
    else:
        await ext.send('koskhol boro too ye voice channel')


@bot.command()
@has_permissions(administrator=True)
async def stop(ext):
    if ext.author.voice is not None:
        await ext.author.voice.channel.set_permissions(ext.guild.default_role, speak=None)
        await ext.send(
            'Done! hala mitooni harf bezani kale kiri :red_circle: :angry:')
    else:
        await ext.send('koskhol boro too ye voice channel')


@start.error
async def start_error(error, ext):
    print(error)


@stop.error
async def stop_error(error, ext):
    print(error)


bot.run('NzU2ODkwMjU3NDg3NjkxODQ3.X2Ya-w.sjC8CVcxPmyWCrzwJT8Zr7Gxxuw')
