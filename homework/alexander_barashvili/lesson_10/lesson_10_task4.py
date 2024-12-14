PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

price_dict = {key: int(value[:-1]) for key, value in (x.split(' ') for x in PRICE_LIST.split('\n'))}

print(price_dict)
