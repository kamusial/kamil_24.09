number1 = float(input('Podaj liczbe 1:  '))
number2 = float(input('Podaj liczbe 2:  '))

try:
    result = number1 / number2
    print(f'WYnik dzielenia to: {result}')
except ZeroDivisionError:
    result = 0
    print('Dzielenie sie nie powiodło, result = 0')

print('dalsza częsć programu')


def test1():
    assert fizzbuzz(3) == 'fizz'


