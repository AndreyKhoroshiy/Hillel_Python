def parse_cookie(query: str) -> dict:
    my_str = query
    index = my_str.find('=')
    if index == -1:
        my_dict = {}
    else:
        my_new_str = my_str.replace(';', ' ')
        my_new_str = my_new_str.strip()
        my_new_str = my_new_str.replace(' ', ':')
        try:
            my_dict = dict(x.split('=') for x in my_new_str.split(':'))
        except ValueError:
            my_new_str = my_new_str.replace('=', ';', 1)
            my_new_str = my_new_str.split(':')
            my_list = my_new_str[-1].replace('=', ';')
            my_second_str = ''.join(my_list)
            my_final_str = my_new_str[0] + ' ' + my_second_str
            my_dict = dict(x.split(';') for x in my_final_str.split(' '))
    print(my_dict)
    return my_dict


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
