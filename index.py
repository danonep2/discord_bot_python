import discord
import functions.commands as commands

bot_token = 'MTA2NjM2MDgzOTI1MjIzNDMxMA.GLj_Lz.Sz7YCwUQnQSs2mY5nRJh_cWLl0ShFK24QGUMNY'
prefix = '$'

class MyClient(discord.Client):
    async def on_ready(self):
        print('Login in', self.user)

    async def on_message(self, message):
        if message.author == self.user: return
        
        if f'<@{self.user.id}>' in message.content:
            await message.channel.send(f'Olá <@{message.author.id}>. Digite $h para mais informações sobre o bot.')

        if message.content[0] == prefix:
            await commands.foundCommand(message)

intents = discord.Intents.all()
client = MyClient(intents=intents)
client.run(bot_token)

