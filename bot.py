import discord, re, math
from discord.ext import commands, tasks
from itertools import cycle
import random
import os
from datetime import datetime



client = commands.Bot(command_prefix='*')
client.remove_command('help')
courses = {
 "checkXml" : 'x',
 "checkComp" : 'c',
 "checkTesting": 't',
 "checkSecurity": 's',
 "checkDesign": 'd',
 "checkAsp": 'a'
}



x = courses['checkXml'] = '''```css\n
Course: [XML]
Date: [11/11/2020]
Chapters: [1,2,3,4 and 5]```'''

c = courses['checkComp'] = '''```css\n
Course: [Compiler]
Date: [17/11/2020]
Chapters: [1,2,3 up to first() and follow()]```'''

t = courses['checkTesting'] = '''```css\n
Course: [Software Testing]
Date: [10/11/2020]
Chapters: [2 and 3]```'''

s = courses['checkSecurity'] = '''```css\n
Course: [Security]
Date: [14/11/2020]
Chapters: [1,2 and 3]```'''

d = courses['checkDesign'] = '''```css\n
Course: [Design]
Date: [11/11/2020]
Chapters: [1(only diagrams),2 and 3 up-to ACD]```'''


a = courses['checkAsp'] = '''```css\n
Course: [Asp.NET]
Date: [10/11/2020]
Chapters: [2,3 and 4 up to the topic of 3/11/2020 class]```'''

@client.event
async def on_ready():
 
 print('bot is ready...')
 print(client.user.name)
 
@client.command()
async def checkXml(ctx):
 await ctx.send(x)

@client.command()
async def checkComp(ctx):
 await ctx.send(c)


@client.command()
async def checkTesting(ctx):
 await ctx.send(t)

@client.command()
async def checkSecurity(ctx):
 await ctx.send(s)

@client.command()
async def checkDesign(ctx):
 await ctx.send(d)

@client.command()
async def checkAsp(ctx):
 await ctx.send(a)

@client.command()
async def checkAll(ctx):
 for key, value in courses.items():
  a = value + '\n' + '\n'
  await ctx.send(a)



@client.command()
async def clear(ctx, amount=1+1):
 await ctx.channel.purge(limit=amount)


@client.command()
async def help(ctx):
 author = ctx.message.author

 embed = discord.Embed(
  color = discord.Colour.orange()
  )
 embed.set_author(name='Help')
 embed.add_field(name='*checkAll', value='returns the date of all courses',inline=False)
 embed.add_field(name='''*check[course_Name]''', value='returns the date of a specific course',inline=False)
 embed.add_field(name='*links', value='returns the playlist of all courses',inline=False)
 await ctx.send(embed=embed)


 @client.command()
 async def help2(ctx):
 	file = discord.File("C:/Users/Nasser/Desktop/python/dsicord/watch.jpg", filename = "watch.jpg")
 	await ctx.send("hello",file=file)



@client.event
async def on_message(message):
 #guild = ctx.guild
 dude = message.author
 word = "mushtaq"
 if word in message.content:
  print('message saved..')
  count = re.split(r'\s|(?<!\d)[,.](?!\d)', message.content)
  total = count.count(word)
  add = word
  if total > 0:
   for word in range(total):
    new = open('mustaq.txt', 'a+')
    damn =('\n {} {}').format(add,dude)
    new.write(damn)
    with open('mustaq.txt') as f:
     content = f.read()
     yo = content.count('mushtaq') + 1
     author = message.author.name
     new.close()
     embed = discord.Embed(
     color = discord.Colour.orange()
     )
     embed.set_author(name='Mushtaq')
     embed.add_field(name='sum of Mustaqs', value='{} has been called {} times by {}'.format(add,yo,author),inline=False)
     await message.channel.send(embed=embed)
 await client.process_commands(message)
  


@client.command()
async def resetM(ctx):
 await ctx.send('are you sure you want to delete all the mushtaqeens we counted ?')
 def msg(msg):
  return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in ['yes', 'no']        
 msg = await client.wait_for("message", check=msg)

 if msg.content.lower() == "yes":
  dele = open('mustaq.txt', 'r+')
  dele.truncate(0)
  await ctx.send("all mushtaqeens are gone :(")     
 else:
     await ctx.send("the mushtaqeens are saved!")


@client.command()
async def countM(ctx):
 guild = ctx.guild
 with open('mustaq.txt') as f:
  content = f.read()
  alo = []
  for member in guild.members:
   alo.append(member.name)
   if content in alo:    
    print(alo)
    mus = content.count('mushtaq')
    embed = discord.Embed(
    color = discord.Colour.red()
    )
    embed.set_author(name='who said it the most')
    embed.add_field(name='who', value='hi',inline=False)
    await ctx.send(embed=embed)



@client.command()
async def rain(ctx):
 d = datetime.today()
 date = d.strftime("%B %d, %Y")
 rain = open('rain.txt', 'a+')
 when = "\n raind on {} ".format(date)
 rain.write(when)
 embed = discord.Embed(color = discord.Colour.blue())
 embed.set_author(name='Rain')
 embed.add_field(name='Rain', value="raind on {} ".format(date),inline=False)
 await ctx.send(embed=embed)


@client.command()
async def func(ctx):
 await ctx.send('Type the values of n1, n2, N1 and N2 (use a single space between each value)')
 def msg(msg):
  return msg.author == ctx.author and msg.channel == ctx.channel      
 msg = await client.wait_for("message", check=msg)
 n1,n2,N1,N2= str.split(msg.content)
 length = int(N1) + int(N2)
 V = int(n1) + int(n2)
 logofn = round(math.log10(15),4)
 logof2 = round(math.log10(2),4)
 log = round(logofn/logof2,4)
 vol = round(log * length,4)
 diffn1 = int(n1) / 2
 diffn2 = int(N2) / int(n2)
 diff = diffn1 * diffn2
 E = diff * vol
 embed = discord.Embed(
 color = discord.Colour.orange()
 )
 embed.set_author(name='Function points')
 embed.add_field(name='the answer', value='the length is: {} \n the vocab is: {} \n the volume is: {} \n the diff is: {} \n the Effort is: {}'.format(length,V,vol,diff,E),inline=False)
 await ctx.channel.send(embed=embed)










client.run('NzcxMzcxNDgwMDUwNTY1MTMw.X5rJrA.xrPaYc1jd_UTyucg4YtsMIDVmtE')

