from service.parsers import *
import os
import sys
import django
from django.db import DatabaseError



proj = os.path.dirname(os.path.abspath(__file__))
sys.path.append(proj)
os.environ["DJANGO_SETTINGS_MODULE"] = 'service_vacancies.settings'

django.setup()

from service.models import Vacancy, City, Language, Error


parsers = (
    (hh, "https://hh.ru/search/vacancy?text=python&from=suggest_post&area=1"),
    (superjob, "https://russia.superjob.ru/vacancy/search/?keywords=Python")
)

city = City.objects.filter(slug='almetevsk').first()
language = Language.objects.filter(slug='python').first()


jobs, errors = [], []

for func, url in parsers:
    # print(func)
    # print(url)
    j, e = func(url)
    jobs += j
    errors += e

for job in jobs:
    v = Vacancy(**job, city=city, language=language)
    try:
        v.save()
    except DatabaseError:
        pass

if errors:
    er = Error(data=errors).save()

# h = open("work.json", "w", encoding='utf-8')
# h.write(str(jobs))
# h.close()

