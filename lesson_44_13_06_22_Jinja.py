### from LESSON 43 ### jinja Begin
### FILTER
from jinja2 import Template

# {{ }} - Выражение для вставки конструкции Python в Шаблон.
# {% %} - Спецификатор Щаблона.
# ## - Строчный комментарий.


# name = "Игорь"
# age = 28
#
# tm = Template("Мне {{ a*2 }} лет. Меня зовут {{ n.upper() }}")
# msg = tm.render(n=name, a=age)
# print(msg)
#
# per = {'name': "Игорь", 'age':28}
# tm = Template("Мне {{ p['age'] }} лет. Меня зовут {{ p.name }}")
# msg = tm.render(p=per)
# print(msg)
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#
# # per = {'name': "Игорь", 'age': 28}
# per = Person("Игорь", 28)
# # tm = Template("Мне {{ p['age'] }} лет. Меня зовут {{ p.name }}")
# tm = Template("Мне {{ p.get_age() }} лет. Меня зовут {{ p.get_name() }}")
# msg = tm.render(p=per)
# print(msg)


# data = "{% raw %}Строка, с названием {{ name }}. Со значением {% endraw %}"
#
# tm = Template(data)
# msg = tm.render(name="Игорь")
# print(msg)

# link = "<a href='#'>Ссылка</a>"
#
# tm = Template("{{ link | e }}")
# msg = tm.render(link=link)
#
# print(msg)


### LESSON 44 13.06.2022 ###
# JINJA
# {% raw %} {% endraw %}
from jinja2 import Template

cities = [
    {'id': 1, 'city': 'Москва'},
    {'id': 2, 'city': 'Смоленск'},
    {'id': 3, 'city': 'Минск'},
    {'id': 4, 'city': 'Сочи'},
    {'id': 5, 'city': 'Ярославль'},
]

link = """<select name="cities">
    {% for c in cities -%}
    {% if c.id > 3 -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
    {% elif c.city == "Москва" -%}
        <option>{{ c['city'] }}</option>
    {% else -%}
        {{ c['city'] }}
    {% endif -%}
    {% endfor -%}
</select>"""

tm = Template(link)
msg = tm.render(cities=cities)

print(msg)

# # {% if <condition> %}
# #   <cod>
# # {% else %}
# #   <cod>
# # {% endif %}
print("### Tern 1 lesson 44 ###")
punkts = [
    {'href': 'index', 'title': 'Главная'},
    {'href': 'newst', 'title': 'Новости'},
    {'href': 'about', 'title': 'О коипании'},
    {'href': 'shop', 'title': 'Магазин'},
    {'href': 'contacts', 'ttle': 'Контакты'}
]
d = "class = 'active'"
link = """
    <ul>
    {% for c in punkts -%}
    {% if c.href=="index" -%}
        <li><a href="/{{ c['href'] }} {{ d }}>{{ c['title'] }}</a></li>
    {% else -%}
        <li><a href="/{{ c.href }} {{ c.title }} </a></li>
    {% endif -%}
    {% endfor -%}
    </ul>
"""

tm = Template(link)
msg = tm.render(punkts=punkts, d=d)
print(msg)

# data=[
#     {'href': 'index', 'title':'Главная'},
# {'href': 'news', 'title':'Новости'},
# {'href': 'about', 'title':'О компании'},
# {'href': 'shop', 'title':'Магазин'},
# {'href': 'contacts', 'title':'Контакты'},
# ]
#
# d="class = 'active'"
# link="""
# <ul>
# {% for di in data%}
# {% if di.href=="index"%}
#     <li><a href="/{{di.href}} {{d}}>{{di.title}}</a></li>
# {% else%}
#     <li><a href="/{{di.href}}>{{di.title}}</a></li>
# {%endif%}
# {%endfor%}
# </ul>
# """
# tm = Template(link)
# msg = tm.render(data=data)
# print(msg)

print("### SUMMA Of LIST ###")
lst = [1, 2, 3, 4, 5, 6]
tpl = "Summa: {{cs | sum}}"
tm = Template(tpl)
msg = tm.render(cs=lst)
print(msg)

print("### SUMMAOf DICTIONARY")
cars = [
    {'model': 'Audi', 'price': 23000},
    {'model': 'Skoda', 'price': 17300},
    {'model': 'Renault', 'price': 44300},
    {'model': 'Wlksvagen', 'price': 21300},
]

