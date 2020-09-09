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
    alicia = 'sleepyhead#3539'
    vivek = 'Festive Squid#6907'
    oliver = 'Pebis#4777'

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
        elif str(user) == alicia:
            await channel.send('')
        elif str(user) == vivek:
            await channel.send('')
        elif str(user) == oliver:
            await channel.send('')
        return

@bot.command(name='silence',
                description="silences the typing events",
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

@bot.command(name='purify',
                description="purifies grov's last embed",
                brief="PURIFICATION",
                aliases=[])
async def purify(ctx):
    # previous messages[1].embeds[0].fields[0].value is the first block of lyrics
    previous_messages = await ctx.history(limit=2).flatten()
    
    copy_embed = previous_messages[1].embeds[0].copy()

    await ctx.channel.purge(limit=2)        # Deletes the command and the original lyrics

    content = copy_embed.fields             # Makes a copy of the fields
    copy_embed.clear_fields()               # Clears the fields to add the new fields

    for i in range(len(content)):
        swear_dict = {'fuck':'heck', ' ass':' butt', 'shit':'poop', 'bitches':'women', 'bitch':'gal',\
                      'Fuck':'Heck', 'Ass ':'Butt '  , 'Shit':'Poop', 'Bitches':'Women', 'Bitch':'Gal'}
        for swear in swear_dict:
            content[i].value = content[i].value.replace(swear, swear_dict[swear])
        copy_embed.add_field(name=content[i].name, value = content[i].value, inline=False)
    await ctx.send(embed=copy_embed)

bot.run('NjA2MDMzMTE0OTc1OTYxMDg4.XUFKUg.tUTMgLdjJ7YteNsXJDr1yMwk1aI')