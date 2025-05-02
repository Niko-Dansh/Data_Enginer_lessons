def generate(day_of_the_week=0,date=18,days=7):
    day_of_the_week_list = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресение']
    for item in range(days):
        print(f'- [ ] Попрограмировать немного : {date + item}е {day_of_the_week_list[item]}')


generate(date=14)