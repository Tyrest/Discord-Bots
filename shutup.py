import discord
from discord.ext.commands import Bot
import random

bot = Bot(command_prefix = "?")

speaks = False

@bot.event
async def on_ready():
    print('Ready')

@bot.event
async def on_typing(channel, user, when):
    oosh = 'OOsh02#7936'
    tyresty = 'Tyresty#8394'
    drinnok = 'Drinnok#6792'
    josh = 'RubixQber#3402'
    jonathan = 'luckySquid#0849'

    global speaks
    if speaks:
        if str(user) == oosh:
            await channel.send('Yo Oosh Doosh Bush - ya better not press that enter button or we gonna come and get ya')
        elif str(user) == tyresty:
            await channel.send('Thank you for blessing us with your words great Tyresty. I anticipate nothing more than that moment when you press the enter button and bless us with the art that is your messages')
        elif str(user) == drinnok:
            await channel.send('GOD SPEAKS (everyone quiet down)')
        elif str(user) == josh:
            await channel.send('Have you no shame attempting to speak under the great rule of Tyresty? You are merely a subject of his rule. Know your place')
        elif str(user) == jonathan:
            await channel.send('You better hope the chat you\'re about to send is readable')
        return

@bot.command(name='silence',
                description="silences the bot",
                brief="a silent bot",
                aliases=[])
async def silence(ctx):
    global speaks
    await ctx.send('As you wish')
    speaks = not speaks
    if not speaks:
        await ctx.send('I will now be silent')
    else:
        await ctx.send('I will now make fun of Jonathan')

bot.run('NjA2MDMzMTE0OTc1OTYxMDg4.XUFKUg.tUTMgLdjJ7YteNsXJDr1yMwk1aI')