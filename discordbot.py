import codecs
import yaml
import json
import discord
import character

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    m = message.content.split(' ')
    if m[0] == '/redive':
        reply = ''
        if m[1] == 'character' or m[1] == 'chara' or m[1] == 'c':
            reply = character.get_character(m)
        elif m[1] == 'equipment' or m[1] == 'equip' or m[1] == 'e':
            reply = 'send equipment message.'
        elif m[1] == 'monster' or m[1] == 'mons' or m[1] == 'm':
            reply = 'send monster message.'
        elif m[1] == 'help' or m[1] == 'h':
            reply = 'send help message.'
        else:
            reply = 'Oops! Please re-send command.\nHelp: `/redive help`'
        await client.send_message(message.channel, reply)

client.run('token')
