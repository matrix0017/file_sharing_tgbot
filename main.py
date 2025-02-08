from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Client(
    "filesharing",
    api_id=22881482,
    api_hash="c3cc63dd8419c3eabf9aa637f64c5d22",
    bot_token="7847022400:AAFoDeEX071VNjP9WURvFWnfHmnErGhE3Bs"
)

# Command handler for '/start'
@bot.on_message(filters.command('start') & filters.private)
def command1(bot, message):
    # Inline keyboard with buttons
    keyboard = [
        [InlineKeyboardButton("Upload File", callback_data='upload_file')],
        [InlineKeyboardButton("Add to Group", url=f"https://t.me/{bot.username}?startgroup=true")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    bot.send_message(
        chat_id=message.chat.id,
        text="Heyo, I'm a simple file sharing bot. Use the buttons below to upload a file or add me to a group.",
        reply_markup=reply_markup
    )

# Callback query handler
@bot.on_callback_query(filters.regex('upload_file'))
def upload_file(bot, query):
    query.message.reply_text("Please send the file you want to upload.")

# File handler
@bot.on_message(filters.document & filters.private)
def handle_file(bot, message):
    file = message.document
    file_id = file.file_id
    file_size = file.file_size

    # Define the size limit (e.g., 10MB)
    size_limit = 10 * 1024 * 1024

    if file_size > size_limit:
        message.reply_text('File is too large to upload. Please upload a smaller file.')
    else:
        # Save the file locally
        file_path = f'./{file.file_name}'
        file.download(file_path)
        message.reply_text(f'File {file.file_name} uploaded successfully!')
        bot.run()
                        