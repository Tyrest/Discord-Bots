import discord
from discord.ext.commands import Bot
import random

bot = Bot(command_prefix = "?")

commandStage = 0

@bot.event
async def on_ready():
    print('Ready')

@bot.command(name='roll',
                description="rolls a number of 6 sided dice",
                brief="dice rolling mania",
                aliases=[])
async def roll(ctx):
    await ctx.send('How many dice?')
    async def on_message(input):
        ctx.send('Rolling' + input + 'dice')
        rolls = int(input,10)
        total = 0
        for x in range(rolls):
            roll = random.randint(1, 6)
            total += roll
            await ctx.send(roll)
        await ctx.send('Total was: ' + str(total))

    return

bot.run('NjA2MDMzMTE0OTc1OTYxMDg4.XUFLpg.gXVzVgz2fzbxG3GHlrGw2LTHD_8')
