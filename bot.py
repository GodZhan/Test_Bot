import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='Test0') #建置BOT實體

@bot.event
async def on_ready():
    print('>>> Bot is online <<<')

@bot.event
async def on_member_join(member):
    ch1 = bot.get_channel(755604074820534309) #取得頻道 CH1 = channel 1 
    await ch1.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    ch1 = bot.get_channel(755604098061041746) 
    await ch1.send(f'{member} leave!')

@bot.command()
    await ctx.send(bot.latency) 
