import os
import feedparser
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Берём токен из Railway Variables
TOKEN = os.getenv( "8782328242:AAH5gW4CuLhsUdTb4Bmaq7568nTKZdcaMgw")

RSS_FEEDS = {
    "Argentina": "https://eleconomista.com.ar/ultimas-noticias/feed/",
    "Radio Farda": "https://en.radiofarda.com/rssfeeds",
    "Mehr News": "https://en.mehrnews.com/rss"
}

def get_news(feed_url):
    feed = feedparser.parse(feed_url)
    news_text = ""
    for entry in feed.entries[:5]:
        news_text += f"• {entry.title}\n"
    return news_text

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    argentina_news = get_news(RSS_FEEDS["Argentina"])
    farda_news = get_news(RSS_FEEDS["Radio Farda"])
    mehr_news = get_news(RSS_FEEDS["Mehr News"])

    message = (
        f"🇦🇷 Новости Аргентины:\n{argentina_news}\n\n"
        f"🇮🇷 Radio Farda:\n{farda_news}\n\n"
        f"🇮🇷 Mehr News:\n{mehr_news}"
    )

    await update.message.reply_text(message)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("news", news))

app.run_polling()
