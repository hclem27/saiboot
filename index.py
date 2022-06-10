# Le code ci-dessus importe les modules nécessaires à l'exécution du bot.
import os
from imgurpython import ImgurClient
import discord
import requests
from dotenv import load_dotenv
from discord.ext import commands
from http import server
from discord.utils import get
from email import message


load_dotenv(dotenv_path="config")


# Définition des variables à utiliser dans le code.
client = discord.Client()
client.twitchUserG = ""
client.imageUser = ""
client.money = ""
client.emoji3 = ""
client.roles = ""
rolesUser = ""

@client.event
async def on_ready():
    print("le bot est prêt")

@client.event
async def on_message(message):

    
    # Vérifier si le message est dans le canal avec l'ID 948630478301315082 et si l'auteur du message
    # a un surnom.
    if message.channel == client.get_channel(948630478301315082):
        nick_member = message.author.nick
        if nick_member != None:

            # Prendre la variable nick_member et la diviser en une liste.
            tblMemberSplit = nick_member.split("|")
            twitchUser = tblMemberSplit[1]
            twitchUser = twitchUser.replace(" ", "")

            # Prendre le message de l'utilisateur et le stocker dans une variable.
            client.twitchUserG = twitchUser
            client.roles = message.author.roles[1].id
            client.twitchUserG = twitchUser
            messagePhotoUser = message.attachments[0].content_type
            client.imageUser = message.attachments[0].url

            
            # Vérifier si le message est dans le bon canal et si le message est une image. Si c'est le
            # cas, cela ajoute des réactions au message.
            if messagePhotoUser == 'image/png' or messagePhotoUser == 'image/jpeg' or messagePhotoUser == 'image/jpg' or messagePhotoUser == 'image/webp':
                emoji1 = '1️⃣'
                emoji2 = '2️⃣'
                emoji3 = '3️⃣'
                emoji4 = '4️⃣'
                emoji5 = '5️⃣'
                emoji6 = '6️⃣'
                emoji7 = '7️⃣'
                emoji8 = '8️⃣'
                emoji9 = '9️⃣'
                emoji10 = '🔟'
                emoji25 = '<:25:980833618446389288>'
                emoji50 = '<:50:980833628340776961>'
                await message.add_reaction(emoji1)
                await message.add_reaction(emoji2)
                await message.add_reaction(emoji3)
                await message.add_reaction(emoji4)
                await message.add_reaction(emoji5)
                await message.add_reaction(emoji6)
                await message.add_reaction(emoji7)
                await message.add_reaction(emoji8)
                await message.add_reaction(emoji9)
                await message.add_reaction(emoji10)
                await message.add_reaction(emoji25)
                await message.add_reaction(emoji50)
            else:
                await message.delete()
                await message.channel.send("Erreur : Le format de l'image est incorrect ! Veuillez contacter un administrateur")
    else:
        print("tu n'es pas dans le bon channel") 


