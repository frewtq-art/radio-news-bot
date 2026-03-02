import os
import requests
import feedparser
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Берём токен из переменной окружения
TOKEN = os.environ.get("8782328242:AAFZ0CVWJBfuj6fmk9yb9-GRg3lvG7-fbCU")

# RSS-фиды новостей
RSS_FEEDS = {
    "Argentina": "https://eleconomista.com.ar/ultimas-noticias/feed/",
    "Radio Farda": "https://www.en.radiofarda.com/rssfeeds",
    "Mehr News": "http://www.mehrnews.com/rss"
}

# Функция для получения последних 5 новостей из RSS
def get_news(feed_url):
    feed = feedparser.parse(feed_url)
    news_text = ""
    for entry in feed.entries[:5]:
        news_text += f"• {entry.title}\n"
    return news_text

# Обработчик команды /news
async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    argentina_news = get_news(RSS_FEEDS["Argentina"])
    farda_news = get_news(RSS_FEEDS["Radio Farda"])
    mehr_news = get_news(RSS_FEEDS["Mehr News"])

    message = f"🇦🇷 Новости Аргентины:\n{argentina_news}\n\n🇮🇷 Radio Farda:\n{farda_news}\n\n🇮🇷 Mehr News:\n{mehr_news}"
    await update.message.reply_text(message)

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бот запущен! Используй команду /news для получения новостей.")

# Создаём и запускаем бота
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("news", news))

app.run_polling()
