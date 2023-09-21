# -*- coding: utf-8 -*-
# time:2023/8/21 14:12
# file test.py
# outhor:czy
# email:1060324818@qq.com

data = [('C2', 'Incomplete'), ('C2', 'Complete'), ('C4', 'Incomplete'), ('C10', 'Incomplete'), ('C10', 'Incomplete'), ('C10', 'Completed'), ('C11', 'Incomplete'), ('C11', 'Incomplete'), ('cf', 'Done')]

# Step 1: Get all elements where the second column is 'Incomplete'
incomplete_elements = [element for element in data if element[1] == 'Incomplete']

# Step 2: Remove elements where the second column is 'Incomplete' and remove related elements
filtered_data = []
removed_names = set()
for element in data:
    if element[1] != 'Incomplete':
        filtered_data.append(element)
    else:
        removed_names.add(element[0])

final_data = [element for element in filtered_data if element[0] not in removed_names]

print("All elements where the second column is 'Incomplete':")
print(incomplete_elements)
print("\nFiltered data after removing related elements:")
print(final_data)






