import discord
from discord.ext.commands import Bot
import random

bot = Bot(command_prefix = "?")

@bot.event
async def on_ready():
    print('Ready')

@bot.command(name='purify',
                description="purifies grov's last embed",
                brief="PURIFICATION",
                aliases=[])
async def purify(ctx):
    # previous messages[1].embeds[0].fields[0].value is the first block of lyrics
    previous_messages = await ctx.history(limit=2).flatten()
    
    copy_embed = previous_messages[1].embeds[0].copy()

    ctx.purge(limit=2)              # Deletes the command and the original lyrics

    content = copy_embed.fields     # Makes a copy of the fields
    copy_embed.clear_fields()       # Clears the fields to add the new fields
    
    for i in range(len(content)):
        swear_dict = {'fuck':'heck', 'ass':'butt', 'shit':'poop'}
        for swear in swear_dict:
            content[i].value = content[i].value.replace(swear, swear_dict[swear])
        copy_embed.add_field(name=content[i].name, value = content[i].value, inline=False)
    await ctx.send(embed=copy_embed)

bot.run('NjA2MDMzMTE0OTc1OTYxMDg4.XUFKUg.tUTMgLdjJ7YteNsXJDr1yMwk1aI')