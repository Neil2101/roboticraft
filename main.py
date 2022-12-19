import os
import discord
import random
import math as rmath
import cmath

TOKEN = os.environ['TOKEN']

var12 = 0
client = discord.Client()
amt_msg_to_hail = random.randint(1,19)

@client.event
async def on_ready():
  if client.user == None:
    print("something is wrong")
  else:
    print("Logged in to {}".format(client.user))

@client.event
async def on_message(message):

#if someone says something, search for these words
  if message.author != client.user:
    if str(message.content).lower() == "hello!":
      await message.channel.send("Hello!")
    elif str(message.content).lower() == "never":
      await message.channel.send("gonna give you up")

#to mess with those two idiots
  if str(message.author.name) == "Quandale Dingle" or str(message.author.name) == "Juandale Pringle (bruvboi1290)":
    await message.channel.send("Can you shut up?")

#HAIL ME!
  if str(message.author.name) == "Mintysharky" or str(message.author.name) == "RoboticMage888":
    global var12
    global amt_msg_to_hail
    if var12 == amt_msg_to_hail:
      var12 = 0
      amt_msg_to_hail = random.randint(1,19)
      await message.channel.send("Hello Owner!")
    else:
      var12 += 1
  
client.run(TOKEN)
