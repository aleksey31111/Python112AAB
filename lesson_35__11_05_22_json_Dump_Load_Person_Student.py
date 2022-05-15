import json

print("&35_1" * 20)
print("JSON формат при Работе в Python.")
data = {
    "firstName": "Jane",
    "lastName": "goe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}
print("Запись в Файл.")
with open("data_file_35.json", "w") as fw:
    json.dump(data, fw, indent=4)
print("Считывание Из Файла.")
with open("data_file_35.json", "r") as fw:
    data1 = json.load(fw)
    print(data1)
print("Запись в Память")
json_string = json.dumps(data, sort_keys=True)
print("Считывание Из Памяти.")
data1 = json.loads(json_string)
print(data1)
print("&35_1" * 20)

print("############### " * 4)
print("\tРабота с Кирилицей (Русский Алфавит) print(json.dumps(y, ensure_ascii=False))")
# import json
#
x = {'name': 'Виктор'}
y = {'name': 'Виктор'}

print(json.dumps(x))
print(json.dumps(y, ensure_ascii=False))
print("############### " * 4)

print("######################" * 2)
print("Генерация Имени из Букв и Телефона из Цифр")
# import json
from random import choice


def gen_person():
    name = ''
    tel = ''

    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letter)
    # print(name)

    while len(tel) != 10:
        tel += choice(nums)
    # print(tel)

    # gen_person()

    person = {
        'name': name,
        'tel': tel
    }

    return person


print(gen_person())
print()
print("##### Упорядочивание 5 Словарей из Имен и Телефонов #####")
person = []
for i in range(5):
    print(gen_person())
print()
print("  Собирание 6 Словарей из Имен и Телефонов в Список.")
person = []
for i in range(6):
    person.append(gen_person())
print(person)
print()
print("Запись Имен и Телефонов в JSON - Файл \n"
      " НеЧитабельный JSON формат при повторном Добавлении.")
person = []
for i in range(6):
    person.append(gen_person())

with open("person_34.json", "w") as f:
    json.dump(data, f, indent=3)
print(person)
print()
print("Запись Имен и Телефонов в JSON Файл person_34.json\n"
      " Читабельный JSON Формат При Повторном Добавлении.")


def write_json(personal_dict):
    try:
        data = json.load(open('persons_35_1.json'))
    except FileNotFoundError:
        data = []
    data.append(personal_dict)
    with open('persons_35_1.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person())

print(person)
print()

print('@! ' * 30)
print("########## TASK 1 Lesson 35  #########")
print("Создать Класс Student, с Возможностью Добавления, Удаления,\n"
      "\tИзменения Оценок и Подсчета Среднего Балла.\n"
      "Создать Класс Group, который Принимает Список Студентов.\n"
      "Реализовать Возможность Добавления, Удаления Студента в Группу\n"
      "\tи Перевода Студентов Между Группами.\n"
      "Необходимо Реализовать Запись Данных о Студенте в Файл\n"
      "\tи Возможность Считывания Данных из Файла.\n"
      "\tА также Запись Данных в Файл о Группе Студентов и Считывание Данных.")


# import json
# import random
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        # return f'Student:{self.name}: {self.marks}'
        c = ''
        for i in self.marks:
            c += str(i) + ', '
        return f'Student: {self.name}: {c[:-2]}'

    #         return f"Студент: {self.name}: {[i for i in self.marks]}"

    def add_marks(self, mark):
        return self.marks.append(mark)

    def delete_mark(self, index):
        self.marks.pop(index)

    def edit_mark(self, index, new_marks):
        self.marks[index] = new_marks

    def average_mark(self):
        return round(sum(self.marks) / len(self.marks), 2)

    @classmethod
    def dump_to_json(cls, stud, filename):
        try:
            data = json.load(open(filename))
        except FileNotFoundError:
            data = []
        data.append({"name": stud.name, "marks": stud.marks})

        # data = {"name": stud.name, "marks": stud.marks}
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    @classmethod
    def load_from_file(cls, filename):
        with open(filename, 'r') as f:
            print(json.load(f))


st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
print(st1)
st1.add_marks(5)
print(st1)
st1.delete_mark(-2)
print(st1)
st1.edit_mark(2, 5)
print(st1)
print(st1.average_mark())


class Group:
    def __init__(self, students, group):
        self.students = students
        self.group = group

    def __str__(self):
        # return f"{self.student}"
        c = ''
        for i in self.students:
            c += str(i) + '\n'
        # return f"{c}"
        return f"Группа: {self.group}\n{c}"

    def add_student(self, student):
        self.students.append(student)

    # Удаление Студента С Возвратом Значения.
    def remove_student(self, index):
        return self.students.pop(index)

    # Перевод Между Группами
    @classmethod
    def change_group(cls, group1, group2, index):
        return group2.add_student(group1.remove_student(index))

    @classmethod
    def dump_group(cls, file, group):
        try:
            data = json.load(open(file))
        except FileNotFoundError:
            data = []

        with open(file, 'w') as f:
            stud_lst = []
            for i in group.students:
                stud_lst.append([i.name, i.marks])
            tmp = {"Students": stud_lst}
            data.append(tmp["Students"])
            json.dump(data, f, indent=2)

    @classmethod
    def upload_group(cls, file):
        with open(file, 'r') as f:
            print(json.load(f))


st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])
sts = [st1, st2]

my_group = Group(sts, "ГК Python")

print(my_group)
my_group.add_student(st3)
print(my_group)
my_group.remove_student(0)
print(my_group)

group22 = [st1]
my_group2 = Group(group22, "ГК Web")
print(my_group2)

Group.change_group(my_group, my_group2, 0)
print(my_group)
print(my_group2)

Student.dump_to_json(st1, 'student_35.json')
Student.dump_to_json(st2, 'student_35.json')
# Student.load_from_file('student_35.json')
Student.dump_to_json(st3, 'student_35.json')
Student.load_from_file('student_35.json')

# Group.dump_group('group_35.json', my_group)


Group.dump_group('group_35.json', my_group2)
Group.upload_group('group_35.json')
