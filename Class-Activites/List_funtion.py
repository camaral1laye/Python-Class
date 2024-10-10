fruit =["Banana", "Mango", "Apple"]
fruit[1] = "Grapes"

print(fruit[1])
print(len(fruit))
print(fruit)

food = "Banana"
if food in fruit:
    fruit.remove(food)
    print(fruit)


name = ["w", "z", "d"]
name[0] = "M"
print(name[0])
print()