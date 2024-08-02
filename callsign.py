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
    'INTERNATIONAL': ':united_nations:',
    'UNITED KINGDOM': ':flag_gb:',
    'NETHERLANDS': ':flag_nl:',
    'ITALY': ':flag_it:',
    'NEW ZEALAND': ':flag_nz:',
    'TAIWAN': ':flag_tw:',
    'GREECE': ':flag_gr:',
    'AUSTRALIA': ':flag_au:',
    'GERMANY': ':flag_de:',
    'CZECHIA': ':flag_cz:',
    'CHILE': ':flag_cl:',
    'IRELAND': ':flag_ie:',
    'MALTA': ':flag_mt:',
    'FRANCE': ':flag_fr:',
    'SPAIN': ':flag_es:',
    'TURKEY': ':flag_tr:',
    'SAUDI ARABIA': ':flag_sa:',
    'ALGERIA': ':flag_dz:',
    'ISRAEL': ':flag_il:',
    'POLAND': ':flag_pl:',
    'UNITED ARAB EMIRATES': ':flag_ae:',
    'CANADA': ':flag_ca:',
    'BELGIUM': ':flag_be:',
    'NORWAY': ':flag_no:',
    'QATAR': ':flag_qa:',
    'MALAYSIA': ':flag_my:',
    'PERU': ':flag_pe:',
    'BRAZIL': ':flag_br:',
    'COLOMBIA': ':flag_co:',
    'JORDAN': ':flag_jo:',
    'SWEDEN': ':flag_se:',
    'SOUTH KOREA': ':flag_kr:',
    'EUROPEAN UNION': ':eu:',
    'MOROCCO': ':flag_ma:',
    'AUSTRIA': ':flag_at:',
    'DENMARK': ':flag_dk:',
    'BAHAMAS': ':flag_bs:',
    'BAHRAIN': ':flag_bh:',
    'BANGLADESH': ':flag_bd:',
    'NATO': ':nato:',
    'SINGAPORE': ':flag_sg:',
    'PORTUGAL': ':flag_pt:',
    'PHILIPPINES': ':flag_ph:',
    'BOLIVIA': ':flag_bo:',
    'BULGARIA': ':flag_bg:',
    'MILDENHALL': ':flag_gb:',
    'PAKISTAN': ':flag_pk:',
    'HUNGARY': ':flag_hu:',
    'JAPAN': ':flag_jp:',
    'RUSSIA': ':flag_ru:',
    'SENEGAL': ':flag_sn:',
    'SLOVENIA': ':flag_si:',
    'SWITZERLAND': ':flag_ch:',
    'CROATIA': ':flag_hr:',
    'FINLAND': ':flag_fi:',
    'CYPRUS': ':flag_cy:',
    'EL SALVADOR': ':flag_sv:',
    'EGYPT': ':flag_eg:',
    'ESTONIA': ':flag_ee:',
    'MEXICO': ':flag_mx:',
    'ARGENTINA': ':flag_ar:',
    'GABON': ':flag_ga:',
    'INDIA': ':flag_in:',
    'SOUTH AFRICA': ':flag_za:',
    'HONDURAS': ':flag_hn:',
    'THAILAND': ':flag_th:',
    'KUWAIT': ':flag_kw:',
    'KOREA': ':flag_kr:',
    'ROMANIA': ':flag_ro:',
    'LATVIA': ':flag_lv:',
    'LITHUANIA': ':flag_lt:',
    'OMAN': ':flag_om:',
    'TUNISIA': ':flag_tn:',
    'NIGER': ':flag_ne:',
    'NIGERIA': ':flag_ng:',
    'TRINIDAD & TOBAGO': ':flag_tt:',
    'ORGANIZATION OF EASTERN CARIBBEAN STATES': ':flag_ag:',
    'HMS WESTMINSTER FLIGHT': ':flag_gb:',
    'SLOVAKIA': ':flag_sk:',
    'INDONESIA': ':flag_id:',
    'TCHAD': ':flag_td:',
    'UNITED NATIONS': ':united_nations:',
    'IVORY COAST': ':flag_ci:',
    'RUSSIAN FEDERATION': ':flag_ru:',
    'MONGOLIA': ':flag_mn:',
    'ANGOLA': ':flag_ao:',
    'SUDAN': ':flag_sd:',
    'IRAN (ISLAMIC REPUBLIC OF)': ':flag_ir:',
    'GHANA': ':flag_gh:',
    'KENYA': ':flag_ke:',
    'REPUBLIC OF KOREA': ':flag_kr:',
    'SAN MARINO': ':flag_sm:',
    'GAMBIA': ':flag_gm:',
    'GUATEMALA': ':flag_gt:',
    'KAZAKHSTAN': ':flag_kz:',
    "COTE D'IVOIRE": ':flag_ci:',
    'TIMOR-LESTE': ':flag_tl:',
    'VENEZUELA': ':flag_ve:',
    'GEORGIA': ':flag_ge:',
    'GUERNSEY': ':flag_gg:',
    'KYRGYZSTAN': ':flag_kg:',
    'BARBADOS': ':flag_bb:',
    'COSTA RICA': ':flag_cr:',
    'ECUADOR': ':flag_ec:',
    'URUGUAY': ':flag_uy:',
    'UKRAINE': ':flag_ua:',
    'DOMINICAN REPUBLIC': ':flag_do:',
    'UGANDA': ':flag_ug:',
    'PANAMA': ':flag_pa:',
    'CONGO': ':flag_cg:',
    'REPUBLIC OF MOLDOVA': ':flag_md:',
    'CUBA': ':flag_cu:',
    'AFGHANISTAN': ':flag_af:',
    'SAO TOME AND PRINCIPE': ':flag_st:',
    'LIBYA': ':flag_ly:',
    'CAMEROON': ':flag_cm:',
    'CHINA': ':flag_cn:',
    'MAURITANIA': ':flag_mr:',
    'SAINT VINCENT AND THE GRENADINES': ':flag_vc:',
    'UNITED REPUBLIC OF TANZANIA': ':flag_tz:',
    'ALBANIA': ':flag_al:',
    'ICELAND': ':flag_is:',
    'MYANMAR': ':flag_mm:',
    'GUINEA-BISSAU': ':flag_gw:',
    'BOTSWANA': ':flag_bw:',
    'BURKINA FASO': ':flag_bf:',
    'MOZAMBIQUE': ':flag_mz:',
    'ARMENIA': ':flag_am:',
    'SERBIA': ':flag_rs:',
    'HAITI': ':flag_ht:',
    'JAMAICA': ':flag_jm:',
    'KIRIBATI': ':flag_ki:',
    "DEMOCRATIC PEOPLE'S REPUBLIC OF KOREA": ':flag_kp:',
    'MADAGASCAR': ':flag_mg:',
    'MALAWI': ':flag_mw:',
    'MARSHALL ISLANDS': ':flag_mh:',
    'MAURITIUS': ':flag_mu:',
    'VIET NAM': ':flag_vn:',
    'MONTENEGRO': ':flag_me:',
    'NAMIBIA': ':flag_na:',
    'NEPAL': ':flag_np:',
    'PAPUA NEW GUINEA': ':flag_pg:',
    'FIJI': ':flag_fj:',
    'ZIMBABWE': ':flag_zw:',
    'SEYCHELLES': ':flag_sc:',
    'UZBEKISTAN': ':flag_uz:',
    'VANUATU': ':flag_vu:',
    'BURUNDI': ':flag_bi:',
    'BELARUS': ':flag_by:',
    'CHAD': ':flag_td:',
    'TURKMENISTAN': ':flag_tm:',
    'IRAQ': ':flag_iq:',
    'YEMEN': ':flag_ye:',
    'RWANDA': ':flag_rw:',
    'CAMBODIA': ':flag_kh:',
    'AZERBAIJAN': ':flag_az:',
    'TAJIKISTAN': ':flag_tj:',
    'TOGO': ':flag_tg:',
    'CENTRAL AFRICAN REPUBLIC': ':flag_cf:',
    'PALAU': ':flag_pw:',
    'BOSNIA AND HERZEGOVINA': ':flag_ba:',
    'LEBANON': ':flag_lb:',
    'BENIN': ':flag_bj:',
    'MALDIVES': ':flag_mv:',
    'BERMUDA': ':flag_bm:',
    'BHUTAN': ':flag_bt:',
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
