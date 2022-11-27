from telegram.ext import *




def s(u,c):
    u.message.reply_text("Hello")




u = Updater("5895389339:AAFxtHGcFItvazTYkYiSDN2EARcRluWVE9U",use_context=True)



u.dispatcher.add_handler(CommandHandler("start",s))


u.start_polling()
u.idle()
