#dictionary keys can't be changable variable like list
dictionary = {
 "asliddin" : "Tursunov",
 "Jonibek" : ["Sharipov","AVazbek"]
 }

print(dictionary["Jonibek"])
print()

#dictionary methods like .get() and dict() function

dict2 = dict(greting = "Hello",
              sabr = "World")
print(dict2.get("Jonibek" , "He is Calculus Hero"))

# tuple()
# it look like a list/array but you can not change its values or add data
my_tuple = (1,2,3)
print(my_tuple)
print(my_tuple[0])
# it is not possible my_tuple[0] = 12
object = my_tuple[:]
print(object)

#set()
#it only gets unique values,
my_set = {1,2,3,4,5}
set2 = { 2,4,1,32,12,23}
print("difference()")
print(my_set.difference(set2))

print("discard()")
my_set.discard(1)
print(my_set)

print("difference_update()")
my_set.difference_update(set2)
print(my_set)
print("intersection()")
my_set.intersection_update(set2)
print(my_set)
print("isdisjoint()")
print(my_set.isdisjoint(set2))

print("issubset()")
print(my_set.issubset(set2))

print("issuperset()")
print(my_set.issuperset(set2))

print("union()")
print(my_set.union(set2))




