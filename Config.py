import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "29243172"))
    API_HASH = os.environ.get("API_HASH", "9c0154a1fa268924a82ce74e781059b5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6251651452:AAEHHEhp3akggucPQga6KrlViH-Qw14adCk")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOGkBu3AXYkaCA-B_temAZi9zUcuCU7cawNGXixr7tdmTOJ9y9jJ16zZADaUn2lgY6SFTbWa9XVNnOefs4g2UrpijdEiheOFGa29l_6T_ng_XSXCWf_lGEMZMWzM1QD1GWOPE7cA4SRLTJHILCDQWL1hRmuyZTlCvYXDeRXHS40gCciunCIAdku-0470LrRycW87mr_cXHeDffdERopf5M9FyywH3Cv77UO9Eo_rerKRFhvaYNfoLCyjeNFGwSZ1j4ZQa1e5BqafG9tluvls2FoAxT9zbfQ96ipo_6DHIGS7YFYhoVvaujz0MeTWdruBU_toLVaxi6U9qppUd289Fbj_onEY=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "reddior_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5907105558")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
