


from flask import Flask
import json
import datetime
from pathlib import Path

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
NEWS_FILE = BASE_DIR / "news_data.json"


@app.route('/news.all.get')
def get_news_all_articles():
    with open(NEWS_FILE, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return json.dumps(data)


@app.route('/news.categories.get')
def get_news_categories():
    time_now_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = {
        'title': 'List of Categories',
        'time': time_now_str,
        'categories': [
            {'id': 1, 'name': 'Sports'},
            {'id': 2, 'name': 'Politics'},
            {'id': 3, 'name': 'Education'}
        ]
    }
    return json.dumps(data)


@app.route('/')
def index():
    return 'Welcome ENSIA Students from Flask!'


if __name__ == "__main__":
    app.run(port=8080)
