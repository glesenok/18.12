gain =  int(input('ВВедите сумму выручки :'))
outlay = int(input('ВВедите сумму убытков :'))
if gain > outlay:
    profit = gain - outlay
    rent= profit / gain
    print('Прибыль больше убытков')
if outlay > gain:
    beat = outlay- gain
    print('Огромные убытки')

work = int(input("Cколько сотрудников фирме: "))
sum = profit // work
print ('на одного сотрудника:',(sum))
print ('конец программы')
