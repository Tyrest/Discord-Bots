from datetime import datetime

now = datetime.now()
now = now.strftime('%m-%d-%Y_%H-%M-%S')
fileName = 'DiscordRecord/' + str(now) + '.txt'

f = open(fileName,'w+')

f.write('Hello\n')
f.write('This should be the second line\n')
