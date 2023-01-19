import discord,asyncio,aiohttp,json
from discord import Webhook
from discord.ext import commands
from operator import iadd
from discord.utils import get 
from discord.commands import Option,slash_command



bot = commands.Bot(command_prefix="!" , intents=discord.Intents.all()) 


#上線回應
@bot.event
async def on_ready():
    print("本開源由 我是人#8315 製作")
    print("請勿修改")
    print("有問題請至 https://discord.gg/WDxmw5WjPY 詢問")
    print("==================================================")
    print(F"{bot.user}已連線")
    activity=discord.Activity(type=discord.ActivityType.watching, name="一款好用的匿名系統") 
    await bot.change_presence(status=discord.Status.dnd,activity=activity)

@slash_command()
@bot.slash_command(name="匿名發言",description="發布匿名訊息")
async def noname(ctx,*,msg):
  async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url("webhookurl", session=session)#更改webhookurl
        await webhook.send(F"{msg}", username="匿名")  
        await ctx.respond("發送成功", ephemeral=True)
        channel = bot.get_channel(紀錄頻道)#輸入紀錄頻道ID
        await channel.send (F"{ctx.author}用匿名說了{msg}")





bot.run("TOKEN")#放上token