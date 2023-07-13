import discord
from discord.ext import commands
import aiohttp
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

@bot.event
async def on_ready():
    print(f"{bot.user} is connected to Discord!")

async def fetch_weather_data(city: str, api_key: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                return None

# Unregister the existing help command
bot.remove_command("help")

@bot.command(name="hello", help="Greets you with your username.")
async def hello(ctx):
    await ctx.send(f"Namaskar, {ctx.author.name}!")

@bot.command(name="echo", help="Repeats the provided text.")
async def echo(ctx, *, text):
    await ctx.send(text)

@bot.command(name="calc", help="Evaluates a mathematical expression.")
async def calc(ctx, *, expression):
    try:
        result = eval(expression)
        await ctx.send(f"The result is: {result}")
    except Exception as e:
        await ctx.send(f"Error: {e}")

@bot.command(name="help", help="Shows the available commands.")
async def help_command(ctx, *args):
    if not args:
        command_list = bot.commands
        embed = discord.Embed(title="🚀 Available Commands", description="These are the cool commands you can use with this bot:", color=0x4B0082)  # Indigo color
        for command in command_list:
            embed.add_field(name=f"!{command.name}", value=command.help, inline=False)
        embed.set_thumbnail(url=bot.user.avatar.url)
        embed.set_footer(text="Enjoy using the bot!", icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)
    else:
        command_name = args[0]
        command = bot.get_command(command_name)
        if command:
            embed = discord.Embed(title=f"Help: !{command_name}", description=command.help, color=0x4B0082)  # Indigo color
            await ctx.send(embed=embed)
        else:
            await ctx.send("Command not found.")

@bot.command(name="weather", help="Shows the current weather for the specified city.")
async def weather(ctx, *, city):
    data = await fetch_weather_data(city, OPENWEATHER_API_KEY)
    if data:
        try:
            weather_desc = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]

            embed = discord.Embed(
                title=f"Weather for {city.capitalize()}",
                description=f"🌡 Temperature: {temp}°C\n"
                            f"🥵 Feels Like: {feels_like}°C\n"
                            f"💧 Humidity: {humidity}%\n"
                            f"☁️ Description: {weather_desc}",
                color=0x4B0082,  # Indigo color
            )
            embed.set_thumbnail(url=f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png")
            embed.set_footer(text="Powered by OpenWeather", icon_url=ctx.author.avatar.url)

            await ctx.send(embed=embed)
        except Exception as e:
            print(f"Error in weather command: {e}")
            await ctx.send("An error occurred while processing the !weather command.")
    else:
        await ctx.send("Could not fetch weather data for the specified city.")

bot.run(DISCORD_BOT_TOKEN)
