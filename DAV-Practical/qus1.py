dict_of_lists = {'Boys': [72, 68, 70, 69, 74], 'Girls': [63, 65, 69, 62, 61]}
list_of_dicts = []
for i in range(len(dict_of_lists['Boys'])):
    list_of_dicts.append({'Boys': dict_of_lists['Boys'][i], 'Girls': dict_of_lists['Girls'][i]})

print(list_of_dicts)
