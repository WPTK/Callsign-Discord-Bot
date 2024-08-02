import discord
import pandas as pd
import numpy as np

# Load the Excel file
file_path = 'C:\\ADSBxCallsigns\\Callsigns.xlsx'
df = pd.read_excel(file_path)

# Convert all values to strings to avoid issues with nan
df = df.astype(str)

# Convert all relevant columns to uppercase to ensure case-insensitive search
df['CALLSIGN'] = df['CALLSIGN'].str.upper()
df['SSR INDICATION'] = df['SSR INDICATION'].str.upper()

# Create a dictionary for country flags
country_flags = {
    'UNITED STATES': ':flag_us:',
    'CANADA': ':flag_ca:',
    'UNITED KINGDOM': ':flag_gb:',
    'GERMANY': ':flag_de:',
    'FRANCE': ':flag_fr:',
    'JAPAN': ':flag_jp:',
    'AUSTRALIA': ':flag_au:',
    'ITALY': ':flag_it:',
    'SPAIN': ':flag_es:',
    'BRAZIL': ':flag_br:',
    'RUSSIA': ':flag_ru:',
    'CHINA': ':flag_cn:',
    'INDIA': ':flag_in:',
    'MEXICO': ':flag_mx:',
    'SOUTH AFRICA': ':flag_za:',
    'SOUTH KOREA': ':flag_kr:',
    'ARGENTINA': ':flag_ar:',
    'NETHERLANDS': ':flag_nl:',
    'SWEDEN': ':flag_se:',
    'NORWAY': ':flag_no:',
    'DENMARK': ':flag_dk:',
    'FINLAND': ':flag_fi:',
    'POLAND': ':flag_pl:',
    'TURKEY': ':flag_tr:',
    'ISRAEL': ':flag_il:',
    'SWITZERLAND': ':flag_ch:',
    'GREECE': ':flag_gr:',
    'NEW ZEALAND': ':flag_nz:',
    'BELGIUM': ':flag_be:',
    'NATO': ':flag_nato:'
}

# Create an instance of a Client. This handles events and interactions with Discord.
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    try:
        # Ignore messages from the bot itself
        if message.author == client.user:
            return

        # Check if the message starts with "!callsign"
        if message.content.startswith('!callsign'):
            # Extract the keyword and convert to uppercase
            keyword = message.content[len('!callsign '):].strip().upper()

            # Search for the keyword in the "CALLSIGN" and "SSR INDICATION" columns
            result = df[(df['CALLSIGN'] == keyword) | (df['SSR INDICATION'] == keyword)]

            if not result.empty:
                # Check for exact duplicates
                if len(result) > 1:
                    row = result.iloc[0]
                    country = row['COUNTRY'] if row['COUNTRY'] != 'nan' else ''
                    country_flag = country_flags.get(country.upper(), '')
                    final_response = (f"> **Callsign:** {row['CALLSIGN']}\n"
                                      f"> **Unit / Operator:** {row['UNIT / OPERATOR'] if row['UNIT / OPERATOR'] != 'nan' else ''}\n"
                                      f"> **Force:** {row['FORCE'] if row['FORCE'] != 'nan' else ''}\n"
                                      f"> **Country:** {country} {country_flag}\n"
                                      f"> **Note:** {row['NOTE'] if row['NOTE'] != 'nan' else ''}\n")
                else:
                    responses = []
                    for _, row in result.iterrows():
                        country = row['COUNTRY'] if row['COUNTRY'] != 'nan' else ''
                        country_flag = country_flags.get(country.upper(), '')
                        response = (f"> **Callsign:** {row['CALLSIGN']}\n"
                                    f"> **Unit / Operator:** {row['UNIT / OPERATOR'] if row['UNIT / OPERATOR'] != 'nan' else ''}\n"
                                    f"> **Force:** {row['FORCE'] if row['FORCE'] != 'nan' else ''}\n"
                                    f"> **Country:** {country} {country_flag}\n"
                                    f"> **Note:** {row['NOTE'] if row['NOTE'] != 'nan' else ''}\n")
                        responses.append(response)
                    final_response = "\n".join(responses)
            else:
                final_response = 'Sorry! No results found.'

            # Send the response back to the channel
            await message.channel.send(final_response)
    except Exception as e:
        # Print any errors that occur
        print(f'Error: {e}')

# Run the bot with your token
client.run('YOUR_DISCORD_BOT_TOKEN')
