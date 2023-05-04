from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "24284247"))
API_HASH = getenv("API_HASH", "0df90bc85e18922bf38e5c0b6f0f22c9)
BOT_TOKEN = getenv("BOT_TOKEN", "6293970196:AAH8JfxIuBkBFWm0--lykf6FFFqDLm4v6jI")
SESSION_NAME = getenv("SESSION_NAME", "1BJWap1wBuydfoDbRj0lUuYOSdfWBfNOeBajgROxqJieB5zHZw5wsanPbC8JQqzC_p8_Jj5QJ20vVseQmAAetO0rd359KjiYHw1LRqNsMKrzY7QvqbtxbdWOskRXuTmtfGMSUj_AqKaNC_rWlrGM1zSSbsH4MiYFW_TMnR9NHO770TA6Fwiu1S8HLYxPtO5pEFV0_SDAbm5vOOaMXqEB6pmMYLFM7UM3JTXUv7uMuvbnV5zW1WDah4crRT3rjI-WBVwR6dFeUA9y1qPOkRIRE5rrhH7s1ikBq-OAT0J5_AaGomKvweFujOTNa_JmNwEDYsfnJ7yfhY7Tz8vq1aignG1kSRHdNLrQ=)

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "z_p_p_y")
ALIVE_NAME = getenv("ALIVE_NAME", "song")
BOT_USERNAME = getenv("BOT_USERNAME", "t_t_e_e_t_t_o_obot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "GU_NR")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "z_k_p_y")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "1854384004").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
