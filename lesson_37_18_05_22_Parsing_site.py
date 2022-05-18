### LESSON 37 ###
# from bs4 import BeautifulSoup

# f = open('index.html').read()
# soup = BeautifulSoup(f, 'html.parser')
# row = soup.find("div", class_="name").text
# row = soup.find_all("div", class_="name")
# row = soup.find_all("div", class_="row")[1].find_all('div', class_='links')
# row = soup.find_all("div", {"class": "name"})

# row = soup.find_all("div", {"dat-set": "salary"})
# row = soup.find("div", text="Alena").parent
# row = soup.find("div", text="Alena").find_parent(class_="row")
# row = soup.find("div", id="whois3")
# row = soup.find("div", id="whois3").find_next_sibling()
# row = soup.find("div", id="whois3").find_previous_sibling()
# print(row)

#
# def get_copywriter(tag):
#     whois = tag.find('div', class_="whois")
#     if "Copywriter" in whois:
#         return tag
#     return None
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

####### Гег Выражения для Поиска ###
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, 'html.parser')
# salary = soup.find_all('div', {'data-set': 'salary'})
# print(salary)
#
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, 'html.parser')
# salary = soup.find_all('div', {'data-set': 'salary'})..text
# for i in salary:
#     print(i.taxt)

# import re
# def get_salary(s):
#     pattern = r''
#     # res = re.findall(pattern, s)[8]
#     res = re.search(pattern, s).group()
#     print(res)
#
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, 'html.parser')
# salary = soup.find_all('div', {'data-set': 'salary'})
# print(salary)
# for i in salary:
#     get_salary(i.text)

import csv
import re
import requests
from bs4 import BeautifulSoup
# r = requests.get("https://ru.wordpress.org")
# print(r.status_code)
# print(r.headers['content-type'])
# print(r.content)
# r.encoding = 'utf-8??'
# print(r.text)
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
# def refined(s):
#     res = re.sub(r'\D+', '', s)
#     return res
#
# def write_csv(data):
#     with open('plugins.csv', 'a') as f:
#         writer = csv.writer(f, lineterminator='\r')
#         writer.writerow(data['name'], data['url'], data['rating'])
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')  #'html.parser')
#     # p1 = soup.find("header", id="masthead").find('p', class_="site-title").text
#     s = soup.find_all('section', class_='plugin-section')[1]
#     plugins = s.find_all('article')
#
#     for plugin in plugins:
#         name = plugins.find("h3").text
#         name = plugins.find("h3").find('a').get('href')
#         rating = plugin.find('span', class_="rating_count").find('a').text
#         # print(name)
#         r = refined(rating)
#
#         data = {'name': name, 'url': url, 'rating': r}
#         # print(rating)
#         print(r)
#     # return len(plugins)
#
# def main():
#     url = 'https://ru.wordpress.org/plugins'
#     # print(get_data(get_html(url)))
#     get_data(get_html(url))
#
# if __name__ == '__main__':
    # main()


def get_html(url):
    r = requests.get(url)
    return r.text

def refine_cy(s):
    return s.split()[-1]

def write_csv(data):
    with open('plagins1.csv', 'a') as f

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    elements = soup.find_all('article', class_="plagin-card")
    for el in elements:
        try:
            name = el.find('h3').text
        except ValueError:
            name = ''

        try:
            url = el.find('h3').find('a').get('href')
        except ValueError:
            url = ''

        try:
            snippet = el.find('div', class_='entry-excerpt').text.strip()
        except ValueError:
            snippet = ''

        try:
            active = el.find("div", class_="acctive_installs").text.strip()
        except ValueError:
            active = ''

        try:
            c = el.find('span', class_="tested-with").text.strip()
            cy = refine_cy(_cy(c))
        except ValueError:
            c = ""
            cy=''

        data = {

        }

        print(url)
    # print(len(element))

def main():
    # url = 'https://ru.wordpress.org/plugins/'
    # print(get_data(get_html(url)))
    # get_data(get_html(url))
    for i in range(1,7):
        url = 'https://ru.wordpress.org/plugins/brouse.blocks/page/{i}'
        get_page_data(get_html(url))

if __name__ == '__main__':
    main()