from random import choice
from string import ascii_letters
import math
from math import pi
from datetime import datetime
import random


def generate_password(length: int) -> str:
    return ''.join(choice(ascii_letters) for _ in range(length))


def encrypt_message(message: str) -> str:
    key = 2
    return ''.join(chr(num + key) for num in map(ord, message))


if __name__ == '__main__':
    assert encrypt_message('Dima') == 'Fkoc'
    assert encrypt_message('Vita') == 'Xkvc'
    assert encrypt_message('Dom') == 'Fqo'
    assert encrypt_message('Key') == 'Mg{'
    assert encrypt_message('Som') == 'Uqo'


def lucky_number(ticket: str) -> bool:
    left_side = int(ticket[0])+int(ticket[1])+int(ticket[2])
    right_part = int(ticket[3])+int(ticket[4])+int(ticket[5])
    return left_side == right_part


if __name__ == '__main__':
    assert lucky_number('667766') == True
    assert lucky_number('321051') == True
    assert lucky_number('123006') == True
    assert lucky_number('098189') == False
    assert lucky_number('432678') == False


def fizz_buzz(num: int) -> str:
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return str(num)


if __name__ == '__main__':
    assert fizz_buzz(6) == 'Fizz'
    assert fizz_buzz(25) == 'Buzz'
    assert fizz_buzz(15) == 'FizzBuzz'
    assert fizz_buzz(30) == 'FizzBuzz'
    assert fizz_buzz(2) == '2'


def password_is_strong(password: str) -> bool:
    if len(password) < 10:
        return False
    if password.upper() == password:
        return False
    if password.lower() == password:
        return False
    return any(_.isdigit() for _ in password)


if __name__ == '__main__':
    assert password_is_strong('abcd111') == False
    assert password_is_strong('aaaaa11aaaaaaa') == False
    assert password_is_strong('AAAAAAAAAA1111') == False
    assert password_is_strong('AaaaaaaaaaaB') == False
    assert password_is_strong('aaaaAaaaa1') == True


def number_is_prime(num: int) -> bool:
    square_root = int(math.sqrt(num))
    if num < 2:
        return False
    elif num == 2:
        return True
    i = 2
    while i <= square_root:
        if num % i == 0:
            return False
        i += 1
    return True


if __name__ == '__main__':
    assert number_is_prime(17) == True
    assert number_is_prime(61) == True
    assert number_is_prime(83) == True
    assert number_is_prime(40) == False
    assert number_is_prime(65) == False


def decrypt_message(message: str) -> str:
    key = 2
    return ''.join(chr(num - key) for num in map(ord, message))


if __name__ == '__main__':
    assert decrypt_message('Fkoc') == 'Dima'
    assert decrypt_message('Xkvc') == 'Vita'
    assert decrypt_message('Fqo') == 'Dom'
    assert decrypt_message('Mg{') == 'Key'
    assert decrypt_message('Uqo') == 'Som'
    

def volume_of_sphere(radius: float) -> float:
    volume = (4/3)*pi*pow(radius, 3)
    volume_sphere = round(volume, 2)
    return volume_sphere


if __name__ == '__main__':
    assert volume_of_sphere(2) == 33.51
    assert volume_of_sphere(5) == 523.60
    assert volume_of_sphere(10) == 4188.79
    assert volume_of_sphere(15) == 14137.17
    assert volume_of_sphere(20) == 33510.32


def days_diff(start_date: ..., end_date: ...) -> int:
    d1 = datetime.strptime(start_date, '%d.%m.%Y')
    d2 = datetime.strptime(end_date, '%d.%m.%Y')
    difference = abs(d2 - d1).days
    return difference


if __name__ == '__main__':
    assert days_diff('14.03.2021', '16.03.2021') == 2
    assert days_diff('12.03.2021', '16.03.2021') == 4
    assert days_diff('10.03.2021', '16.03.2021') == 6
    assert days_diff('05.03.2021', '16.03.2021') == 11
    assert days_diff('01.03.2021', '16.03.2021') == 15


def prs(client_choice: str) -> str:
    server_choice = random.choice(['p', 'r', 's'])
    if client_choice == 'p' and server_choice == 'p':
        return 'draw'
    elif client_choice == 'p' and server_choice == 'r':
        return 'won'
    elif client_choice == 'p' and server_choice == 's':
        return 'lost'
    elif client_choice == 'r' and server_choice == 'p':
        return 'lost'
    elif client_choice == 'r' and server_choice == 'r':
        return 'draw'
    elif client_choice == 'r' and server_choice == 's':
        return 'won'
    elif client_choice == 's' and server_choice == 'p':
        return 'won'
    elif client_choice == 's' and server_choice == 'r':
        return 'lost'
    elif client_choice == 's' and server_choice == 's':
        return 'draw'
    else:
        return 'Enter correct data'


def integer_as_roman(integer: int) -> str:
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thous = ["", "M", "MM", "MMM", "Mv", "v", "vM", "vMM", "vMMM", "Mx"]

    t = thous[integer // 1000]
    h = hunds[integer // 100 % 10]
    te = tens[integer // 10 % 10]
    o = ones[integer % 10]

    return t+h+te+o


if __name__ == '__main__':
    assert integer_as_roman(9) == 'IX'
    assert integer_as_roman(15) == 'XV'
    assert integer_as_roman(123) == 'CXXIII'
    assert integer_as_roman(650) == 'DCL'
    assert integer_as_roman(3541) == 'MMMDXLI'
