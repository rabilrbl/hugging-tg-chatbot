import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ConversationHandler
)
from hugging_tg_chatbot.handlers import (
    start,
    help_command,
    message_handler,
    new_command_handler,
    model_command_handler,
    change_model_callback_handler,
    SYSTEM_PROMPT_SP,
    CANCEL_SP,
    start_system_prompt,
    get_system_prompt,
    cancelled_system_prompt,
    info_command_handler
)
from hugging_tg_chatbot.filters import AuthFilter, MessageFilter
from dotenv import load_dotenv

load_dotenv()


def start_bot():
    app = Application.builder().token(os.getenv("BOT_TOKEN")).build()

    app.add_handler(CommandHandler("start", start, filters=AuthFilter))
    app.add_handler(CommandHandler("help", help_command, filters=AuthFilter))
    app.add_handler(CommandHandler("new", new_command_handler, filters=AuthFilter))
    app.add_handler(CommandHandler("model", model_command_handler, filters=AuthFilter))
    app.add_handler(CommandHandler("info", info_command_handler, filters=AuthFilter))
    
    app.add_handler(
        ConversationHandler(
            entry_points=[CommandHandler("system_prompt", start_system_prompt, filters=AuthFilter)],
            states={
                SYSTEM_PROMPT_SP: [MessageHandler(MessageFilter, get_system_prompt)],
                CANCEL_SP: [CommandHandler("cancel", cancelled_system_prompt, filters=AuthFilter)],
            },
            fallbacks=[CommandHandler("cancel", cancelled_system_prompt, filters=AuthFilter)],
        )
    )
    
    app.add_handler(MessageHandler(MessageFilter, message_handler))
    app.add_handler(
        CallbackQueryHandler(change_model_callback_handler, pattern="^change_model_")
    )

    # Run the bot until the user presses Ctrl-C
    app.run_polling(allowed_updates=Update.ALL_TYPES)