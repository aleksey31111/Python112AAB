import pickle
import os.path

class Article:
    def __init__(self, title, author, pages, description):
        self.title = title
        self.author = author
        self.pages = pages
        self.description = description

    def __str__(self):
        return f'{self.title} ({self.author})'


class ArticleModel:
    def __str__(self):
        self.db_name = 'db.txt'
        self.article = self.load_data()

    def add_article(self, dict_article):
        article = Article(*dict_article.values())
        self.article[article.title] = article

    def get_all_articles(self):
        return self.articles.values()

    def get_single_article(self, user_title):
        article = self.articles[user_title]
        dict_article = {
            'Название': article.title,
            'author': article.author,
            'Number Char': article.pages,
            'Description': article.description
        }
        return dict_article

    def remove_article(self):
        return self.articles.pop(user_title)

    def load_data(self):
        if os.path.exists(self.name):
            with open(self.db_name, 'rb') as f:
                return pickle.load(f)

        else:
            return dict()

    def save_data(self):
        with open(self.db_name, 'wb') as f:
            pickle.dump(self.articles, f)

