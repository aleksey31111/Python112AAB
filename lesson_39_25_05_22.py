### Lesson 39 ###
# Сокет - Прог Интерфейс для Обеспечения Информационнргр Обмена между Процессами
#
#
#
import socket

# # Клиентский Сокет
# URLS = {
#     '/': "index page",
#     '/blog': 'blog page'
# }
#
#
# def parse_request(request):
#     parsed = request.split(" ")
#     method = parsed[0]
#     url = parsed[1]
#     return method, url
#
#
# def generate_headers(method, url):
#     if method != 'GET':
#         return 'HTTP/1.1 405 Method Not Allowed!\n\n', 405
#     if url not in URLS:
#         return 'HTTP/1.1 404 Page Not Found!\n\n', 404
#     return 'HTTP/1.1 200 OK!\n\n', 200
#
#
# def generate_response(request):
#     method, url = parse_request(request)
#     header, code = generate_headers(method, url)
#     body = URLS.get(url)
#     return (header + body).encode('utf-8')
#
#
# # Серверный Сокет
# def run():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind(('127.0.0.1', 5000))
#     server_socket.listen()  # 127.0.0.1:5000
#
#     while True:
#         client_socket, addr = server_socket.accept()
#         request = client_socket.recv(1024)
#
#         print(f"Клиент: {addr} => \n{request},decode('utf-8')")
#
#         response = generate_response(request.decode())
#         client_socket.sendall(response)
#         client_socket.close
#
#
# if __name__ == '__main__':
#     run()


#### [19:23] Козякина Елена  ####
# import socket
# from view import index, blob
#
# URLS = {
#     '/': index,  # 'index page',
#     '/blog': blog  #'blog page'
# }
#
#
# def parse_request(request):
#     parsed = request.split(" ")
#     method = parsed[0]
#     url = parsed[1]
#     return method, url
#
#
# def generate_headers(method, url):
#     if method != 'GET':
#         return 'HTTP/1.1 405 Method Allowed!\n\n', 405
#     if url not in URLS:
#         return 'HTTP/1.1 404 Page Not Found!\n\n', 404
#     return 'HTTP/1.1 200 OK!\n\n', 200
#
#
# def generate_content(code, url):
#     if code == 404:
#         return '<h1>404</h1><h3>Page Not Gound</h3>'
#     elif code == 405:
#         return '<h1>404</h1><h3>Page Allowed</h3>'
#     return URLS[url]()
#
#
# def generate_response(request):
#     method, url = parse_request(request)
#     header, code = generate_headers(method, url)
#     # body = URLS.get(url, 'Errors 404')
#     body = generate_content(code, url)
#     return (header + body).encode()
#
#
# def run():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind(('127.0.0.1', 5000))
#     server_socket.listen()  # 127.0.0.1:5000
#     while True:
#         client_socket, addr = server_socket.accept()
#         request = client_socket.recv(1024)
#         print(f"Клиент: {addr} => \n{request.decode('utf-8')}")
#         response = generate_response(request.decode())
#         client_socket.sendall(response)
#         client_socket.close()
#
#
# if __name__ == '__main__':
#     run()



#### DATABASE ####
# SQL - Язык Структурированных Запросов
### Сетевая Модель БазыДанных ###
# COLUMNS
# ROW
# AQLite - *.bd, *.sdb, *.sqlite, *.sqlite3, *.db2



import sqlite3 as sq

#
# con = sq.connect('profile_39.db')
# cur = con.cursor()
#
# cur.execute("""
# """)
#
# con.close()

with sq.connect('profile_39.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE users")
    # cur.execute("""CREATE TABLE IF NOT EXISTS users(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # sum REAL,
    # date TEXT
    # )""")