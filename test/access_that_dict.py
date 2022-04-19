from import_dict import City

def printCity():
    print('City')
    for key in City:
        c = City[key]
        i = c['id']
        x = c['x']
        y = c['y']
        print(key, '  ', i, '  ', x, '  ', y, sep='')
    print()