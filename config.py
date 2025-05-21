import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "24828197")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "d36e278e89ebeb900aeda4128d413a77") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7293747094:AAGMF2OcCkcgcUibCu0oQllkrhmWviDRBMM") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', 'XIAO_BOTS') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "mongodb+srv://Krishna:krishna@cluster0.ecime.mongodb.net/")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","XIAO_BOTS") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "7660990923")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1002595090996')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://files.catbox.moe/2uiu0q.jpg")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


    caption = """
**File Name**: {0}

**Original File Size:** {1}
**Encoded File Size:** {2}
**Compression Percentage:** {3}

__Downloaded in {4}__
__Encoded in {5}__
__Uploaded in {6}__
"""
