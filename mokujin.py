#!/usr/bin/env python3
import asyncio

import discord
from discord.ext import commands

import tkfinder

prefix = '.'
description = 'A Tekken 7 Frame bot in construction... Made by Baikonur'
bot = commands.Bot(command_prefix=prefix, description=description)

# Get token from local txt file
with open('token.txt') as token_file:
    token = token_file.read().strip()

def make_move_embed(character, move):
    pass


@bot.event
@asyncio.coroutine 
def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
@asyncio.coroutine 
def test():
    print('Testing...')
    embed = discord.Embed(title='Test title', description='A test embed thing.', colour=0x0000FF)
    embed.set_author(name='Test name', icon_url=bot.user.default_avatar_url)
    yield from bot.say(embed=embed, delete_after=60)

@bot.event
@asyncio.coroutine
def on_message(message):
    if message.content.startswith('!') and message.channel.name == 'tekken':
        user_message = message.content
        user_message = user_message.replace('!', '')
        user_message_list = user_message.split(' ', 1)

        if len(user_message_list) <= 1:
            # malformed command
            return

        chara_name = user_message_list[0].lower()
        chara_move = user_message_list[1]
        if chara_name == 'dj' or chara_name == 'dvj' or chara_name == 'devil' or chara_name == 'deviljin':
            chara_name = 'devil_jin'
        elif chara_name == 'sergei':
            chara_name = 'dragunov'
        elif chara_name == 'jack':
            chara_name = 'jack7'
        elif chara_name == 'chloe' or chara_name == 'lc' or chara_name == 'lucky':
            chara_name = 'lucky_chloe'
        elif chara_name == "hei":
            chara_name = 'heihachi'
        elif chara_name == 'raven':
            chara_name = 'master_raven'
        elif chara_name == 'yoshi':
            chara_name = 'yoshimitsu'
        elif chara_name == 'ling':
           chara_name = 'xiaoyu'

        character = tkfinder.get_character(chara_name)
        if character is not None:
            bot_msg = 'Character ' + chara_name + ' exists!'
            print(bot_msg)
            yield from bot.send_message(message.channel, bot_msg)
            move = tkfinder.get_move(character, chara_move)
            if move is not None:
                pass
            else:
                print('Move not found: ' + chara_move)
        else:
            bot_msg = 'Character ' + chara_name + ' does not exist.'
            print(bot_msg)
            yield from bot.send_message(message.channel, bot_msg)
            return
        # if character_exists:
            # move_dict = get_move_details(chara_name, chara_move)
            # if validate move:
                # construct the message
                # send message
            # else move doesn't exist:
                # construct error msg
                # send error msg
            # return
        # else:
            # send char doesn't exist msg
            # return
    yield from bot.process_commands(message)
bot.run(token)
