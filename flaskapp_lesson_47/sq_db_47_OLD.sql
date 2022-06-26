CREATE TABLE IF NOT EXISTS mainmenu(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
url TEXT NOT NULL
);

from flask-app.main import create_db
create_db()