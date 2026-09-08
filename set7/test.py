dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

for i, key in enumerate(dict):
    if i % 2 == 0:
        print(key, dict[key])
