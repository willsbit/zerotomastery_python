#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1= Cat('Ginger', 4)
cat2= Cat('Maxi', 2)
cat3= Cat('Ruby', 11)


# 2 Create a function that finds the oldest cat

def oldestCat(*args):
  return max(args)
 
# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'O gato mais velho tem {oldestCat(cat1.age, cat2.age, cat3.age)} anos de idade')