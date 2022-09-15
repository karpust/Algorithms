import json
from pympler import asizeof

gen_dict = {i: i * 2 for i in range(100000)}
dumped_dict = json.dumps(gen_dict)
print(type(dumped_dict))

out_dict = json.loads(dumped_dict)
print(type(out_dict))

print('Размер list: ', asizeof.asizeof(gen_dict))
print('Размер json: ', asizeof.asizeof(dumped_dict))

"""
<class 'dict'>
<class 'str'>
Размер list:  11638840
Размер json:  1633384
"""

# ВРЕМЯ ?
