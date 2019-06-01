from calculator.model import Calculator

if __name__ == '__main__':
    a = int(input('첫번째수'))
    b = int(input('두번째 수'))

    calc = Calculator(a, b)
    print('{} + {} = {}'.format(a,b,  calc.sum()))






