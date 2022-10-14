import discord

# client = discord.Client(intents=discord.Intents.default())

intents = discord.Intents.default()
intents.members = True
intents.typing = False
intents.presences = False

# client = commands.Bot(command_prefix=',', intents=intents)
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("Le bot est prêt")


@client.event
async def on_message(message):
    # print(message.content)
    await message.channel.send("ert")

client.run("MTAzMDExOTA5MTU5NzQ5NjQzMQ.GIFJJF.iRkS7GHxpMpiABMrase5ATW8_8fXdhKEeR4Pjw")
