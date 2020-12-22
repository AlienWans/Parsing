from pymongo import mongo_client
from ScrapingJob import ScrapingJob
from pprint import pprint

vacancy_db = ScrapingJob('mongodb://172.17.0.2:27017/', 'vacancy', 'vacancy_db')
vacancy_db.print_salary(300_000)

#{'_id': ObjectId('5d89d0fb97faf8415e0e9914'),
# 'city': 'Москва',
# 'company_name': ' DataFork ',
# 'metro_station': 'Площадь Революции',
# 'salary_currency': 'RUB',
# 'salary_max': 400000,
# 'salary_min': 300000,
# 'site': 'hh.ru',
# 'vacancy_link': 'https://hh.ru/vacancy/33498645',
# 'vacancy_name': 'Data Engineering Team Lead (Python / C++)'}
#{'_id': ObjectId('5d89d0fb97faf8415e0e9918'),
# 'city': 'Санкт-Петербург',
# 'company_name': ' Cindicator ',
# 'metro_station': 'Гостиный двор',
# 'salary_currency': 'RUB',
# 'salary_max': 400000,
# 'salary_min': None,
# 'site': 'hh.ru',
# 'vacancy_link': 'https://hh.ru/vacancy/31182158',
# 'vacancy_name': 'Python разработчик / Python software developer'}
#{'_id': ObjectId('5d89d0fb97faf8415e0e9923'),
# 'city': 'Москва',
# 'company_name': ' Cindicator ',
# 'metro_station': None,
# 'salary_currency': 'RUB',
# 'salary_max': 400000,
# 'salary_min': None,
# 'site': 'hh.ru',
# 'vacancy_link': 'https://hh.ru/vacancy/33416348',
# 'vacancy_name': 'Python разработчик / Python software developer'}
#{'_id': ObjectId('5d89d1830f1be7fa56ae7114'),
# 'city': 'Нур-Султан',
# 'company_name': 'ТОО Helios Soft ',
# 'metro_station': None,
# 'salary_currency': 'KZT',
# 'salary_max': 800000,
# 'salary_min': 300000,
# 'site': 'hh.ru',
# 'vacancy_link': 'https://hh.ru/vacancy/33553701',
# 'vacancy_name': 'Программист Python'}

#1* Написать функцию, которая будет добавлять в вашу базу данных только новые вакансии с сайта

vacancy_db.collection.update_one({'vacancy_link': 'https://hh.ru/vacancy/31828023'},
                                 {'$set': {'city':'Москва', 'company_name':'some compary'}})

#<pymongo.results.UpdateResult at 0x7f21bb0ae910>

objects = vacancy_db.collection.find().limit(1)
for obj in objects:
    pprint(obj)

#{'_id': ObjectId('5d89d0fa97faf8415e0e98e5'),
# 'city': 'Москва',
# 'company_name': 'some compary',
# 'metro_station': 'Чернышевская',
# 'salary_currency': None,
# 'salary_max': None,
# 'salary_min': None,
# 'site': 'hh.ru',
# 'vacancy_link': 'https://hh.ru/vacancy/31828023',
# 'vacancy_name': 'Программист Python / C++'}

vacancy = 'Python'
vacancy_db.search_job(vacancy)
objects = vacancy_db.collection.find().limit(1)
for obj in objects:
    pprint(obj)

#{'_id': ObjectId('5d89d0fa97faf8415e0e98e5'),
# 'city': 'Москва',
# 'company_name': 'some compary',
# 'metro_station': 'Чернышевская',
# 'salary_currency': None,
# 'salary_max': None,
# 'salary_min': None,
# 'site': 'hh.ru',
# 'vacancy_link': 'https://hh.ru/vacancy/31828023',
# 'vacancy_name': 'Программист Python / C++'}