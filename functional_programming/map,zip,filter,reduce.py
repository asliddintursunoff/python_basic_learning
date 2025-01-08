from itertools import count

#not using any method
lst = [1,2,3]
some_list = ['a','b','c','b','d','m','n','n']
new_list = []
for i in range(len(some_list)):
    for x in  range(len(some_list)):
        if some_list[i] == some_list[x] and i!=x:
            if some_list[x] not in new_list:
                new_list.append(some_list[x])
duplicateList = []
for a in some_list:
    if some_list.count(a)>=2:
        if a not in duplicateList:
            duplicateList.append(a)
print(f"not with count() {new_list}")
print(f"with count() {duplicateList}")

duplicates = {item for item in some_list if some_list.count(item)>=2}

func = (lambda item: item**2)
print(list(map(func,lst)))
print(f"functional programming, list comprehension:  {list(duplicates)}")