from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int("39342891")
API_HASH = "68687eb7013eddae0609e4dc1d3162c2"

# Your Main Bot Token 
BOT_TOKEN = "9146432058:AAHoRgWx3zeOj0_YSVIn9V9tPMCKvnQP0MY"

# Owner ID For Broadcasting 
OWNER_ID = int("8416917212") # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = "mongodb+srv://priyanshuparida760_db_user:Priyanshu12345@cluster0.5eegtqb.mongodb.net/"

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))
