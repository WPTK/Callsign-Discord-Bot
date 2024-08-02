# Callsign-Discord-Bot
Search military and civil callsigns. 

WIP/Concept

![image](https://github.com/user-attachments/assets/1c7fcea1-2f6b-465a-b5f8-38de5f83fc2a)

# Callsign Discord Bot

The Callsign Discord Bot is a Python-based bot that interacts with users on a Discord server to fetch and display information from an Excel spreadsheet. The bot responds to the `!callsign` command, searches the provided Excel file for the specified keyword, and returns the relevant data in a formatted response.

## Features

- Responds to the `!callsign` command.
- Searches for exact and non-exact matches in the specified columns of the Excel file.
- Returns formatted results with bold titles and country flags.
- Handles multiple exact matches by displaying only one result.
- Displays multiple non-exact matches if no exact duplicates are found.

## Prerequisites

- Python 3.x
- Discord bot token
- Required Python libraries: `discord.py`, `pandas`, `openpyxl`

## Setup

### 1. Create a Discord Bot

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click on "New Application" and give it a name.
3. Under the "Bot" tab, click "Add Bot" to create a bot user.
4. Copy the bot token. You will need this to run the bot.

### 2. Clone the Repository

```sh
git clone https://github.com/yourusername/callsign-discord-bot.git
cd callsign-discord-bot

### 3. Fire it up

In terminal/command prompt, go to the folder where you've cloned the repo and run:
`python callsign.py`

You should be up and running! 

