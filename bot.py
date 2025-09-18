import discord
from discord.ext import commands
import random
from utils import load_json

TOKEN = "YOUR_DISCORD_TOKEN"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")

@bot.command()
async def quiz(ctx):
    data = load_json("data/pyqs.json")
    if not data:
        await ctx.send("No dataset loaded.")
        return
    q = random.choice(data)
    msg = f"**{q['question_en']}**\n"
    for i, choice in enumerate(q["choices_en"]):
        msg += f"{i+1}. {choice}\n"
    await ctx.send(msg)

bot.run(TOKEN)
