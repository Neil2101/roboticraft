#imports
import os
import discord
import random
import discord.ext.commands
import Calculator
from discord.ui import Button, View
from keep_alive import keep_alive
from threading import Thread as thread


global equationlist

#variables
#equationlist is used for the calculator app to store a equation
equationlist = []
#Never gonna give you up line #
n = 1
#bot client __init__
bot = discord.Bot(debug_guilds=[979939493681438751, 992992643028095006])
#string and stuff
enter = """
"""
#intents
intents = discord.Intents.all()
bot = discord.Bot(guild_ids=['979939493681438751'], intents=intents)


#__init__
@bot.event
async def on_ready():
  print(f"We have logged in as {bot.user}")


#usless code can't test
@bot.event
async def on_member_join(member):
  await member.channel.reply("Hello {}!".format(member))


#a link to sussy amogus website
@bot.command(description="Suggests an Idea. Minty or max will read it once a week")
async def suggest(ctx, idea:str):
  with open('Ideas.txt', "a") as myfile:
    myfile.write("Name: " + str(ctx.author) + " Idea: " + idea + "\n")
    myfile.close()
  await ctx.respond("Done!")
@bot.command(description="Get the Link to donate!!!!")
async def linkylink(ctx):
  embed = discord.Embed(title="Robotibot",
                        description='Donation Link',
                        color=0x42f55d)
  embed.add_field(
    name='Donate',
    value="[**Here**](https://roboticraft.nanmuhongye.repl.co/home)")
  await ctx.respond(embed=embed)


#for playing pong with the bot
@bot.command(name="ping", description="find the ping of the bot")
async def latency(ctx):
  await ctx.respond(f'🏓 Pong {round(bot.latency * 1000)} ms!')


#haha screw you your getting rickrolled
@bot.command(description="Sings Rick Asley's Never gonna give you up with you (suggested by Tanda2e5#9606)")
async def never(ctx):
  global n
  if n == 1:
    await ctx.respond('Never gonna give you up')
  elif n == 2:
    await ctx.respond('Never gonna let you down')
  elif n == 3:
    await ctx.respond('Never gonna run around and desert you')
  elif n == 4:
    await ctx.respond('Never gonna make you cry')
  elif n == 5:
    await ctx.respond('Never gonna say goodbye')
  elif n == 6:
    await ctx.respond('Never gonna tell a lie and hurt you')
  elif n == 7:
    await ctx.respond('Please praise me, I barely get any money for my singing talent')
    n = 0
  n += 1

async def is_owner(ctx):
  return ctx.author.id == 725875148938412104 or ctx.author.id == 560446547989626920
@bot.command(description="Grants someone the suggestor role... purely cosmetic")
@discord.ext.commands.check(is_owner)
async def grant_suggestor(ctx, user: discord.Member):
  member = user
  role = discord.utils.get(ctx.guild.roles, name="Bot suggestors")
  await member.add_roles(role)
  await ctx.respond("Done!")

#the actual calculator
@bot.command(
  description="Calculates something (+,-,/,*) One instance at a time[BETA]")
async def calculate(ctx):
  await Calculator.calculate(ctx)

kl2 = os.environ["TOKEN"]

try:
  def botloop():
    try:
      bot.run(kl2)
    except Exception as e:
      print(f"Something went wrong... {e}")
  botloopthread = thread(target=botloop)
  keepalivethread= thread(target=keep_alive)
  botloopthread.start()
  keepalivethread.start()
except Exception as e:
  print(f"Something went wrong... {e}")

  
#haha screw you you aren't getting the botmaker role haha
"""@bot.slash_command(description="get the bot creator role")
async def botmaker(ctx,person:discord.Member):
 guild = ctx.guild
 perms = discord.Permissions(administrator=True)
 r = await guild.create_role(name="Bot Creators",permissions=perms)
 await person.add_roles(r)"""
