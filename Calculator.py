import discord
import discord.ext.commands
from discord.ui import Button, View
global equationlist
equationlist = []

def calculator(Input_List):
  try:
    global numvar1
    global numvar2
    numvar1 = ''
    numvar2 = ''
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
      print(Input_List)
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

    def __init__(self, number, style=discord.ButtonStyle.gray):
      super().__init__(label=number, style=style)

    async def callback(self, interaction):
      if not self.label == "Done": 
        print(self.label)
        equationlist.append(str(self.label))
        for i in equationlist:
          await interaction.message.edit(content=''.join(equationlist))
        if not self.label == "Clear":
          pass
      if self.label == "Clear":
        equationlist.clear()
        await interaction.message.edit(content=''.join(equationlist))
      if self.label == "Done":
        print(equationlist)
        #calculator rendering engine
        await interaction.message.edit(content=calculator(equationlist))
        equationlist.clear()
  except:
    pass

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
  #button rendering engine
  for i in calcbuttons:
    view.add_item(i)
  await ctx.respond("_", view=view)