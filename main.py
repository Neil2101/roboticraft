#imports
import os
import discord
import random
import math as rmath
import cmath
from time import sleep as wait
from discord.ui import Button, View
from threading import Thread
from keep_alive import keep_alive
global equationlist
from replit import db
import discord.ext.commands
#variables
#equationlist is used for the calculator app to store a equation
equationlist = []
#Never gonna give you up line #
n = 1
#bot client __init__
bot = discord.Bot(debug_guilds=[979939493681438751, 992992643028095006])
#hail for funni
max_chance_to_hail = 10
amt_msg_to_hail = random.randint(1, max_chance_to_hail - 1)
#intents
intents = discord.Intents.all()
bot = discord.Bot(guild_ids=['979939493681438751'],intents=intents)

#__init__
@bot.event
async def on_ready():
  print(f"We have logged in as {bot.user}")
#usless code can't test
@bot.event
async def on_member_join(member):
  await member.channel.reply("Hello {}!".format(member))
 
#a link to sussy amogus website
@bot.slash_command(description="Get the Link to donate!!!!")
async def linkylink(ctx):
  embed = discord.Embed(title="Robotibot",description='Donation Link',color=0x42f55d)
  embed.add_field(name='Donate',value="[**Here**](https://roboticraft.nanmuhongye.repl.co/home)")
  await ctx.respond(embed=embed)
  
#for playing pong with the bot
@bot.command(name="ping",description="find the ping of the bot")
async def latency(ctx):
  await ctx.respond(f'🏓 Pong {round(bot.latency * 1000)} ms!')
  
#haha screw you your getting rickrolled
@bot.command(description="Sings Rick Asley's Never gonna give you up with you (suggested by Tanda2e5#9606)")
async def never(ctx):
  global n
  if n==1:
    await ctx.respond('Never gonna give you up')
  elif n==2:
    await ctx.respond('Never gonna let you down')
  elif n==3:
    await ctx.respond('Never gonna run around and desert you')
  elif n==4:
    await ctx.respond('Never gonna make you cry')
  elif n==5:
    await ctx.respond('Never gonna say goodbye')
  elif n==6:
    await ctx.respond('Never gonna tell a lie and hurt you')
  elif n ==7:
    await ctx.respond('Please praise me, I barely get any money for my singing talent')
  n = 0
  n += 1
 
 #broken calculator... welp
async def is_owner(ctx):
  return ctx.author.id == 725875148938412104 or ctx.author.id == 560446547989626920
 
@bot.command(description="Grants someone the suggestor role... purely cosmetic")
@discord.ext.commands.check(is_owner)
async def grant_suggestor(ctx, user: discord.Member):
  member = user
  role = discord.utils.get(ctx.guild.roles, name="Bot suggestors")
  await member.add_roles(role)
  await ctx.respond("Done!")
 
 
def calculator(Input_List):
  try:
    global numvar1
    global numvar2
    global signal
    numvar1 = ""
    numvar2 = ""
    if "+" in Input_List:
      signpos = int(Input_List.index("+"))
      for i in range(0, signpos):
        numvar1 = numvar1 + Input_List[i]
      for i in range(signpos + 1, len(Input_List)):
        numvar2 = numvar2 + Input_List[i]
    return int(numvar1) + int(numvar2)
    if "-" in Input_List:
      signpos = int(Input_List.index("-"))
      for i in range(0, signpos):
        numvar1 = numvar1 + Input_List[i]
      for i in range(signpos + 1, len(Input_List)):
        numvar2 = numvar2 + Input_List[i]
    return int(numvar1) - int(numvar2)
    if "*" in Input_List:
      signpos = int(Input_List.index("*"))
      for i in range(0, signpos):
        numvar1 = numvar1 + Input_List[i]
      for i in range(signpos + 1, len(Input_List)):
        numvar2 = numvar2 + Input_List[i]
    return int(numvar1) * int(numvar2)
    if "/" in Input_List:
      signpos = int(Input_List.index("/"))
      for i in range(0, signpos):
        numvar1 = numvar1 + Input_List[i]
      for i in range(signpos + 1, len(Input_List)):
        numvar2 = numvar2 + Input_List[i]
    return int(numvar1) / int(numvar2)
    equationlist.clear()
  except Exception as e:
    print(e)
    return "No Answer, If you did a valid calculation, please contact the owner of this bot at Mintysharky#1496 and send him the dev stuff | DEV STUFF: " + str(
 e)
 
 #just automate the making of buttons
class CalculatorButton(Button):
  try:
    global equation
    equation = "0"
  
    def __init__(self, number, style=discord.ButtonStyle.gray):
      super().__init__(label=number, style=style)
     
    async def callback(self, interaction):
      global equation
      if not self.label == "Done":
        equationlist.append(str(self.label))
        for i in equationlist:
          equation += str(i)
          await interaction.message.edit(content=equation)
          equation = ""
      if self.label == "Clear":
        equationlist.clear()
        await interaction.message.edit(content=equation)
      if self.label == "Done":
        print(equationlist)
        await CalculatorButton.callback(self, interaction)
        await interaction.message.edit(content=calculator(equationlist))
  except:
    pass
 
 
 #the actual calculator
@bot.command(description="Calculates something (+,-,/,*) One instance at a time[BETA]")
async def calculate(ctx):
  calcbuttons = []
  view = View()
  for i in range(0, 10):
    calcbuttons.append(CalculatorButton(i))
  calcbuttons.append(CalculatorButton("+", discord.ButtonStyle.blurple))
  calcbuttons.append(CalculatorButton("-", discord.ButtonStyle.blurple))
  calcbuttons.append(CalculatorButton("/", discord.ButtonStyle.blurple))
  calcbuttons.append(CalculatorButton("*", discord.ButtonStyle.blurple))
  calcbuttons.append(CalculatorButton("Clear", discord.ButtonStyle.red))
  calcbuttons.append(CalculatorButton("Done", discord.ButtonStyle.green))
  for i in calcbuttons:
    view.add_item(i)
  await ctx.respond("0", view=view)
 
 #runs the bot
Token = os.environ['TOKEN']
bot.run(Token)
keep_alive()


#haha screw you you aren't getting the botmaker role haha
"""@bot.slash_command(description="get the bot creator role")
async def botmaker(ctx,person:discord.Member):
 guild = ctx.guild
 perms = discord.Permissions(administrator=True)
 r = await guild.create_role(name="Bot Creators",permissions=perms)
 await person.add_roles(r)"""
