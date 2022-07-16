from tomlkit import value


def main():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {'firstname':'Miguel', 'lastname':'Tarazona'}

    super_list = [
        {'firstname':'Miguel', 'lastname':'Tarazona'}, 
        {'firstname':'Jose', 'lastname':'Vega'},
        {'firstname':'Angel', 'lastname':'Gamboa'},
        {'firstname':'Carlos', 'lastname':'Blanco'}
    ]

    super_dict = {
        'natural_nums':[1,2,3,4,5],
        'integer_nums':[-2,-1,0,1,2],
        'floating_nums':[1.1,4.5,6.43]
    }

    for key, value in super_dict.items():
        print(key, '-', value)

    for i in super_list:
        print(i['firstname'], '-', i['lastname'])

if __name__ == '__main__':
    main()