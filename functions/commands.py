import random
from discord import Embed, Colour
from functions.help import helperCommands

commandsList = [
    'help', 'h',
    'random', 'r',
    'calc'
]

async def randomF(start, end, channel):
    print(start, end)

    if end < start: end, start = start, end

    res = random.randint(start, end)
    ranger = f'No intervalo de [{start} : {end}]'
    embed = Embed(
        title = f'O numero sorteado foi: {res}',
        description = ranger,
        colour= Colour.red())

    return embed

async def calc(expressao):
    try:
        resE = eval(expressao)
        res = Embed(
            description = f'{expressao} = {resE}',
            colour = Colour.red()
        )

    except:
        res = Embed(
            description = 'A expressão não esta correta.',
            colour = Colour.red()
        )

    return res

'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣿⣿⣷⣶⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⡟⠁⣰⣿⣿⣿⡿⠿⠻⠿⣿⣿⣿⣿⣧⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⠏⠀⣴⣿⣿⣿⠉⠀⠀⠀⠀⠀⠈⢻⣿⣿⣇⠀⠀⠀
⠀⠀⠀⠀⢀⣠⣼⣿⣿⡏⠀⢠⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⡀⠀⠀
⠀⠀⠀⣰⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀
⠀⠀⢰⣿⣿⡿⣿⣿⣿⡇⠀⠘⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⢀⣸⣿⣿⣿⠁⠀⠀
⠀⠀⣿⣿⣿⠁⣿⣿⣿⡇⠀⠀⠻⣿⣿⣿⣷⣶⣶⣶⣶⣶⣿⣿⣿⣿⠃⠀⠀⠀
⠀⢰⣿⣿⡇⠀⣿⣿⣿⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀
⠀⢸⣿⣿⡇⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠛⠉⢉⣿⣿⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣇⠀⣿⣿⣿⠀⠀⠀⠀⠀⢀⣤⣤⣤⡀⠀⠀⢸⣿⣿⣿⣷⣦⠀⠀⠀
⠀⠀⢻⣿⣿⣶⣿⣿⣿⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣦⡀⠀⠉⠉⠻⣿⣿⡇⠀⠀
⠀⠀⠀⠛⠿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠈⠹⣿⣿⣇⣀⠀⣠⣾⣿⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣦⣤⣤⣤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⠿⠋⠉⠛⠋⠉⠉⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉'''

async def foundCommand(message):
    parametros = message.content[1:].split()
    print(parametros)

    if parametros[0] in commandsList:
        print('found command')
        command = parametros[0]

    else:
        await message.channel.send(embed=Embed(
                title = '',
                description ='Comando não encontrado. Tente $help para ver a lista de comandos.',
                colour = Colour.red()))
        return

    ################# Help #################
    if command == 'help' or command == 'h':
        await helperCommands(parametros, message)
        return
    
    ################# Random  #################
    elif command == 'random' or command == 'r':
        try:
            if len(parametros) == 2:
                res = await randomF(0, int(parametros[1]), message.channel)

            elif len(parametros) == 3:
                res = await randomF(int(parametros[1]), int(parametros[2]), message.channel)

            else:
                res = Embed(
                title = '',
                description ='Valores inválidos',
                colour = Colour.red())
        
        except:
            res = Embed(
            title = '',
            description ='Valores inválidos',
            colour = Colour.red())

        
        await message.channel.send(embed=res)
        return
    
    ################# Calc #################
    elif command == 'calc':
            res = await calc(message.content.replace('$calc ', ''))
            await message.channel.send(embed=res)