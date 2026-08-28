import discord

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$buen dia'):
        await message.channel.send("hola")
    elif message.content.startswith('$emoji'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$me despido'):
            await message.channel.send("chau")
    else:
        await message.channel.send(message.content)

client.run("")
