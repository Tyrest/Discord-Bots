import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Ready')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    input = message.content

    if input.startswith('?'):
        input = input[1:]
        if input.startswith('mine'):
            input = input[5:]
            await message.channel.send('https://minecraft.gamepedia.com/index.php?search=' + input + '&title=Special%3ASearch&go=Go')
        elif input.startswith('terr'):
            input = input[5:]
            await message.channel.send('https://terraria.gamepedia.com/index.php?search=' + input + '&title=Special%3ASearch&go=Go')
        elif input.startswith('cala'):
            input = input[5:]
            await message.channel.send('https://calamitymod.gamepedia.com/index.php?search=' + input + '&title=Special%3ASearch&go=Go')

    return

client.run('NjA2MDMzMTE0OTc1OTYxMDg4.XUFLpg.gXVzVgz2fzbxG3GHlrGw2LTHD_8')
