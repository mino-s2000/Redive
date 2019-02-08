import codecs
import yaml
import json
import discord
import charactor

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    m = message.content.split(' ')
    if m[0] == '/redive':
        if m[1] == 'charactor' or m[1] == 'chara':
            reply = charactor.get_charactor(m)
            await client.send_message(message.channel, reply)

client.run('token')
