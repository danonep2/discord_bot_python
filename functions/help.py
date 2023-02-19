from discord import Embed, Colour

commandsList = [
    'help', 'h',
    'random', 'r',
    'calc'
]

helpeTextCommand = {
    'help':{
        'name' :'Help',                                               
        'desc' :'Exibe uma descrição mais detalhada do comando',      
        'syntax' : '$help <comando>',                                 
        'comments':'',                                                
    },
    'random' : {
        'name' : 'Radom',
        'desc' : 'Gera um valor aleatorio no intervalo informado',
        'syntax' : '$random <valor min> <valor max>',
        'comments' : 'Caso seja informado apenas um valor o valor min é 0.'
    },
    'calc' : {
        'name' :'Calc',
        'desc' :'Calcula a expressão informada',
        'syntax' : '$calc <expressão>',
        'comments' :'''/  => divisão
*   => multiplicação
** => potencia
+   => soma
-   => subtração
( para raizes utilize a potencia com fração )
        '''
    }
}

async def helperCommands(parametros, message):
    if len(parametros) > 2:
        embed = Embed(
            title = '',
            description ='Parametros inválidos.',
            colour = Colour.red()
            )
    
    if len(parametros) == 1:
        embed = Embed(
            title = 'Lista de comandos',
            description =' Utilize $help <comando> para mais detalhes',
            colour = Colour.red()
            )

        name_author = 'OhMyGod#9543'
        icon_author = 'https://i.pinimg.com/originals/85/be/94/85be94350b6cefd78140c8c8232c75e5.gif'
        img = 'https://media.tenor.com/e73qA4y4pKIAAAAC/pepe-frog.gif'
        thumb_img = 'https://media.tenor.com/AF8QpfRjlJQAAAAC/pepe-bebep.gif'
        footer_text = ' Iago (@danonep2) '

        embed.set_author(name= name_author, icon_url= icon_author)
        embed.set_image(url= img)
        embed.set_footer(text=footer_text)
        embed.set_thumbnail(url= thumb_img)

        for i in helpeTextCommand.keys():
            comN = helpeTextCommand[i]
            embed.add_field(name = comN['name'], value= comN['desc'], inline=False)

    if len(parametros) == 2:
        if not(parametros[1] in commandsList):
            embed = Embed(
                title = '',
                description ='comando não encontrado',
                colour = Colour.red())
        else:
            commandInfo = helpeTextCommand[parametros[1]]      
            embed = Embed(
                title = f'Ajuda em --> {parametros[1]}',
                description ='',
                colour = Colour.red())

            embed.add_field(name=commandInfo['name'],value=commandInfo['desc'],inline=False)
            embed.add_field(name='Sintaxe', value = commandInfo['syntax'],inline=False)
            if commandInfo['comments'] != '':
                embed.add_field(name="Obeservações", value=commandInfo['comments'], inline=False)

            thumb_img = 'https://media.tenor.com/AF8QpfRjlJQAAAAC/pepe-bebep.gif'
            embed.set_thumbnail(url=thumb_img)

    await message.channel.send(embed= embed)