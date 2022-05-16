### Lesson API ### JSON API ###
## pip install requests ##
import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

# print(todos[:10])

todos_by_user = {}

for todo in todos:
    if todo['completed']:
        try:
            todos_by_user[todo['userId']] += 1
        except KeyError:
            todos_by_user[todo['userId']] = 1

print(todos_by_user)

top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
print(top_users)

max_completed = top_users[0][1]
print(max_completed)

users = []
for user, num_complete in top_users:
    if num_complete < max_completed:
        break
    users.append(str(user))

print(users)

max_users = " and ".join(users)

s = 's' if len(users) > 1 else ""
print(f"user{s} {users} completed {max_completed} TODOs")
print(f"user{s} {max_users} completed {max_completed} TODOs")


def keep(todo):
    is_complete = todo['completed']
    has_max_coubt = str(todo['userId']) in users
    return is_complete and has_max_coubt


with open('filtered_data_file_36.json', 'w') as data_file:
    filter_todos = list(filter(keep, todos))

    json.dump(filter_todos, data_file, indent=2)

with open("filtered_data_file_36.json", "r") as fw:
    data = json.load(fw)
    print(data)
print()

#### CSV (Comma Separated Values) ####
#### data.csv ####
### Имя, Профессия, Год Рождения
### Виктор, Веб-дизайнер, 1995
### Игорь, Программист,1983

import csv

# with open('data_36_1.csv') as r_file:
#     file_reader = csv.reader(r_file, delimiter=";")


import csv

with open('data_36.csv') as r_file:
    file_reader = csv.reader(r_file, delimiter=",")
    count = 0

    # print(file_reader)
    for row in file_reader:
        if count == 0:
            print(f"Файл Содержит Столбцы: {', '.join(row)}")
        else:
            print(f"\t{row[0]} - {row[1]}. Родился в {row[2]} году.")
        count += 1
        print(f"Всего в Файле {count} строки.")

# print("VARIANT 2")
# with open('data_36_2.csv') as r_file:
#     fieldnames = ['Имя', 'Профессия', 'Год Рождения']
#     file_reader = csv.DictReader(r_file, delimiter=",", field_names=fieldnames)
#     count = 0
#
#     # print(file_reader)
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл Содержит Столбцы: {', '.join(row)}")
#         # else:
#         print(f"\t{row['Имя']} - {row['Профессия']}. Родился в {row['Год Рождения']} году.")
#         count += 1
#     print(f"Всего в Файле {count + 1} строки.")


# print("Variant 3")
# with open('student_36.csv', mode='w') as f:
#     writer = csv.writer(f, delimiter=",", lineterminator="\r")
#     writer.writerow(['Имя','Класс','Возраст'])
#     writer.writerow(['Женя', '9', '15'])
#     writer.writerow(['Маша', '11', '18'])
#
#
# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3750', 'London, Best str'],
#         ['sw3', 'Cisco', '3750', 'London, Best str'],
#         ['sw4', 'Cisco', '3750', 'London, Best str'],]
#
# with open('sw_data_new.csv', 'w') as f:
#     writer = csv.writer(f, lineterminator="\r\n", quoting-csv.QUOTE_NONNUMERIC)
#     for row in data:
#         writer.writerow(row)
#
# with open('sw_data_new.csv', 'r') as f:
#     print(f.read())
#
# print("Variant 4")
#
# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3750', 'London, Best str'],
#         ['sw3', 'Cisco', '3750', 'London, Best str'],
#         ['sw4', 'Cisco', '3750', 'London, Best str'],]
#
# with open('sw_data_new.csv', 'w') as f:
#     writer = csv.writer(f, lineterminator="\r\n", quoting-csv.QUOTE_NONNUMERIC)
#     for row in data:
#         writer.writerow(row)
#
# with open('sw_data_new.csv', 'r') as f:
#     print(f.read())

import csv

# print("Variant 5")
# with open("student2.csv", "w") as f:
#     names = ['Имя', 'Возраст']
#     file_writer = csv.DictWriter(f, delimiter=",", lineterminator="\r", fieldnames=names)
#     file_writer.writeheader()
#     file_writer.writerow()
#     file_writer.writerow()
#


# print("Variant 7")
# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# },
#     {
#         'hostname': 'sw2',
#         'location': 'London',
#         'model': '3750',
#         'vendor': 'Cisco'
#     }]
# with open('dictwriter.csv', 'w') as f:
#     write = csv.DictWriter(f, fieldnames)


# pip install beatifulsoup4

from bs4 import BeautifulSoup

f = open('index.html').read()
soup = BeautifulSoup(f, 'html.parser')
# row = soup.find("div", class_="name").text
# row = soup.find_all("div", class_="name")
# row = soup.find_all("div", class_="row")[1].find_all('div', class_='links')
row = soup.find_all("div", {"class": "name"})
print(row)


