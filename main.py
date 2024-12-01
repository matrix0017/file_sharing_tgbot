from pyrogram import Client , filters

bot = Client(
    "filesharing",
    api_id:= 22881482,
    api_hash ="c3cc63dd8419c3eabf9aa637f64c5d22",
    bot_token= "7847022400:AAFoDeEX071VNjP9WURvFWnfHmnErGhE3Bs"

)
@bot.on_message(filters.command('start') & filters.private)
def command1(bot , message):
    bot.send_message(message.chat.id , "Heyo , I'm a simple file sharing bot")
    
bot.run()