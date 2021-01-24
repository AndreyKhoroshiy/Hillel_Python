def parse(query: str) -> dict:
    my_str = query
    index = my_str.find('?')
    if index == -1:
        my_dict = {}
    else:
        my_list = my_str.split("?")
        my_first_list = my_list[-1:]
        my_new_str = ''.join(my_first_list)
        my_new_str = my_new_str.strip()
        if len(my_new_str) == 0:
            my_dict = {}
        else:
            my_new_str = my_new_str.replace('&', ',')
            my_new_str = my_new_str.strip(',')
            my_dict = dict(x.split('=') for x in my_new_str.split(','))
    print(my_dict)
    return my_dict


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('https://example.com/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/pathto/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https:/example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&year=1987') == {'name': 'ferret',
                                                                                            'color': 'purple',
                                                                                            'year': '1987'}
    assert parse('http://example.com/?name=Dima ') == {'name': 'Dima'}
