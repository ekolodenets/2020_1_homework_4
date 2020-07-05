'''
Декоратор типов
Напишите декоратор, который проверял бы тип параметров функции следующим образом: При вызове без аргументов осуществлял
бы конвертацию параметров и возвращаемого значения в указанные типы:

@typed
def add(a: int, b: int) -> str:
    return a + b

add("3", 5) -> "8"
add(2.35, True) -> "3"
При вызове с параметром strict=True выбрасывал бы исключение при неправильной передаче параметров:

@typed(strict=True)
def convert_upper(msg: str) -> str:
    return msg.upper()

convert_upper('abc') -> 'ABC'
convert_upper(5) -> TypeError('`convert_upper` argument `msg` required to be a `str` instance')
Если типы параметров функции не указаны декоратор должен предполагать их тип как Any:

@typed
def acc(a, b, c):
    return a + b + c

acc('a', 'b', 'c') -> 'abc'
acc(5, 6, 7) -> 18
acc(0.1, 0.2, 0.4) -> 0.7000000000000001
'''


class MyClass:

    # def typed(n):
    #     def sub(f):
    #         def wrapper(self, *args):
    #             lst = []
    #             lst2 = []
    #             for i in args:
    #                 if i is int(i) or i is float(i):
    #                     lst.append(i)
    #                     if len(args) == len(lst):
    #                         a = sum(args)
    #                 else:
    #                     for i in args:
    #                         lst2.append(str(i))
    #                     a = ''.join(lst2)
    #             if n == True and msg == int(msg):
    #                 msg = "TypeError('`convert_upper` argument `msg` required to be a `str` instance')"
    #             else:
    #                 msg = args.upper()
    #             return a, msg
    #         return wrapper
    #     return sub

    def typed(f):
        def wrapper(self, *args):
            st = ''
            n = 0
            for i in args:
                st += str(i)
            if st.isdigit():
                for i in args:
                    n += i
                a = n
            else:
                try:
                    for i in args:
                        i == float(i)
                except:
                    a = st
                else:
                    for i in args:
                        n += float(i)
                        a = n
            return a
        return wrapper

    @typed
    def add(self, a: int, b: int) -> str:
        return a + b
    #
    # @typed(strict=True)
    # def convert_upper(self, msg: str) -> str:
    #     return msg.upper()
    #
    @typed
    def acc(self, a, b, c):
        return a + b + c

if __name__ == '__main__':

    # Here we can make console input and check how function works
    #
    a = 'b'
    b = 0

    result = MyClass().add(a, b)
    print(result)

    # msg = "abs"
    # result = MyClass().convert_upper(msg)
    # print(result)

    a =3
    b ='y'
    c =5
    result = MyClass().acc(a, b, c)
    print(result)