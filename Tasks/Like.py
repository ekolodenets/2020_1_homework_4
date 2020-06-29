'''
Мне нравится 👍
Создайте функцию, которая, принимая массив имён, возвращает строку описывающая количество лайков (как в Facebook).

def likes(*arr: str) -> str:
    pass
Примеры:

likes() -> "no one likes this"
likes("Peter") -> "Peter likes this"
likes("Jacob", "Alex") -> "Jacob and Alex like this"
likes("Max", "John", "Mark") -> "Max, John and Mark like this"
likes("Alex", "Jacob", "Mark", "Max") -> "Alex, Jacob and 2 others like this"
Бонусные очки
Функция работает на нескольких языках и кодировках - язык ответа определяется по языку входного массива.
'''


class MyClass:

    def likes(self, var: str) -> str:
        from langdetect import detect
        lst = []

        result = 'No one like this'

        if len(var) > 0:
            lang = detect(var)
            var = var.replace(',', '')
            lst = ' '.join(var.split())
            lst = lst.split(" ")

            # Paweł Krzysztof Yuzef Zofia Amelia        -> PL
            # Ulrich Gertrud Ernst Wilhelm Friedrich    -> DE
            # Марина Александр Евгений Андрей Сергей    -> RU

            if len(lst) == 1:
                lst = " ".join(x.strip('"') for x in lst) + ' likes this'
            elif len(lst) == 2:
                lst = " and ".join(x.strip('"') for x in lst) + ' like this'
            elif len(lst) == 3:
                lst = f'{lst[0]}, {lst[1]} and {lst[2]} like this'
                lst = lst.replace('"', '')
            elif len(lst) > 3:
                lst = f'{lst[0]}, {lst[1]} and {len(lst) - 2} others like this'
                lst = lst.replace('"', '')

            if lang == "de":
                lst = lst.replace('and', 'und').replace('others like this', 'hat es gefallen').replace('likes this', 'hat das gefallen').replace('like this', 'mögen das')
            elif lang == "ru":
                lst = lst.replace('and', 'и').replace('others like this', 'другим это понравилось').replace('likes this', 'это понравилось').replace('like this', 'это понравилось')
            elif lang == "pl":
                lst = lst.replace('and', 'i').replace('others like this', 'innym się spodobało').replace('likes this', 'się spodobało').replace('like this', 'spodobało się')

            return lst
        # return result



if __name__ == '__main__':
    # Here we can make console input and check how function works

    var = input('Input names: ')

    result = MyClass().likes(var)

    print(result)
