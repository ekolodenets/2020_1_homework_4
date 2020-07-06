'''
Инженерный калькулятор
Напишите программу - инженерный калькулятор. После запуска программа открывает интерактивную оболочку, в которую можно вводить комманды:

user@machine:~$ python calc.py
Advanced calculator. Author: [Student Name], Version: 1.0.0
~ ...
Базовые требования
Программа воспринимает введённые пользователем математические выражения и правильно их интепретирует:
~ 5 + 4
9
~ 10 - 3 + 1
8
~ 2 ** 3 - 1
7
Программа знает о приоритете операторов
~ 2 + 3 * 4
14
~ 8 / 2 * 3
12
Программа поддерживает изменение приоритета при помощи скобок
~ 3 * (2 + 1)
9
~ 5 + (2 - 2 * (3 + 7))
-13
Использование eval, exec, compile запрещено.
Дополнительные баллы (каждый подпункт - 1 балл)
Программа воспринимает основные математические функции и константы:
~ sqrt(3) + ln(e) - pi
-0.4095418460209159
Программа поддерживает переменные
~ x = 5
~ x
5
~ x + 3
8
Программа поддерживает оператор ' для взятия производной простейших функций
~ x = 2
~ (x ** 3)'
12
~ sin(2 * x)'
-0.8322936730942848
Программа поддерживает объявление функций
~ f(x) = x ** 2 + tg(x)'
~ f(5)
37.427881707458354

'''

import re
class MyClass:
    print('код я взял -> https://habr.com/ru/post/273253/')
    def advanced_calc(self, expression):

        '''
        Here we write all the logic and return result

        :return:
        '''
        # def sum(self, *args):
        #     l1 = []
        #     l2 = []
        #     si = inp.index('+')
        #     num = int(inp[si-1])+int(inp[si+1])
        #     l1 = inp[0:si-1]
        #     l1.append(num)
        #     l2 = inp[si+2::]
        #     l1 = l1+l2
        #     return l1
        #
        # def minus(self, *args):
        #     l1 = []
        #     l2 = []
        #     si = inp.index('-')
        #     num = int(inp[si - 1]) - int(inp[si + 1])
        #     l1 = inp[0:si - 1]
        #     l1.append(num)
        #     l2 = inp[si + 2::]
        #     l1 = l1 + l2
        #     return l1
        #
        # def mult(self, *args):
        #     l1 = []
        #     l2 = []
        #     si = inp.index('*')
        #     num = int(inp[si - 1]) * int(inp[si + 1])
        #     l1 = inp[0:si - 1]
        #     l1.append(num)
        #     l2 = inp[si + 2::]
        #     l1 = l1 + l2
        #     return l1
        #
        # def div(self, *args):
        #     l1 = []
        #     l2 = []
        #     si = inp.index('/')
        #     num = int(inp[si - 1]) / int(inp[si + 1])
        #     l1 = inp[0:si - 1]
        #     l1.append(int(num))
        #     l2 = inp[si + 2::]
        #     l1 = l1 + l2
        #     return l1
        #
        # inp = []
        # if 'pi' in var: x = var.replace('pi', '3.14159265359')
        #
        # if "(" in var:  # проверяем на наличие скобок
        #     print("есть скобки")
        # else:
        #     print("нет скобок")
        #     for x in re.split(r'\s+', var):
        #         inp.append(x)
        #     print(inp)
        #
        #     while len(inp) > 2:
        #
        #         if '*' in inp:
        #             new = mult(inp)
        #             print(new)
        #         elif '/' in inp:
        #             new = div(inp)
        #             print(new)
        #         elif '+' in inp:
        #             new = sum(inp)
        #             print(new)
        #         elif '-' in inp:
        #             new = minus(inp)
        #             print(new)
        #         inp = new
        #         for i in inp:
        #             result = i    # мой ломаный код

        OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
                     '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y)}


        def parse(expression):
            number = ''
            for s in expression:
                if s in '1234567890.':
                    number += s
                elif number:
                    yield float(number)
                    number = ''
                if s in OPERATORS or s in "()":
                    yield s
            if number:
                yield float(number)

        def shunting_yard(parsed_formula):
            stack = []
            for token in parsed_formula:
                if token in OPERATORS:
                    while stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
                        yield stack.pop()
                    stack.append(token)
                elif token == ")":
                    while stack:
                        x = stack.pop()
                        if x == "(":
                            break
                        yield x
                elif token == "(":
                    stack.append(token)
                else:
                    yield token
            while stack:
                yield stack.pop()

        def calc(polish):
            stack = []
            for token in polish:
                if token in OPERATORS:
                    y, x = stack.pop(), stack.pop()
                    stack.append(OPERATORS[token][1](x, y))
                else:
                    stack.append(token)
            return stack[0]

        return calc(shunting_yard(parse(expression)))

        return result  # here we return result


if __name__ == '__main__':
    # Here we can make console input and check how function works

    var = input('Input Expression: ')

    result = MyClass().advanced_calc(var)

    print(result)
