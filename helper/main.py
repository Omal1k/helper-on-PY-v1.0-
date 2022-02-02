#Модули------------------------

import requests
from bs4 import BeautifulSoup
from math import sqrt
import random
from pyowm import OWM
from colorama import init
from colorama import Fore, Back, Style
init()
#------------------------------
#Масивы------------------------
First_answers = ['Да', 'Yes', 'yes', 'да']

#------------------------------------------
#Функции
""" def parse():
    URL = 'https://site.ua/news/?utm_source=ggl_news_1005&utm_medium=cpc&utm_campaign=search_news_site&utm_content=about_news_root&utm_term=news_site_ukraine2&gclid=CjwKCAjwqcKFBhAhEiwAfEr7zWFEzGfgnAOWtp82jbeCMlbsJ2s-_-Ttugq4hFHWefQPNSNmkMShCxoCMusQAvD_BwE'
    HEADDERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 OPR/75.0.3969.279' 

    }

    response = requests.get(URL, headers= HEADDERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_ = 'padding-vertical-15')
    comps = []
    for item in items:
        comps.append({
            'title': item.find('a', class_ = 'widget-post-title').text(strip = True)

        })

        for comp in comps:
            print(comp['title'])   """
def game(): 
    print('Привет, сыграем в игру?')
    a = ['+', '-', '/', '*']
    qe = input('Ну что, начнём?')
    while qe != 'q' or 'ні':
        b = random.choice(a)
        c = random.randint(1, 10)
        d = random.randint(1, 10)
        if b == '+':
            e = c + d 
            print('Сколько будет: ' + str(c) + ' + ' + str(d) + ' =')
            q = float(input('Сколько будет? '))
            if q == e:
                print('Молодец, правильный ответ :-)')
            else:
                print('Неправильно :-(')

        elif b == '-':
            e = c - d 
            print('Сколько будет: ' + str(c) + ' - ' + str(d) + ' =')
            q = float(input('Сколько будет? '))
            if q == e:
                print('Молодец, правильный ответ :-)')
            else:
                print('Неправильно :-(')


        elif b == '/':
            e = c / d
            h = c % d
            if  h == 0:
                print('Сколько будет: ' + str(c) + ' / ' + str(d) + ' =')
                q = float(input('Сколько будет? '))
                if q == e:
                    print('Молодец, правильный ответ :-)')
                else:
                    print('Неправильно :-(')
            
   
        elif b == '*':
            e = c * d 
            print('Сколько будет: ' + str(c) + ' * ' + str(d) + ' =')
            q = float(input('Сколько будет? '))
            if q == e:
                print('Молодец, правильный ответ :-)')
            else:
                print('Неправильно :-(')
        qe = input('не желаешь закончить-q?')
    print('Ну ладно...\nКак хочешь, пока :-(')


def calculator(): 
    from math import sqrt
    print('Я умный калькулятор от данного автора: @.Omal1k`\n Я умею много чего длеать, снизу я приведу список.\nприбавить: +,\nотнять: -,\nразделить: /,\nнайти процент от числа: %,\nКвадратный корень: sqrt,\nУмножение: *,\nСтепень: ^\nВыйти: q')
    what = input('Что будем делать?')
    while what != 'q':
        if what == '+':
            a = float(input("Выбирите первое значение: " ))
            b = float(input("Выбирите второе значение: " ))
            c = a + b
            print(c)
            what = input('Что теперь?')
        elif what == '-':
            a = float(input("Выбирите первое значение: " ))
            b = float(input("Выбирите второе значение: " ))
            c = a - b 
            print(c)
            what = input('Что теперь?')
        elif what == '/':
            a = float(input("Выбирите первое значение: " ))
            b = float(input("Выбирите второе значение: " ))
            
            try: 
                a / b
                print(a / b)
            except ZeroDivisionError:
                print('Делить на ноль нельзя')
            what = input('Что теперь?')
            what = input('Что будем делать?')
        elif what == '/':
            a = float(input("Выбирите число с которого нужно найти процент: "))
            b = float(input("Укажите процент: "))
            c = (a * b) / 100 
            print(c)
            what = input('Что теперь?')
        elif what == 'sqrt':
            a = float(input("ВЫбирите число с которого вам нужно найти корень: "))
            c = sqrt(a)
            print(c)
            what = input('Что теперь?')
        elif what == '*':
            a = float(input("Выбирите первое значение: "))
            b = float(input("Выбирите второе значение: "))
            c = a * b
            print(c)
            what = input('Что теперь?')
        elif what == '^':
            a = float(input("Выбирите значени которое нужно подвести в степень:" ))
            b = float(input("Выбирите степень: "))
            c = a ** b
            print(c)
            what = input('Что теперь?')
        elif what == 'q':
            break
        else:
            print('Такой операции несуществует!')
            what = input('Что теперь?')
def weather():
    city = input('ВВедите название города: \n q-выход. ')
    while city != 'q':
        owm = OWM('82b2becf29f6456dd032586a448fcfa6')
        city = input('ВВедите название города: \n q-выход. ')
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(city)
        w = observation.weather
        t = w.temperature('celsius')
        t1 = t['temp']
        t2 = t['feels_like']
        t3 = t['temp_max']
        t4 = t['temp_min']
        print(f'В городе {city} температура {t1}, очущается как {t2}, макс. температура сегодня: {t3}, мин. температура в день: {t4}') 



def sec():
    '''Секундомер'''
    from time import time
    print('Нажмите клавишу Enter, чтобы начать. После этого нажмите клавишу Enter, чтобы "нажать" на секундомер. Нажмите комбинацию клавиш Ctrl-C для останова секундомера и выхода из программы.')
    input()
    print('Начали.')
    startTime = time.time() 
    lastTime = startTime
    lapNum = 1

    
    try:
        while True:
            input()
            lapTime = round(time.time() - lastTime, 2)
            totalTime = round(time.time() - startTime, 2)
            print('Круг #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
            lapNum += 1
            lastTime = time.time() 
    except KeyboardInterrupt:
        
        print('\nГотово.')

#------------------------------------------
print(Back.RED)
print(Fore.CYAN)
print('Привет. Я умею много чего багато, снизу список:')
print('------------------------------------------------------------------------------------------------\nФормат: [Название виджета - команда для вызова]\n------------------------------------------------------------------------------------------------\nНовости-news\nСекундомер-time\nПогода-weather\nКалькулятор-calculator\n рандомные_числа_игра-1st_game\n------------------------------------------------------------------------------------------------')
Genereal_ques = input('Что будем делать?')
while Genereal_ques != 'q':
    if Genereal_ques == 'time':
        sec()
        Genereal_ques = input('Чё теперь?')
    elif Genereal_ques == 'q':
        quit
    elif Genereal_ques == '1st_game':
        game()
        Genereal_ques = input('Чё теперь?')
    elif Genereal_ques == 'calculator':
        calculator()
        Genereal_ques = input('Чё теперь?')
    elif Genereal_ques == 'weather':
        weather()
    else:
        print('Такой функции не СУЩЕСТВУЕТ!')
        Genereal_ques = input('Чё теперь?')

print('пока!')








