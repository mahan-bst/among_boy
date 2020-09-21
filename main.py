import discord
from discord.ext import commands
API_TOKEN = 'NzU2ODkwMjU3NDg3NjkxODQ3.X2Ya-w.cx0CzdHU3HAyA5rM9D32wpqC9kY'


bot = commands.Bot(command_prefix='?')


@bot.event
async def on_ready():
    print('im ready')


@bot.command()
async def ping(ext):
    await ext.send('pong! {0} ms'.format(round(bot.latency*1000)))


@bot.command()
async def start(ext):
    if ext.author.id == 752517697853718669:
        await ext.author.voice.channel.set_permissions(ext.guild.default_role, speak=False)
        await ext.send(
            'Done! hamaro mute krdm tokhm dary harf bezan kale kiri :red_circle: :angry:')
    else:
        await ext.send('fekr kardi man kharam man faqat be @maahaanbst javab midam na be toie ......')


@bot.command()
async def stop(ext):
    if ext.author.id == 752517697853718669:
        await ext.author.voice.channel.set_permissions(ext.guild.default_role, speak=None)
        await ext.send(
            'Done! hala mitooni harf bezani kale kiri :red_circle: :angry:')
    else:
        await ext.send('fekr kardi man kharam man faqat be @maahaanbst javab midam na be toie ......')


@bot.event
# off caps sensitivity
async def on_message(message):
    message.content = message.content.lower().replace(' ', '')
    await bot.process_commands(message)


bot.run(API_TOKEN)
