# ### LESSON 37 ###
# from bs4 import BeautifulSoup
#
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, 'html.parser')
# row = soup.find("div", class_="name").text
# print(row)
# row = soup.find_all("div", class_="name")
# print(row)
# row = soup.find_all("div", class_="row")[1].find('div', class_='links')
# print(row)
# row = soup.find_all("div", {"class": "name"})
# print(row)
# print("#" * 49)
# print("Получение Доступа к Пользовательскому-Аттрибуту data-set Через Словарь:")
# row = soup.find_all("div", {"data-set": "salary"})
# print(row)
# print("!" * 49)
# print("Поиск Снизу-Вверх По-Тексту.")
# row = soup.find("div", text="Alena").parent
# row1 = soup.find("div", text="Kate").parent
# print(row)  # , row1)
# row = soup.find("div", text="Alena").find_parent(class_="row")
# print(row)
# print("#" * 49)
# print(f"Поиск Элементов с id='whois3' И Его Соседних DIV Снизу И Сверху")
# row1 = soup.find("div", id="whois3")
# row2 = soup.find("div", id="whois3").find_next_sibling()
# row3 = soup.find("div", id="whois3").find_previous_sibling()
# # print(f"{row1}\n{row2}\n{row3}")
# print("#" * 49)
# print("Функция Фильтрации Содержимого Сайта Copywriter")
#
#
# def get_copywriter(tag):
#     whois = tag.find('div', class_="whois")
#     if "Copywriter" in whois:
#         return tag
#     return None
#
#
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, 'html.parser')
# copywriter = []
# row = soup.find_all("div", class_="row")
# # print(row)  # All info
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
#
# print(copywriter)
# print()
#
# print("#" * 49)
# print("####### Регулярные Выражения для Поиска ### Поиск Загплаты.")
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, 'html.parser')
# salary = soup.find_all('div', {'data-set': 'salary'})
# for i in salary:
#     print(i.text)
# # print(salary)
#
# # f = open('index.html', encoding='utf-8').read()
# # soup = BeautifulSoup(f, 'html.parser')
# # salary = soup.find_all('div', {'data-set': 'salary'})
# # for i in salary:
# #     print(i.text)
#
# import re
#
#
# def get_salary(s):
#     pattern = r'[0-9]+'  # \d+
#     res = re.findall(pattern, s)[0]
#     res1 = re.search(pattern, s).group()
#     print(f"{res} {res1}")
#
#
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, 'html.parser')
# salary = soup.find_all('div', {'data-set': 'salary'})
# # print(salary)
# for i in salary:
#     get_salary(i.text)
# print()
# print("#" * 49)
# print("Получение Разметки Сьраницы. Получение Данных со Страницы.")
# import csv
# import requests
# from bs4 import BeautifulSoup
#
# r = requests.get("https://ru.wordpress.org")
# print(r)  #
# print(r.status_code)
# print(r.headers['content-type'])
# print(r.content)
# r.encoding = 'utf-8??'
# print(r.text)
# print("!" * 59)
# print("Получение HTML-Разметки Страницы. web-parsing - Получение Данных Со Страницы. По Функциям.")
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refined(s):
#     res = re.sub(r'\D+', '', s)
#     return res
#
#
# def write_csv(data):
#     with open('plugins_37.csv', 'a') as f:
#         writer = csv.writer(f, delimiter=';', lineterminator='\r')
#         writer.writerow((data['name'], data['url'], data['rating']))
#
#
# print("Метод Получения Данных С Помощью BeautifulSoup")
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')  # 'html.parser')
#     # p1 = soup.find("header", id="masthead").find('p', class_="site-title").text
#     # return p1
#     s = soup.find_all('section', class_="plugin-section")[1]
#     # return s
#     plugins = s.find_all('article')
#     print(f"Количество Плагинов На Вкладке Рекомендуемые: {len(plugins)}")
#     # return len(plugins)
#
#     for plugin in plugins:
#         name = plugin.find("h3").text
#         # print("Сохранение Ссылки На Плагин:")
#         url = plugin.find('h3').find('a').get('href')
#         # print(name)
#         # print(url)
#         # print("Находим Текст Рейтинга")
#         rating = plugin.find('span', class_="rating-count").find('a').text
#         r = refined(rating)
#         # print(r)
#         data = {'name': name, 'url': url, 'rating': r}
#         # print(data)
#         write_csv(data)
#
#
# #         print(r)
# #     # return len(plugins)
#
# def main():
#     # url = 'https://ru.wordpress.org/plugins'
#     url = 'https://ru.wordpress.org/plugins'
#     # print(f"Получение HTML-Разметки: {get_html(url)}")
#     # print(get_data(get_html(url)))
#     get_data(get_html(url))
#
#
# #     get_data(get_html(url))
#
# if __name__ == '__main__':
#     main()
#
# print("!" * 59)
# print("#" * 49)
# print()
print("HTML-парсинг Сайта Из Множества Элементов.")
import  csv
import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def refine_cy(s):
    return s.split()[-1]  # ['Протестирован', 'с', '5.9.3']


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')  # 'html.parser')

    elements = soup.find_all('article', class_="plugin-card")
    # print(len(elements))

    def write_csv(data):
        with open('plagins1_37.csv', 'a') as f:
            writer = csv.writer(f, delimiter=';', lineterminator='\r')
            writer.writerow((data['name'],
                             data['url'],
                             data['snippet'],
                             data['active'],
                             data['cy']))


    for el in elements:
        try:
            name = el.find('h3').text
        except ValueError:
            name = ''
        # print(name)
        try:
            url = el.find('h3').find('a').get('href')
        except ValueError:
            url = ''
        # print(url)
        try:
            snippet = el.find('div', class_='entry-excerpt').text.strip()
        except ValueError:
            snippet = ''
        # print(snippet)
        try:
            active = el.find("span", class_="active-installs").text.strip()
        except ValueError:
            active = ''
        # print(active)
        try:
            c = el.find('span', class_="tested-with").text.strip()
            cy = refine_cy(c)
        except ValueError:
            # c = ""
            cy = ''
        print(cy)


        data = {
            'name': name,
            'url': url,
            'snippet': snippet,
            'active': active,
            'cy': cy
        }

        write_csv(data)



#
#         print(url)
#     # print(len(element))
#
def main():
    url = 'https://ru.wordpress.org/plugins/browse/blocks'
    get_page_data(get_html(url))


#     # get_data(get_html(url))
#     for i in range(1,7):
#         url = 'https://ru.wordpress.org/plugins/brouse.blocks/page/{i}'
#         get_page_data(get_html(url))
#
if __name__ == '__main__':
    main()
