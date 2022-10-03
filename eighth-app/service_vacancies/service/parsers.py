import requests
from bs4 import BeautifulSoup
from random import randint

__all__ = ('hh', 'superjob')

# url = "https://hh.ru/search/vacancy?text=python&from=suggest_post&area=1"
url = "https://russia.superjob.ru/vacancy/search/?keywords=Python"

# resp = requests.get(url)
# h = open("work.html", "w", encoding='utf-8')
# h.write(str(resp.text))
# h.close()
# url = "https://russia.superjob.ru/vacancy/search/?keywords=Python"

#
headers = [{
    'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84 (Edition Campaign 34)',
    'Accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    },
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.71',
        'Accept': '*/*'
    },
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    },

]


def hh(url):
    resp = requests.get(url, headers=headers[randint(0, 2)])
    jobs = []
    errors = []
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, 'html.parser')
        main_div = soup.find("div", class_="vacancy-serp-content")
        if main_div:
            div_lst = main_div.find_all("div", class_="serp-item")
            for div in div_lst:
                title = div.find('h3').text
                # print(title)
                href = div.find("h3").a['href']
                # print(href)
                content = div.find_all("div", class_="vacancy-serp-item__info")
                if len(content) > 1:
                    content = content[1].text
                else:
                    content = "Нет Описания"
                # print(content)
                comp = div.find("div", class_="vacancy-serp-item__meta-info-company").find("a")
                if comp:
                    company = comp.text
                else:
                    company = "Компания Не Известна"
                # print(company)
                jobs.append({'title': title, 'url': href, 'description': content, 'company': company})
        else:
            errors.append({'url': url, 'title': 'Разметка была изменена'})
    else:
        errors.append({'url': url, 'title': 'Страница Не Отвечает'})
    return jobs, errors


# if __name__ == '__main__':
#     jobs, errors = hh(url)
#     h = open("work.json", "w", encoding='utf-8')
#     h.write(str(jobs))
#     h.close()


def superjob(url):
    resp = requests.get(url, headers=headers[randint(0, 2)])
    jobs = []
    errors = []
    domain = "https://russia.superjob.ru"
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, 'html.parser')
        main_div = soup.find("div", class_="_3VMkc")
        title = None
        href = None
        content = None
        company = None
        if main_div:
            div_lst = main_div.find_all("div", class_="f-test-search-results-item")
            for div in div_lst:
                tit = div.find("div", class_="_2J-3z")
                if tit:
                    title = tit.find("a").text
                    # print(title)
                    href = tit.find("a").get("href")
                    # print(href)
                con = div.find("div", class_="_2d_Of")
                if con:
                    content = con.find("div", class_="_3gyJS").text
                    # print(content)
                # comp = div.find("span", class_="_1jb_5")
                comp = div.find("span", class_="f-test-text-vacancy-item-company-name")
                if comp:
                    company_link = comp.find("a")
                    if company_link:
                        company = company_link.text
                        # print(company)
                    else:
                        company = "Компания неизвестна"
                    # print(company)

                jobs.append({'title': title, 'url': domain + href, 'description': content, 'company': company})
        else:
            errors.append({'url': url, 'title': 'Разметка была изменена'})
    else:
        errors.append({'url': url, 'title': 'Страница Не Отвечает'})
    return jobs, errors


if __name__ == '__main__':
    jobs, errors = superjob(url)
    h = open("work.json", "w", encoding='utf-8')
    h.write(str(jobs))
    h.close()
