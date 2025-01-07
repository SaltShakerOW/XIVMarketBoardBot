# XIVMarketBoardBot

XIVMarketBoardBot is a Python powered Discord chat bot that allows the user to check and display data related to the online MMORPG Final Fantasy XIV: Online's market board from the comfort of your own discord chat session.

## Features

- Searches and displays the data related to the lowest price of a user specified item (for all data-centers currently)
- Displays and graphs past pricing data related to a user specified item (WIP)
## Dependancies

XIVMarketBoardBot requires several libaries and APIs to function properly:

- [Universalis] - The black magic API used to scrape all FFXIV market board data in real-time.
- [discord.py] - The library used to interact with the discord client.
- [pandas] - Used to process large amounts of FFXIV item data
- [Requests] - Used to send and receive HTTP requests to and from Universalis
- [xiv-datamining's Item Spreadsheet] - A massive spreadsheet documenting every item in the game

## Installation and Setup

First, if you haven't already, create a discord account. If you don't know how to do this, navigate to https://discord.com/ and click "Login." This will prompt you to enter in a email and password combination, but underneath lies a registration link. Click that and fill out the form to create a fresh account.

Once you have an account in your pocession, I recommend creating a fresh discord server or existing server to run the bot in. This can be done through the plus "+" icon on the left hand side of the screen. Simply create your own server designed for "me and my friends" and name it whatever you please. Once done, you should now be the owner of a fresh discord server.

Now that that's out of the way, we can get into the nitty gritty. To activate the bot, first download the source code from the XIVMarketBoardBot GitHub repo. This can be done through cloning the repo to your machine through Git, or simply downloading it as a ZIP file. Either way, this can be done through the bright green "<> Code" button at the top left of the repo. Once you have the files, ensure they are in a safe location.

You will notice that the file is missing a .env file to house all of the data needed to connect to your discord server. This is intentionally done because a .env file's purpose is to store sensitive keys that must not be shared. Simply create a file called ".env" in the code's root directory and open it in your favorite text editor and copy this line of text and hit save.
```
DISCORD_TOKEN=
```

This will create a safe spot for our discord key to live. But where do we get this key? We first need to go to the [Discord Developer Portal](https://discord.com/developers/applications), which you can gain access to through the Discord account we created a few steps ago, or through your own prexisting account. You then want to press "New Application" in the top right corner of your screen and name it "XIVMarketBoardBot".

You will then be greated by a large set of options. You want to navigate to the "Bot" section on the left hand navigation bar and press on "Reset Token". Take this long string of characters and store it within that .env file we created earlier, assigning our DISCORD_TOKEN varible to the key you just generated.

We then need to give our bot permissions to do the things it needs to be able to do, such as send and read messages. This is done through the "OAuth2" section on the left hand navigation bar in the "OAuth2 URL Generator" section. Select the "bot" option and select "Send Messages" in the "Bot Permissions" section.

You will then see a URL at the bottom of the page. Paste it into a web browser, and assuming you are still logged into your Discord account, select the server we had created earlier to add the bot to it. It should then appear in the server offline.

The one last thing we must do in the Developer Portal is to grant it intents. This is done through the "bot" section on the left hand navigation bar and it is recommended to select all of the options ("Presence Intent", "Server Memebers Intent", and "Message Content Intent"). Make sure to save these changes.

The last thing to do before execution is to grab the server ID of where the bot will talk. This can be done through enabling developer mode in Discord through Settings>Advanced>Developer Mode, and right clicking on the channel you wish to have the bot speak in and copying its Channel ID. We will then create another .env entry with the key of CHANNEL_ID as seen below, and insert the channel ID we just copied into the variable. 
```
CHANNEL_ID=
```

Once that is done, you're all set! Simply execute the "bot.py" file in your code's root directory and you should be off to the races!


## Disclaimer
Please note that this project is VERY WIP, and there will likely need to be extensive modifications/additions to this code base in order to get it working the and with the features I set out to add. Please feel free to put in any pull requests you'd like, as this is a very open source project. Also, please let me know of any bugs that are in need of fixing. Thanks for checking out my stuff!

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

[Universalis]: <https://docs.universalis.app/>
[discord.py]: <https://discordpy.readthedocs.io/en/stable/>
[pandas]: <https://pandas.pydata.org/>
[Requests]: <https://requests.readthedocs.io/en/latest/>
[xiv-datamining's Item Spreadsheet]: <https://raw.githubusercontent.com/xivapi/ffxiv-datamining/refs/heads/master/csv/Item.csv>


