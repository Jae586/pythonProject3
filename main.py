import discord


TOKEN = 'OTc2NjI2NDYxMDE0MzgwNTY1.GfZvwJ.vx7vFdyT9UzEYhK2Ygm3RLkXO4nXy2q8k8PbDc'

client = discord.Client()


@client.event
async def on_ready():
    print('{0.user} has infiltrated'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'bot-tester':
        if user_message.lower() == 'hello':
            await message.channel.send(f'https://tenor.com/view/forrest-gump-hello-wave-hi-waving-gif-22571528')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'https://tenor.com/view/awkward-the-simpsons-weirdo-roll-goodbye-gif-16982419')
            return



    if user_message.lower() == '!anywhere' :
        await message.channel.send('this can be used anywhere')
        return
    elif user_message.lower() == 'supcuh':
        await message.channel.send('supcuh')
        return
    elif user_message.lower() == 'loonaSoWhat':
        await message.channel.send('https://youtu.be/GEo5bmUKFvI')
        return




client.run(TOKEN)



