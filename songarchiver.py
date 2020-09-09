import discord
from discord.ext.commands import Bot
from datetime import datetime

bot = Bot(command_prefix = "?")

@bot.event
async def on_ready():
    print('Ready')

@bot.command(name='record',
                description='records all songs played and saves to a file',
                brief='RECORD',
                aliases=['rec'])
async def record(ctx):
    recording = 1

    chan = ctx.channel

    now = datetime.now()
    now = now.strftime('%m-%d-%Y_%H-%M-%S')
    fileName = 'DiscordRecord/'+ str(now) + '.txt'

    f = open(fileName,'w+')

    await ctx.send('Recording all song requests from this channel')
    chat = await getInput(chan)
    while recording:
        if chat.startswith('-play') or chat.startswith('!play'):
            f.write(chat[6:] + '\n')
            await ctx.send('Recorded')
            chat = await getInput(chan)
        elif chat == '?srec' or chat == '?stoprecord':
            recording = 0
            await ctx.send('Stopped recording song requests from this channel')

    return

async def getInput(channel):
    input = await bot.wait_for('message')
    while input.channel != channel or input.author.bot:
        input = await bot.wait_for('message')

    return input.content

bot.run('NjA2MDMzMTE0OTc1OTYxMDg4.XUFLpg.gXVzVgz2fzbxG3GHlrGw2LTHD_8')
