import discord
from discord.ext.commands import Bot

bot = Bot(command_prefix = "?")

@bot.command(name='terr',
                description="looks stuff up on the terraria wiki",
                brief="wiki finding op",
                aliases=[])
async def terr(ctx, search):
    toSearch = removeSpaces(search)
    await ctx.send('https://terraria.gamepedia.com/index.php?search=' + toSearch + '&title=Special%3ASearch&go=Go')
    return

@bot.command(name='mine',
                description="looks stuff up on the minecraft wiki",
                brief="wiki finding op",
                aliases=[])
async def mine(ctx, search):
    toSearch = removeSpaces(search)
    await ctx.send('https://minecraft.gamepedia.com/index.php?search=' + toSearch + '&title=Special%3ASearch&go=Go')
    return

@bot.command(name='cala',
                description="looks stuff up on the calamity wiki",
                brief="wiki finding op",
                aliases=[])
async def cala(ctx, search):
    print(search)
    toSearch = removeSpaces(search)
    await ctx.send('https://calamitymod.gamepedia.com/index.php?search=' + toSearch + '&title=Special%3ASearch&go=Go')
    return

def removeSpaces(input):
    return input.replace(' ','_')

bot.run('NjA2MDMzMTE0OTc1OTYxMDg4.XUFKUg.tUTMgLdjJ7YteNsXJDr1yMwk1aI')