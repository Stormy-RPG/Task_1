# На вход подается строка, все символы находятся в нижнем регистре и без пробелов. 
# Напишите функцию, которая будет возвращать True, если строка является палиндромом и False, если строка палиндромом не является.

# Функция проверки на палиндром
def is_palindrome(line):
    if line == line[::-1]:
        return True
    else:
        return False
    
# Примеры работы функции
print('1.', is_palindrome('лепсспел'))
print('2.', is_palindrome('helloworld'))
print('3.', is_palindrome('atta'))
print('4.', is_palindrome('бабочка'))
print('5.', is_palindrome('ttttt'))
print('6.', is_palindrome('ghugigivdh'))

# Пример работы функции при вводе с клавиатуры
# print(is_palindrome(input('Введите слово для проверки: ')))