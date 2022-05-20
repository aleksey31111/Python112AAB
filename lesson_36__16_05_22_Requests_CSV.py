print("### Lesson API ### JSON API ###")
print("1) Install <virtenv>")
print("2) ## pip install requests ##")
print('1 1  ' * 20)
print("3) Work with https://jsonplaceholder.typicode.com/todos")

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
print('1 1  ' * 20)
print()

print("2 " * 30)
print("#### CSV (Comma Separated Values) ####\n"
      "#### data.csv ####\n"
      "\tИмя, Профессия, Год Рождения\n"
      "\tВиктор, Веб-дизайнер, 1995\n"
      "Игорь, Программист,1983")

import csv

print("Variant 1. csv.reader(descriptor, delimiter=';'")
with open('data_36.csv') as r_file:
    file_reader = csv.reader(r_file, delimiter=";")

with open('data_36_1.csv') as r_file:
    file_reader = csv.reader(r_file, delimiter=";")
    count = 0

    # print(file_reader)  # Print Object <file_reader>
    for row in file_reader:
        if count == 0:
            print(f"Файл Содержит Столбцы: {', '.join(row)}")
        else:
            print(f"\t{row[0]} - {row[1]}. Родился в {row[2]} году.")
        count += 1
    print(f"Всего в Файле {count} строки.")
print()
print("VARIANT 2. csv.DictReader")
# with open('data_36_1.csv') as r_file:
with open('data_36_2.csv') as r_file:
    fieldnames = ['Имя', 'Профессия', 'Год Рождения']
    file_reader = csv.DictReader(r_file, delimiter=";", fieldnames=fieldnames)
    count = 0

    for row in file_reader:
        if count == 0:
            print(f"Файл Содержит Столбцы: {', '.join(row)}")
        print(f"\t{row['Имя']} - {row['Профессия']}. Родился в {row['Год Рождения']} году.")
        count += 1
    print(f"Всего в Файле {count} строки.")
print("2 " * 30)
print()
print("3 " * 25)
print("Variant 1: csv.writer")
with open('student_36.csv', mode='w') as f:
    writer = csv.writer(f, delimiter=";", lineterminator="\r\n")
    writer.writerow(['Имя', 'Класс', 'Возраст'])
    writer.writerow(['Женя', '9', '15'])
    writer.writerow(['Саша', '5', '12'])
    writer.writerow(['Маша', '11', '18'])
print()

print("Variant 2: csv.writer Nested List")
data = [['hostname', 'vendor', 'model', 'location'],
        ['sw1', 'Cisco', '3750', 'London, Best str'],
        ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
        ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
        ['sw4', 'Cisco', '3650', 'London, Best str']]
#
with open('sw_data_new_36.csv', 'w') as f:
    writer = csv.writer(f, delimiter=';', lineterminator='\r', quoting=csv.QUOTE_NONNUMERIC)
    for row in data:
        writer.writerow(row)

with open('sw_data_new_36.csv') as f:
    print(f.read())
#
print("Variant 4")

data = [['hostname', 'vendor', 'model', 'location'],
        ['sw1', 'Cisco', '3750', 'London, Best str'],
        ['sw2', 'Cisco', '3750', 'London, Best str'],
        ['sw3', 'Cisco', '3750', 'London, Best str'],
        ['sw4', 'Cisco', '3750', 'London, Best str'],]

with open('sw_data_new.csv', 'w') as f:
    writer = csv.writer(f, lineterminator="\r\n", quoting=csv.QUOTE_NONNUMERIC)
    for row in data:
        writer.writerow(row)

with open('sw_data_new.csv', 'r') as f:
    print(f.read())

import csv

print("Variant 5")
with open("student2.csv", "w") as f:
    names = ['Имя', 'Возраст']
    file_writer = csv.DictWriter(f, delimiter=",", lineterminator="\r", fieldnames=names)
    file_writer.writeheader()
    file_writer.writerow({'Имя':'Саша', 'Возраст': '6'})
    file_writer.writerow({'Имя': 'Маша', 'Возраст': '15'})
    file_writer.writerow({'Имя': 'Вова', 'Возраст': '14'})



# print("Variant 7")
data = [{
    'hostname': 'sw1',
    'location': 'London',
    'model': '3750',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw2',
    'location': 'Liverpool',
    'model': '3850',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw3',
    'location': 'Liverpool',
    'model': '3650',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw4',
    'location': 'London',
    'model': '3650',
    'vendor': 'Cisco'
}]

with open('dictwriter_36.csv', 'w') as f:
    write = csv.DictWriter(f, fieldnames=list(data[0].keys()), lineterminator='\r')
    write.writeheader()
    for d in data:
        write.writerow(d)
print()

print("bs4 " * 20)
print(" pip install beatifulsoup4 ")
print(" bs4" * 20)

from bs4 import BeautifulSoup

f = open('index.html').read()
soup = BeautifulSoup(f, 'html.parser')
row = soup.find("div", class_="name").text
row = soup.find_all("div", class_="name")
print(row)
row = soup.find_all("div", class_="row")[1].find_all('div', class_='links')
print(row)
row = soup.find_all("div", {"class": "name"})
print(row)
#