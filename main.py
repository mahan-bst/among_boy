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
@has_permissions(mute_members=True)
async def start(ext):
    if ext.author.id == 752517697853718669 and ext.author.voice.channel:
        await ext.author.voice.channel.set_permissions(ext.guild.default_role, speak=False)
        await ext.send(
            'Done! hamaro mute krdm tokhm dary harf bezan kale kiri :red_circle: :angry:')
    else:
        await ext.send('fekr kardi man kharam man faqat be admina javab midam na be toie ......')


@bot.command()
@has_permissions(mute_members=True)
async def stop(ext):
    if (ext.author.id == 752517697853718669) and ext.author.voice.channel:
        await ext.author.voice.channel.set_permissions(ext.guild.default_role, speak=None)
        await ext.send(
            'Done! hala mitooni harf bezani kale kiri :red_circle: :angry:')
    else:
        await ext.send('fekr kardi man kharam man faqat be admina javab midam na be toie ......')


@start.error
async def start_error(ext):
    await ext.send('fekr kardi man kharam man faqat be admina javab midam na be toie ......')


@stop.error
async def stop_error(ext):
    await ext.send('fekr kardi man kharam man faqat be admina javab midam na be toie ......')


@bot.event
# off caps sensitivity
async def on_message(message):
    message.content = message.content.lower().replace(' ', '')
    await bot.process_commands(message)


bot.run(os.environ['token'])