# tpl = "Summa: {{ cs | sum(attribute='price') }}"
# tpl = "Summa: {{ (cs | max(attribute='price')).model }}"
# tpl = "Summa: {{ cs | random }}"
tpl = "Summa: {{ cs | replace('model', 'brand') }}"
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)
print("######Использование Фильтра##########")
person = [
    {'name': "Алексей", 'yer': 18, 'weight': 78.5},
    {'name': "Никита", 'yer': 28, 'weight': 82.3},
    {'name': "Виталий", 'yer': 33, 'weight': 94.0}

]
tpl = """
{%- for u in users -%}
{% filter upper %} {{ u.name }} - {{ u.weight }} {% endfilter %}
{% filter string %} {{ u.name }} - {{ u.weight }} {% endfilter %}
{% endfor %}
"""
#
tm = Template(tpl)
msg = tm.render(users=person)
print(msg)

print("##### Макроопределения #####"
      "\nПодстановка определенных значений")
html = '''
{% macro input(name, value='', type='text', size='20') -%}
    <input type='{{ type }}' name='{{ name }}' value='{{ value }}' size='{{ size }}'>
{%- endmacro -%}
<p>{{ input('username') }}</p>
<p>{{ input('email', type='email') }}</p>
<p>{{ input('password') }}</p>
'''

tm = Template(html)
msg = tm.render()
print(msg)

### kod Enter HTML
# {% macro input(name, value='', type='text', size='20') -%}
#     <input type='{{ type }}' name='{{ name }}' value='{{ value }}' size='{{ size }}'>
# {%- endmacro %}
# <p>{{ input('username') }}</p>
# <p>{{ input('email', type='email') }}</p>
# <p>{{ input('password') }}</p>


print("## Term 2##"
      "\n Macro Determinition For Pattern Field Of Input")
html = '''
{%- macro input(placeholder, name, type='text') -%}
    <input type='{{ type }}' name='{{ name }}' placeholder='{{ placeholder }}'>
{%- endmacro -%}
<p>{{ input(name='firstname', placeholder='Имя') }}</p>
<p>{{ input(name="lastname", placeholder="Фамилия") }}</p>
<p>{{ input(name="address", placeholder="Адрес") }}</p>
<p>{{ input(type="tel", name="phone", placeholder="Телефон") }}</p>
<p>{{ input(type="email", name="email", placeholder="Почта") }}</p>
'''

tm = Template(html)
msg = tm.render()
print(msg)

# html = '''
#     {% macro input(name, placeholder, type='text') -%}
#         <input type='{{ type }}' name='{{ name }}' placeholder=''>
#     {%- endmacro %}
#     <p>{{ input(name='firstname', placeholder='Имя') }}</p>
#     <p>{{ input(name='lastname', placeholder='Фамилия') }}</p>
#     <p>{{ input(name='address', placeholder='Адрес') }}</p>
#     <p>{{ input(type='tel', name='phone', placeholder='Телефон') }}</p>
#     <p>{{ input(type='email', name='email', placeholder='Почта') }}</p>
# '''

print("МАКРОС Для Вложенных Элементов")
person = [
    {'name': "Aleksey", 'year': 18, 'weight': 78.5},
    {'name': "Nikita", 'year': 28, 'weight': 82.3},
    {'name': "Vita", 'year': 33, 'weight': 94.0}
]
html = """
{% macro list_users(list_of_user) -%}
<ul>
{% for u in list_of_user -%}
    <li>{{ u.name }} {{ caller(u) }}</li>
{% endfor -%}
</ul>
{% endmacro -%}

{% call(user) list_users(users) %}
    <ul>
        <li>{{ user.year }}</li>
        <li>{{ user.weight }}</li>
    </ul>
{% endcall %}
"""
tm = Template(html)
msg = tm.render(users=person)
print(msg)
### COPY
# person = [
#     {'name': "Алексей", 'year': 18, 'weight': 78.5},
#     {'name': "Никита", 'year': 28, 'weight': 82.3},
#     {'name': "Виталий", 'year': 33, 'weight': 94.0}
# ]
#
# html = """
# {% macro list_users(list_of_user) -%}
# <ul>
# {% for u in list_of_user -%}
#     <li>{{ u.name }} {{ caller(u) }}</li>
# {% endfor %}
# </ul>
# {% endmacro %}
# {% call(user) list_users(users) %}
#      <ul>
#         <li>{{ user.year }}</li>
#         <li>{{ user.weight }}</li>
#     </ul>
# {% endcall %}
# """
#
# tm = Template(html)
# msg = tm.render(users=person)
# print(msg)


# from jinja2 import Template, Environment,FileSystemLoader
# person = [
#     {'name': "Алексей", 'year': 18, 'weight': 78.5},
#     {'name': "Никита", 'year': 28, 'weight': 82.3},
#     {'name': "Виталий", 'year': 33, 'weight': 94.0}
# ]
# file_loader =FileSystemLoader('templates_44')
# env = Environment(loader=file_loader)
# tm = env.get_template('index.html')
# # msg = tm.render(users=person)
# msg = tm.render(title="About Jinja")
# print(msg)
