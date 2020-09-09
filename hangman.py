import discord
from discord.ext.commands import Bot
import random
from utils import *

client = Bot(command_prefix = "?")

@client.event
async def on_ready():
    print('Ready')

@client.command(name='hangman',
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

async def getInput(channel):
    input = await client.wait_for('message')
    while input.channel != channel:
        input = await client.wait_for('message')

    return input.content

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
                progress += i
            else:
                progress += '_'
        await channel.send('You have guessed: ' + strip(str(incorrect),'[]'))
        await channel.send('You have ' + str(fails) + ' chances left')
        await channel.send('What is your guess?')
        guess = await getInput(channel)
        guess = guess[0]
        guesses.append(guess)
        if guess in word:
            await channel.send('You got a letter right!')
            for index in range(len(word)):
                if word[index] == guess:
                    progress[index] = guess
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

client.run('NjA2MDMzMTE0OTc1OTYxMDg4.XUFLpg.gXVzVgz2fzbxG3GHlrGw2LTHD_8')
