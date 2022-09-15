"""ChainMap принимает любое количество сопоставлений или
 словарей и превращать их в единое обновляемое представление."""

from collections import ChainMap

computer_parts = {
    'system_block': 1,
    'monitor': 1,
    'keyboard_mouse': 1
}

computer_options = {
    'RAM': '8 Gb',
    'HDD': '1000 Gb',
    'PROC': 'Intel Core i5'
}

computer_accessories = {
    'RAM': '6 Gb',
    'gaming': False,
    'divided': True,
}

"""
мы создали три словаря Python. 
Далее, мы создали экземпляр ChainMap, 
передав эти три словаря. В конце мы попытались 
получить доступ к одному из ключей в нашем ChainMap.
После этого, ChainMap пройдет через каждое сопоставление, 
чтобы увидеть, существует ли данный ключ и имеет ли он значение. 
Если это так, тогда ChainMap вернет первое найденное значение, 
которое соответствует ключу."""

computer_pricing = ChainMap(computer_options, computer_parts, computer_accessories)

print(computer_pricing)
print(computer_pricing['RAM'])  # выполняет поиск по всем ключам но возвращает значение только первого

computer_pricing['opt'] = '20 Gb'  # создаст в первом

computer_pricing['RAM'] = '20 Gb'  # заменит в первом
print(computer_pricing)

computer_accessories['add'] = 100

print(computer_pricing)
