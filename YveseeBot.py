import discord

client = discord.Client()
TOKEN = ""
bad_Words = ['poop', 'bad']


@client.event
async def on_ready():
    print(f"infiltrated as {client.user}")


@client.event
async def on_message(msg):
    if msg.author != client.user:
        for text in bad_Words:
            if "mod" not in str(msg.author.roles) and text in str(msg.content.lower()):
                await msg.delete()
                return
        print("not deleting")


client.run(TOKEN)
