import os, json
from pathlib import Path
from dotenv import load_dotenv
import discord
from discord.ext import commands
from MBData import get_item_data, name_to_id, id_to_name, does_item_exist

description = "A bot that helps keep track of prices on the Final Fantasy XIV Market Board"


#Load Keys/Static Data for operations
load_dotenv('.env')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.dm_messages = True

bot = commands.Bot(command_prefix="!", description=description, intents=intents)

@bot.command()
async def delete_last(ctx):
    # Get the bot's messages in the channel
    messages = []
    async for message in ctx.channel.history(limit=100):  # Adjust limit as needed
        if message.author == bot.user:
            messages.append(message)
            break  # Stop after finding the first message from the bot
    
    # Delete the last message if found
    if messages:
        await messages[0].delete()
        await ctx.send("Last message deleted!", delete_after=5)  # Optional confirmation
    else:
        await ctx.send("No recent messages found to delete.", delete_after=5)

@bot.event
async def on_ready():
    print("XIVMarketBoardBot is ready to be used!")
    channel = bot.get_channel(int(CHANNEL_ID))
    await channel.send("XIVMarketBoardBot is ready to be used!")
    
@bot.command()
async def check(ctx, *, arg):
    item_ID = name_to_id(arg)
    if item_ID == 0:
        await ctx.send("Invalid Item Name. Please try again.")
    else:
        result = get_item_data(itemID=item_ID)
        output_text = format_text(result, 0, item_ID) #0 should be variable but is zero for testing
        await ctx.send(output_text)
        
@bot.command()
async def add_item(ctx, *, arg):
    if does_item_exist(arg) == False:
        await ctx.send("This item doesn't exist (Tip: Make sure the item name is exactly spelled as seen in game)")
    else:
        #code to create a new user entry if it doesn't exist
        with open('user_specifications.json', 'r') as file:
            data = json.load(file)
        
def format_text(data: dict, index: int, itemID: int):
    data_at_index = data['results'][index]
    if data_at_index:
        return f"""
    > Item: {id_to_name(itemID)}
    > Price (Per Unit): {data_at_index['pricePerUnit']}
    > Quantity: {data_at_index['quantity']}
    > Price (Total): {data_at_index['total']}
    > Location: {data_at_index['worldName']}
    > Retainer Name: {data_at_index['retainerName']}
    """
    else:
        return f"No MarketBoard data found..."

def check_if_user_exists(user_id: str):
    with open('user_specifications.json', 'r') as file:
        data = json.load(file)
    for entry in data['data']:
        if entry['user_id'] == user_id:
            return True
        
    return False
        
if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)