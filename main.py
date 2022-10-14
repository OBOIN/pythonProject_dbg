import discord
from datetime import datetime

intents = discord.Intents.default()
intents.members = True
intents.typing = False
intents.presences = False
intents.messages = True
intents.message_content = True

# client = commands.Bot(command_prefix=',', intents=intents)
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("Le bot est prêt")


@client.event
async def on_message(message):
    # print(message.content)
    if message.author == client.user:   # ne répondre à son propre message
        return
    auteur = str(message.author)
    msg = str(message.content)
    channel = message.channel
    if message.content.startswith('!'):
        await channel.send("J'ai bien reçu ton message !!![" + auteur +"/"+msg + "]")
        if message.content.lower() == "!hello":
            await channel.send("Hello " + auteur + " !")
        elif msg.lower() == "!heure":
            maDate = datetime.now()
            await channel.send("Il est " + maDate.strftime("%Hh%M") + ".")
        else:
            print("!bof")

    # ok saul message.content!! await message.channel.send("j'ai bien reçu ton message ["+str(len(message.content))+"]")
    # ok  await channel.send(auteur)
    else:
        await channel.send("J'ai bien reçu ton message ![" + auteur+"/" + msg+"]")
    # ok await channel.send(message.author)

client.run("MTAzMDExOTA5MTU5NzQ5NjQzMQ.GIFJJF.iRkS7GHxpMpiABMrase5ATW8_8fXdhKEeR4Pjw")
