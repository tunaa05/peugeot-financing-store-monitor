import os
from dotenv import load_dotenv

load_dotenv()

# Discord webhook URL
DISCORD_WEBHOOK_URL = os.getenv(
    "DISCORD_WEBHOOK_URL",
    "https://discord.com/api/webhooks/1439725920121389076/VpPM8C4yAAjHZu4LZUdrM0GEGVfvxMkhLkWn6OBeOkN_5AIfHhgVWRmlYnnktOm291Qa"
)

# Price range (monthly lease rate in euros)
MIN_PRICE = float(os.getenv("MIN_PRICE", "50"))
MAX_PRICE = float(os.getenv("MAX_PRICE", "120"))

# Yearly kilometer allowance (km per year)
KM_ALLOWANCE = int(os.getenv("KM_ALLOWANCE", "15000"))

# Check interval in seconds (30 minutes = 1800 seconds)
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", "1800"))

# Peugeot store URL
STORE_URL = "https://financing.peugeot.store/bestand"

# Storage file for tracking seen offers
OFFERS_FILE = "offers.json"

