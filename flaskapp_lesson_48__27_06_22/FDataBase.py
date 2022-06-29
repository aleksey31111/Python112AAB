import sqlite3
import time
import math
import re


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = "SELECT * FROM mainmenu"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print("Ошибка чтения из БД")
        return []

    def add_post(self, title, text, url):
        try:
            self.__cur.execute(INSERT INTO)
                #("SELECT COUNT() as 'count' FROM posts WHERE LIKE ?", (url))
            if res['count'] > 0:
                print("ARticle such URL Exists")
                return False
            base = url_for('static', filename='images')
            text = re.sub(r'(?P<tag><ing\s+[^>]*src=)>)'
                          r'(?P<quote>["\'])(?P<url>.+?)'
                          r'(?P=quote)>',
                          r"\g<tag>" + base + r"/\g<url>"
                          , text)
            # base = url_for('static', filename='images')
            # text = re.sub(r'(?P<tag><img\s+[^>]*src=)(?P<quote>["\'])(?P<url>.+?)(?P=quote)>', r"\g<tag>" + base +
            #               r"/\g<url>>", text)
            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO posts VALUES(NULL,?, ?,?)", (title, text, tm))
        except sqlite3.Error as e:
            print("Error Add article in BD")
            return False

        return True

    def get_post(self, alias):
        try:
            self.__cur.execute(f"SELECT title, text FROM posts WHERE url"
                               f" LIKE {post_id} LIMIT 1")
            res = self.__cur.fetchone()
            if res:
                return res

        except sqlite3.Error as e:
            print("Error Get article in BD")

        return False, False

    def get_posts_anonce(self):
        try:
            self.__cur.execute(f"SELECT id, title, text, url FROM posts "
                               f"ORDER BY time DESC")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Error Get article in BD")

        return []
