import discord
from discord.ext import commands
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "بۆتەکە بە سەرکەوتوویی کار دەکات!"

def run_server():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run_server)
    t.start()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'THE WOLVES Bot is online! Logged in as {bot.user.name}')
    await bot.change_presence(activity=discord.Game(name=".help | THE WOLVES"))

@bot.command()
async def سلاو(ctx):
    await ctx.send(f'سلاو لە تۆش {ctx.author.mention}! چۆن دەتوانم یارمەتیت بدەم؟')

@bot.command()
async def server(ctx):
    name = str(ctx.guild.name)
    memberCount = str(ctx.guild.member_count)
    await ctx.send(f"ناوى سێرڤەر: {name}\nژمارەی ئەندامان: {memberCount}")

keep_alive()
bot.run('MTM0ODk3ODkyNTY2MjQyNjE5NA.GXBEqX.NvQvoOMaS8rwzAEXE8CZZPcyecPiKbjX1eDI5w')
