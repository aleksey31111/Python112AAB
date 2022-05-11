# import json
#
# data = {
#     "firstName": "Jane",
#     "lastName": "goe",
#     "hobbies": ["running", "sky diving", "singing"],
#     "age": 35,
#     "children": [
#         {
#             "firstName": "Alice",
#             "age": 6
#         },
#         {
#             "firstName": "Bob",
#             "age": 8
#         }
#     ]
# }
#
# # with open("data_file.json", "w") as fw:
# #     json.dump(data, fw, indent=4)
# #
# # with open("data_file.json", "r") as fw:
# #     data1 = json.load(fw)
# #     print(data1)
#
# json_string = json.dumps(data, sort_keys=True)
# data1 = json.loads(json_string)
# print(data1)

###############
# import json
#
# x = {'name': 'Виктор'}
# y = {'name': 'Виктор'}
#
# print(json.dumps(x))
# print(json.dumps(y, ensure_ascii=False))


######################
# import json
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letter)
#     print(name)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#     print(tel)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#
#     return person
#
# ##### Change
# def write_json(personal_dict):
#     try:
#         data = json.load(open('persons_json'))
#     except FileNotFoundError:
#         data = []
#     data.append(personal_dict)
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# # person = []
# for i in range(5):
#     # print(gen_person())
#     # person.append(gen_person())
#     write_json(gen_person())
#
# # print(person)
#
# # with open('persons.json', 'w') as f:
# #     json.dump(person, f, indent=2)
# #
# # print(person)


########## TASK 1  #########
import json
import random
class Student:
    def __init__(self, name, marks):
        self.name =name
        self.marks = marks

    def __str__(self):
        c = ''
        for i in self.marks:
            c += str(i) + ', '
        return f'Student:{self.name}: {c[:-2]}'
        # return f"Студент: {self.name} {[i for i in self.marks]}"

    def add_marks(self, mark):
        return self.marks.append(mark)

    def delete_mark(self, index):
        self.marks.pop(index)

    def edit_mark(self,index, new_marks):
        self.marks[index] = new_marks

    def average_mark(self):
        return sum(self.marks) / len(self.marks)


# st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
# print(st1)
# st1.add_marks()
# st1.delete_mark()
# st1.edit_mark()
# st1.average_mark()

    # @classmethod
    # def dump_to_json(cls, stud, filename):
    #     try:
    #         data = json.load(open(filename))
    #     except FileNotFoundError:
    #         data = []
    #     # data.append(filename)
    #     # with open('persons', 'w') as f:
    #     #     json.dump(data, f, indent=2)
    #
    #     data.append({"name": stud.name, "marks": stud.marks})
    #     with open(filename, 'w') as f:
    #         json.dump(data, f, indent=2)
    #
    # @classmethod
    # def load_form_file(cls, filename):
    #     with open(filename, 'r') as f:
    #         print(json.load())

class Group:
    def __init__(self,students, group):
        self.students = students
        self.group = group

    def __str__(self):
        # return f"{self.student}"
        c =''
        for i in self.students:
            c += str(i) + '\n'
        return f"Группа: {self.group}\n{c}"

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, index):
        return self.students.pop(index)

    @classmethod
    def change_group(cls, group1, group2, index):
        return group2.add_student(group1.remove_student(index))

    # @classmethod
    # def dump_group(cls,file,group):
    #     with open(file, 'w') as f:
    #         stud_lst = []
    #         for i in group.students:
    #             stud_lst.append([i.name, i.marks])
    #         tmp = {"Student": stud_lst}
    #         json.dump(tmp["Students"], f, indent=2)

    # @classmethod
    # def upload_group(cls, file):
    #     with open(file, 'r')as f:



st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])
sts = [st1, st2]
my_group = Group(sts, "ГК Python")
# my_group = Group(sts)
print(my_group)
my_group.add_student(st3)
print(my_group)
my_group.remove_student(1)
print(my_group)

group22 = [st2]
my_group2 = Group(group22, "ГК Web")
print(my_group2)
Group.change_group(my_group, my_group2, 0)
print(my_group)
print(my_group2)

Student.dump_to_json(st1, 'student.json')
Student.dump_to_json(st2, 'student.json')

Student.load_form_file('student.json')
my_group.dumo_group('group.json', my_group)

Group.dump_group('group.json', my_group2)