@client.event
async def on_reaction_add(reaction, message):

    # Vérifier si l'utilisateur a le rôle "Botmaster"
    for roles in message.roles:
        if str(roles) == 'Botmaster':
            client.roles = str(roles)
            break
    rolesRequire = "Botmaster"
  	
    # Obtenir l'ID de canal du canal 
    channelAdmin = client.get_channel(926887027679592469)
    # Le code ci-dessus configure les variables de la commande.
    client.emoji25 = '<:25:980833618446389288>'
    client.emoji50 = '<:50:980833628340776961>'
    API = os.getenv("API")
    api_url = "https://wapi.wizebot.tv/api/currency/"+API+"/action/add/"+client.twitchUserG+"/"

    
    # Vérifier si la réaction est 1️⃣ et si le message ne vient pas du bot. Si c'est le cas, il
    # vérifie si l'utilisateur possède les rôles requis. Si c'est le cas, il définit la variable money
    # sur 1 et l'ajoute à api_url. Il définit ensuite la variable client.money sur 1 et obtient la
    # réponse de api_url.
    if str(reaction.emoji) == '1️⃣' and message.name != client.user:
        if client.roles == rolesRequire:
            money = "1"
            api_url += money
            client.money = money
            response = requests.get(api_url)
            response.json()
            #await reaction.message.delete()

            # Création d'une intégration.
            embed=discord.Embed(title="Sai-Bot | Récapitulatif", url=client.imageUser, description="Récapitulatif des points d'entraide ! ", color=0xff8800)
            embed.set_author(name="Sai-Bot", icon_url="https://cdn.discordapp.com/attachments/704666469384060958/980805636176617482/PDP_bot_2.jpg")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/704666469384060958/980805636176617482/PDP_bot_2.jpg")
            embed.add_field(name="Pseudo", value=client.twitchUserG, inline=True)
            embed.add_field(name="Points d'entraide", value=client.money, inline=True)
            embed.set_footer(text="Sai-Bot v.1 | Récapitulatif")
            
            # Envoi de l'intégration et de l'image à la chaîne.
            await channelAdmin.send(embed=embed)
            await channelAdmin.send(client.imageUser)
        else:
            print("Vous n'avez pas le role " + rolesRequire)        

    # Vérifier si l'utilisateur dispose des rôles requis pour utiliser la commande.
    elif str(reaction.emoji) == '2️⃣' and message.name != client.user:
        if client.roles == rolesRequire:
            money = "2"
            api_url += money
            client.money = money
            response = requests.get(api_url)
            response.json()
            #await reaction.message.delete()

            # Création d'une intégration.
            embed=discord.Embed(title="Sai-Bot | Récapitulatif", url=client.imageUser, description="Récapitulatif des points d'entraide ! ", color=0xff8800)
            embed.set_author(name="Sai-Bot", icon_url="https://cdn.discordapp.com/attachments/704666469384060958/980805636176617482/PDP_bot_2.jpg")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/704666469384060958/980805636176617482/PDP_bot_2.jpg")
            embed.add_field(name="Pseudo", value=client.twitchUserG, inline=True)
            embed.add_field(name="Points d'entraide", value=client.money, inline=True)
            embed.set_footer(text="Sai-Bot v.1 | Récapitulatif")

            # Envoi de l'intégration et de l'image à la chaîne.
            await channelAdmin.send(embed=embed)
            await channelAdmin.send(client.imageUser)
            
    # Vérifier si la réaction est 3️⃣ et si le message n'est pas le message du bot. Si c'est le cas,
    # il vérifiera si l'utilisateur a les rôles requis. S'ils le font, il définira la variable money
    # sur 3 et l'ajoutera à api_url. Il fixera ensuite l'argent du client à 3 et obtiendra la réponse
    # de l'api_url.
    elif str(reaction.emoji) == '3️⃣' and message.name != client.user:
        if client.roles == rolesRequire:
            money = "3"
            api_url += money
            client.money = money
            response = requests.get(api_url)
            response.json()
            #await reaction.message.delete()

            # Création d'une intégration.
            embed=discord.Embed(title="Sai-Bot | Récapitulatif", url=client.imageUser, description="Récapitulatif des points d'entraide ! ", color=0xff8800)
            embed.set_author(name="Sai-Bot", icon_url="https://cdn.discordapp.com/attachments/704666469384060958/980805636176617482/PDP_bot_2.jpg")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/704666469384060958/980805636176617482/PDP_bot_2.jpg")
            embed.add_field(name="Pseudo", value=client.twitchUserG, inline=True)
            embed.add_field(name="Points d'entraide", value=client.money, inline=True)
            embed.set_footer(text="Sai-Bot v.1 | Récapitulatif")

            # Envoi de l'intégration et de l'image à la chaîne.
            await channelAdmin.send(embed=embed)
            await channelAdmin.send(client.imageUser)

    # Vérifier si la réaction est 4️⃣ et si le message ne vient pas du bot. Si c'est le cas, il
    # vérifiera si l'utilisateur a les rôles requis. S'ils le font, il définira la variable money sur
    # 4 et l'ajoutera à api_url. Il définira ensuite la variable client.money sur 4 et obtiendra la
    # réponse de api_url.
    elif str(reaction.emoji) == '4️⃣' and message.name != client.user:
        if client.roles == rolesRequire:
            money = "4"
            api_url += money
            client.money = money
            response = requests.get(api_url)
            response.json()
            #await reaction.message.delete()

            # Création d'une intégration.
            embed=discord.Embed(title="Sai-Bot | Récapitulatif", url=client.imageUser, description="Récapitulatif des points d'entraide ! ", color=0xff8800)
            embed.set_author(name="Sai-Bot", icon_url="https://cdn.discordapp.com/attachments/704666469384060958/980805636176617482/PDP_bot_2.jpg")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/704666469384060958/980805636176617482/PDP_bot_2.jpg")
            embed.add_field(name="Pseudo", value=client.twitchUserG, inline=True)
            embed.add_field(name="Points d'entraide", value=client.money, inline=True)
            embed.set_footer(text="Sai-Bot v.1 | Récapitulatif")

            # Envoi de l'intégration et de l'image à la chaîne.
            await channelAdmin.send(embed=embed)
            await channelAdmin.send(client.imageUser)
            
    # Vérifier si la réaction est 5️⃣ et si le message ne vient pas du bot. Si c'est le cas, il
    # vérifiera si l'utilisateur a les rôles requis. S'ils le font, il définira la variable money sur
    # 5 et l'ajoutera à api_url. Il définira ensuite la variable client.money sur 5 et obtiendra la
    # réponse de api_url.
    elif str(reaction.emoji) == '5️⃣' and message.name != client.user:
        if client.roles == rolesRequire:
            money = "5"
            api_url += money
            client.money = money
            response = requests.get(api_url)
            response.json()
           
            # Création d'une intégration.
            embed=discord.Embed(title="Sai-Bot | Récapitulatif", url=client.imageUser, description="Récapitulatif des points d'entraide ! ", color=0xff8800)
            embed.set_author(name="Sai-Bot", icon_url="https://cdn.discordapp.com/attachments/704666469384060958/980805636176617482/PDP_bot_2.jpg")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/704666469384060958/980805636176617482/PDP_bot_2.jpg")
            embed.add_field(name="Pseudo", value=client.twitchUserG, inline=True)
            embed.add_field(name="Points d'entraide", value=client.money, inline=True)
            embed.set_footer(text="Sai-Bot v.1 | Récapitulatif")

            # Envoi de l'intégration et de l'image à la chaîne.
            await channelAdmin.send(embed=embed)
            await channelAdmin.send(client.imageUser)

    # Vérifier si la réaction est 6️⃣ et si le message n'est pas le message du bot. Si c'est le cas,
    # il vérifiera si l'utilisateur a les rôles requis. S'ils le font, il définira la variable money
    # sur 6 et l'ajoutera à api_url. Il fixera ensuite l'argent du client à 6 et obtiendra la réponse
    # de l'api_url.
    elif str(reaction.emoji) == '6️⃣' and message.name != client.user:
        if client.roles == rolesRequire:
            money = "6"
            api_url += money
            client.money = money
            response = requests.get(api_url)
            response.json()

            # Création d'une intégration.
            embed=discord.Embed(title="Sai-Bot | Récapitulatif", url=client.imageUser, description="Récapitulatif des points d'entraide ! ", color=0xff8800)
            embed.set_author(name="Sai-Bot", icon_url="https://cdn.discordapp.com/attachments/704666469384060958/980805636176617482/PDP_bot_2.jpg")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/704666469384060958/980805636176617482/PDP_bot_2.jpg")
            embed.add_field(name="Pseudo", value=client.twitchUserG, inline=True)
            embed.add_field(name="Points d'entraide", value=client.money, inline=True)
            embed.set_footer(text="Sai-Bot v.1 | Récapitulatif")
            
            # Envoi de l'intégration et de l'image à la chaîne.
            await channelAdmin.send(embed=embed)
            await channelAdmin.send(client.imageUser)
        
    # Vérifier si la réaction est 7️⃣ et si le message ne vient pas du bot. Si c'est le cas, il
    # vérifiera si l'utilisateur a les rôles requis. S'ils le font, il définira la variable money sur
    # 7 et l'ajoutera à api_url. Il définira ensuite la variable client.money sur 7 et obtiendra la
    # réponse de api_url.
    elif str(reaction.emoji) == '7️⃣' and message.name != client.user:
        if client.roles == rolesRequire:
            money = "7"
            api_url += money
            client.money = money
            response = requests.get(api_url)
            response.json()
            #await reaction.message.delete()
 
            # Création d'une intégration.
            embed=discord.Embed(title="Sai-Bot | Récapitulatif", url=client.imageUser, description="Récapitulatif des points d'entraide ! ", color=0xff8800)
            embed.set_author(name="Sai-Bot", icon_url="https://cdn.discordapp.com/attachments/704666469384060958/980805636176617482/PDP_bot_2.jpg")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/704666469384060958/980805636176617482/PDP_bot_2.jpg")
            embed.add_field(name="Pseudo", value=client.twitchUserG, inline=True)
            embed.add_field(name="Points d'entraide", value=client.money, inline=True)
            embed.set_footer(text="Sai-Bot v.1 | Récapitulatif")

            # Envoi de l'intégration et de l'image à la chaîne.
            await channelAdmin.send(embed=embed)
            await channelAdmin.send(client.imageUser)

    # Vérifier si la réaction est 8️⃣ et si le message ne vient pas du bot. Si c'est le cas, il
    # vérifiera si l'utilisateur a les rôles requis. S'ils le font, il définira la variable money sur
    # 8 et l'ajoutera à api_url. Il définira ensuite la variable client.money sur 8, puis obtiendra la
    # réponse de api_url.
    elif (reaction.emoji) == '8️⃣' and message.name != client.user:
        if client.roles == rolesRequire:
            money = "8"
            api_url += money
            client.money = money
            response = requests.get(api_url)
            response.json()
            #await reaction.message.delete()

            # Création d'une intégration.
            embed=discord.Embed(title="Sai-Bot | Récapitulatif", url=client.imageUser, description="Récapitulatif des points d'entraide ! ", color=0xff8800)
            embed.set_author(name="Sai-Bot", icon_url="https://cdn.discordapp.com/attachments/704666469384060958/980805636176617482/PDP_bot_2.jpg")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/704666469384060958/980805636176617482/PDP_bot_2.jpg")
            embed.add_field(name="Pseudo", value=client.twitchUserG, inline=True)
            embed.add_field(name="Points d'entraide", value=client.money, inline=True)
            embed.set_footer(text="Sai-Bot v.1 | Récapitulatif")

            # Envoi de l'intégration et de l'image à la chaîne.
            await channelAdmin.send(embed=embed)
            await channelAdmin.send(client.imageUser)
        
    # Vérifier si la réaction est 9️⃣ et si le message n'est pas le message du bot. Si c'est le cas,
    # il vérifiera si l'utilisateur a les rôles requis. S'ils le font, il définira la variable money
    # sur 9 et l'ajoutera à api_url. Il fixera ensuite l'argent du client à 9 et obtiendra la réponse
    # de l'api_url.
    elif str(reaction.emoji) == '9️⃣' and message.name != client.user:
        if client.roles == rolesRequire:
            money = "9"
            api_url += money
            client.money = money
            response = requests.get(api_url)
            response.json()
            #await reaction.message.delete()

            # Création d'une intégration.
            embed=discord.Embed(title="Sai-Bot | Récapitulatif", url=client.imageUser, description="Récapitulatif des points d'entraide ! ", color=0xff8800)
            embed.set_author(name="Sai-Bot", icon_url="https://cdn.discordapp.com/attachments/704666469384060958/980805636176617482/PDP_bot_2.jpg")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/704666469384060958/980805636176617482/PDP_bot_2.jpg")
            embed.add_field(name="Pseudo", value=client.twitchUserG, inline=True)
            embed.add_field(name="Points d'entraide", value=client.money, inline=True)
            embed.set_footer(text="Sai-Bot v.1 | Récapitulatif")

            # Envoi de l'intégration et de l'image à la chaîne.
            await channelAdmin.send(embed=embed)
            await channelAdmin.send(client.imageUser)

    # Vérifier si l'utilisateur dispose des rôles requis pour utiliser la commande.
    elif str(reaction.emoji) == '🔟' and message.name != client.user:
        if client.roles == rolesRequire:
            money = "10"
            api_url += money
            client.money = money
            response = requests.get(api_url)
            response.json()
            #await reaction.message.delete()

            # Création d'une intégration.
            embed=discord.Embed(title="Sai-Bot | Récapitulatif", url=client.imageUser, description="Récapitulatif des points d'entraide ! ", color=0xff8800)
            embed.set_author(name="Sai-Bot", icon_url="https://cdn.discordapp.com/attachments/704666469384060958/980805636176617482/PDP_bot_2.jpg")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/704666469384060958/980805636176617482/PDP_bot_2.jpg")
            embed.add_field(name="Pseudo", value=client.twitchUserG, inline=True)
            embed.add_field(name="Points d'entraide", value=client.money, inline=True)
            embed.set_footer(text="Sai-Bot v.1 | Récapitulatif")

            # Envoi de l'intégration et de l'image à la chaîne.
            await channelAdmin.send(embed=embed)
            await channelAdmin.send(client.imageUser)
        
    # Vérifier si l'emoji est l'emoji25 et si le message ne vient pas du bot. Si c'est le cas, il
    # vérifiera si les rôles sont les rôlesRequire. Si c'est le cas, il fixera l'argent à 25 et
    # l'ajoutera à api_url. Il définira ensuite client.money sur 25 et obtiendra la réponse de
    # api_url.
    elif str(reaction.emoji) == client.emoji25 and message.name != client.user:
        if client.roles == rolesRequire:
            money = "25"
            api_url += money
            client.money = money
            response = requests.get(api_url)
            response.json()
            #await reaction.message.delete()

            # Création d'une intégration.
            embed=discord.Embed(title="Sai-Bot | Récapitulatif", url=client.imageUser, description="Récapitulatif des points d'entraide ! ", color=0xff8800)
            embed.set_author(name="Sai-Bot", icon_url="https://cdn.discordapp.com/attachments/704666469384060958/980805636176617482/PDP_bot_2.jpg")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/704666469384060958/980805636176617482/PDP_bot_2.jpg")
            embed.add_field(name="Pseudo", value=client.twitchUserG, inline=True)
            embed.add_field(name="Points d'entraide", value=client.money, inline=True)
            embed.set_footer(text="Sai-Bot v.1 | Récapitulatif")

            # Envoi de l'intégration et de l'image à la chaîne.
            await channelAdmin.send(embed=embed)
            await channelAdmin.send(client.imageUser)
        
   # Vérifier si l'utilisateur dispose des rôles requis pour utiliser la commande.
    elif str(reaction.emoji) == client.emoji50 and message.name != client.user:
        if client.roles == rolesRequire:
            money = "50"
            api_url += money
            client.money = money
            response = requests.get(api_url)
            response.json()
            #await reaction.message.delete()

            # Création d'une intégration.
            embed=discord.Embed(title="Sai-Bot | Récapitulatif", url=client.imageUser, description="Récapitulatif des points d'entraide ! ", color=0xff8800)
            embed.set_author(name="Sai-Bot", icon_url="https://cdn.discordapp.com/attachments/704666469384060958/980805636176617482/PDP_bot_2.jpg")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/704666469384060958/980805636176617482/PDP_bot_2.jpg")
            embed.add_field(name="Pseudo", value=client.twitchUserG, inline=True)
            embed.add_field(name="Points d'entraide", value=client.money, inline=True)
            embed.set_footer(text="Sai-Bot v.1 | Récapitulatif")

            # Envoi de l'intégration et de l'image à la chaîne.
            await channelAdmin.send(embed=embed)
            await channelAdmin.send(client.imageUser)

client.run(os.getenv("TOKEN"))
