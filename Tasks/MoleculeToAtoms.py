'''
Из молекулы в атомы
Напишите функцию, которая, принимая как параметр строку - формулу молекулы, возвращала бы атомы из этой молекулы и их количество в виде Dict[str, int]:

def parse_molecule(molecule: str) -> dict:
    pass
Примеры:¶
H2O -> {H: 2, O: 1}
Mg(OH)2 -> {Mg: 1, O: 2, H: 2}
K4[ON(SO3)2]2 -> {K: 4, O: 14, N: 2, S: 4}
Замечания:
Скобки в формулах могут быть круглыми, квадратными и фигурными. Такжи они могут быть вложены друг в друга.
Индекс после скобки означает количество раз, которое повторяется каждый атом внутри скобок.
Индекс после скобки необязателен. Если его нет, значит содержимое скобок повторяется 1 раз.
'''


class MyClass:

    def parse(self, var: str) -> dict:
        import re
        # result = {}
        dict = {}

        def simple_cutter(lst):
            while len(lst) > 1:
                if lst[0] in dict:  # если есть в словаре значение
                    try:
                        int(lst[1]) / int(lst[1])  # проверяем 2ое значение в списке или может делиться
                    except:
                        lst.insert(1, 1)  # если не может, добавляем 1 вторым значением
                        dict[lst[0]] = int(dict[lst[0]]) + int(lst[1])  # обновляем значение в словаре добавляя второе число
                        lst = lst[2:]  # удаляем два первых значеиня в списке
                    else:
                        try:
                            int(lst[2]) / int(lst[2])  # если может делиться второе, то проверям 3ее
                        except:
                            dict[lst[0]] = int(dict[lst[0]]) + int(lst[1])  # если не может, обновляем значение в словаре добавляя второе число
                            lst = lst[2:]  # удаляем два первых значеиня в списке
                        else:
                            dict[lst[0]] = int(dict[lst[0]]) + int(lst[1] + lst[2])  # если может, обновляем значение в словаре добавляя склейку 2го и 3го числа
                            lst = lst[3:]  # удаляем три первых значеиня в списке
                try:
                    int(lst[1]) / int(lst[1])
                except:
                    lst.insert(1, 1)
                    dict[lst[0]] = int(lst[1])
                    lst = lst[2:]
                else:
                    try:
                        int(lst[2]) / int(lst[2])
                    except:
                        dict[lst[0]] = int(lst[1])
                        lst = lst[2:]
                    else:
                        dict[lst[0]] = int(lst[1] + lst[2])
                        lst = lst[3:]

            return dict

        def complex_cutter(string, modifier):   # резак сложной формулы

            while len(string) >= 1:

                if string[0] in dict:
                    try:
                        dict[string[0]] = int(dict[string[0]]) + int(string[1])
                        string = string[2:]
                    except:
                        string.insert(1, 1)
                else:
                    try:
                        int(string[1]) / int(string[1])
                    except:
                        string.insert(1, 1)
                    finally:
                        dict[string[0]] = string[1]
                        string = string[2:]
            lst = []
            for key, value in dict.items():
                dict[key] = int(dict[key])
                dict[key] = dict[key]*modifier
            for k, v in dict.items():
                lst.append(str(k)+str(v))
            string = ''.join(lst)

            return string

        def order(var):

            square = var[var.find("["):var.find("]") + 1]   # находим длинну вложеных скобок
            circ = var[var.find("("):var.find(")") + 1]
            figure = var[var.find("{"):var.find("}") + 1]
            z = []
            if len(square) != 0:
                z.append(square)
            if len(circ) != 0:
                z.append(circ)
            if len(figure) != 0:
                z.append(figure)
            return z

        def undress(x, var):
            for i in x:
                if len(i) > 3 and "(" in i or "[" in i or "{" in i:
                    string = i
                    replacer = string
                    modifier = i[-1]
                    break
            string = string[1:-2]
            string = re.findall(r'[A-Z 0-9][^A-Z0-9)]*', string)
            replacement = complex_cutter(string, int(modifier))
            var = var.replace(replacer, replacement)
            return var

        if "{" in var or "(" in var or "[" in var:  # если есть скобки в формуле
            print("Complex formula")
            order(var)  # отправляем ее на определение порядка раскрытия скобок
            y = order(var)
            while True:
                if len(y) > 0:  # пока списо очереди не пуст
                    if '(' in min(y):   # если есть круглые скобки в формуле
                        x = re.findall(r'[(0-9A-Z]?[^(\[\]{}]*', var)  # () разбиваем формулу на скобки с множетилем

                        lst = []
                        for i in x:
                            if "(" in i:
                                lst.append(i)   # если в формуле есть скобка, по типу "(Sn2)2" - добавляем ее с список
                                x.remove(i) # удаляем ее из формулы
                                break
                        string = ''.join(lst)   # создаем строку со скобкой
                        lst = list(string[0:string.find(")") + 2])  #
                        lst = ''.join(lst)
                        x.insert(0, lst)

                        var = undress(x, var)
                        y.remove(min(y))
                        order(var)
                        y = order(var)
                        dict = {}

                    elif '[' in min(y): # если есть квадратные скобки в формуле
                        x = re.findall(r'[\[0-9A-Z]?[^()\[{}]*', var)  # []

                        lst = []
                        for i in x:
                            if "[" in i:
                                lst.append(i)
                                x.remove(i)
                        string = ''.join(lst)
                        lst = list(string[0:string.find("]") + 2])
                        lst = ''.join(lst)
                        x.insert(0, lst)

                        var = undress(x, var)
                        y.remove(min(y))
                        order(var)
                        y = order(var)
                        dict = {}

                    elif '{' in min(y): # если есть фигурные скобки в формуле
                        x = re.findall(r'[{0-9A-Z]?[^()\[\]{]*', var)  # {}

                        lst = []
                        for i in x:
                            if "{" in i:
                                lst.append(i)
                                x.remove(i)
                        string = ''.join(lst)
                        lst = list(string[0:string.find("}") + 2])
                        lst = ''.join(lst)
                        x.insert(0, lst)

                        var = undress(x, var)
                        y.remove(min(y))
                        order(var)
                        y = order(var)

                else:
                    break

            lst = re.findall(r'[A-Z0-9]?[^A-Z 0-9]*', var)
            dict.clear()
            simple_cutter(lst)

        else:
            print("Simple formula")
            lst = re.findall(r'[A-Z0-9]?[^A-Z 0-9]*', var)
            simple_cutter(lst)
        result = dict
        return result



if __name__ == '__main__':
    # Here we can make console input and check how function works

    # var = input('Input formula: ')
    var = 'Golden3(Eye6)6'
    # var = 'K4Fl4{G2[ON(Sn2)2]2H2}2Gy'
    # var = 'K4[ON(SO3)2]2'
    result = MyClass().parse(var)

    print(result)
