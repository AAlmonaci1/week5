# collection = single variable used to store multiple values
#   List = [] ordered and changeable
#   Set = {} unordered and immutable(unchangeable), but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple", "orange", "banana", "cocunut", "kiwi", "dragonfruit"]
print(fruits[1]) #this will print orange
print(fruits[0:3]) #this will print apple orange banana coconut
for fruit in fruits:
#print(fruit)
#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print("pineapple" in fruits) #false boolean 
fruits[0] = "pineapple" #changing value
fruits.append("pineapple")git
fruits.sort()
fruits.reverse()
fruits.clear()