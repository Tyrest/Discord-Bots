import discord
from discord.ext.commands import Bot
import random
from utils import *
from datetime import datetime

speaks = 1

bot = Bot(command_prefix = "?")

async def getInput(channel):
    input = await bot.wait_for('message')
    while input.channel != channel or input.author.bot:
        input = await bot.wait_for('message')

    return input.content

@bot.event
async def on_ready():
    print('Ready')

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
    toSearch = removeSpaces(search)
    await ctx.send('https://calamitymod.gamepedia.com/index.php?search=' + toSearch + '&title=Special%3ASearch&go=Go')
    return

def removeSpaces(input):
    output = ''
    for i in input:
        if i == ' ':
            output += '_'
        else:
            output += i

    return output

@bot.event
async def on_typing(channel, user, when):
    oosh = 'OOsh02#7936'
    tyresty = 'Tyresty#8394'
    josh = 'RubixQber#3402'
    jonathan = 'luckySquid#0849'

    global speaks
    if speaks:
        if str(user) == oosh:
            await channel.send('Yo Oosh Doosh Bush - ya better not press that enter button or we gonna come and get ya')
        elif str(user) == tyresty:
            await channel.send('Thank you for blessing us with your words great Tyresty. I anticipate nothing more than that moment when you press the enter button and bless us with the art that is your messages')
        # elif str(user) == 'Drinnok#6792':
        #     await channel.send('GOD SPEAKS (everyone quiet down)')
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
    if str(ctx.author) == 'Tyrest#8394':
        await ctx.send('As you wish')
        speaks = not speaks

    return

@bot.command(name='hangman',
                description="starts a hangman game",
                brief="staaato",
                aliases=[])
async def game(ctx):
    guild = ctx.guild
    gameChan = ctx.channel
    await gameChan.send('Hangman start!')
    wordRole = await guild.create_role()
    await ctx.author.add_roles(wordRole)
    secretChan = await createSecretChannel(guild, wordRole)
    await secretChan.send('What is your word for this game?')
    word = await getInput(secretChan)
    await secretChan.delete()
    await wordRole.delete()
    await gameChan.send('It\'s time to start guessing!')
    await guessing(gameChan, word)

    return

async def createSecretChannel(guild, role):
    overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages = False),
    guild.me: discord.PermissionOverwrite(read_messages = True),
    role: discord.PermissionOverwrite(read_messages = True)}
    channel = await guild.create_text_channel('secret', overwrites = overwrites)

    return channel

async def guessing(channel, word):
    stillPlaying = 1
    won = 0
    fails = 4
    incorrect = []
    guesses = []
    while stillPlaying:
        progress = ''
        for i in word:
            if i in guesses:
                progress += i + ' '
            else:
                progress += '- '
        await channel.send(progress)
        await channel.send('You have guessed: ' + strip(str(incorrect),'[]'))
        await channel.send('You have ' + str(fails) + ' chances left')
        await channel.send('What is your guess?')
        guess = await getInput(channel)
        guess = guess[0]
        guesses.append(guess)
        if guess in word:
            await channel.send('You got a letter right!')
            if hasWon(word, guesses):
                stillPlaying = 0
                won = 1
        else:
            await channel.send('... is not in the word')
            incorrect.append(guess)
            fails -= 1
            if fails == 0:
                stillPlaying = 0
    if won:
        await channel.send('The guesser wins!')
    else:
        await channel.send('The guesser loses!')

def hasWon(word, guesses):
    for i in word:
        if i not in guesses:
            return False
    return True

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
        elif chat == 'srec' or chat == 'stoprecord':
            print('stopping recording')
            recording = 0
            await ctx.send('Stopped recording song requests from this channel')

    return

bot.run('NjA2MDMzMTE0OTc1OTYxMDg4.XUFLpg.gXVzVgz2fzbxG3GHlrGw2LTHD_8')
