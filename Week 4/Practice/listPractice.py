typePokemon = ['fire', 'water', 'electric', 'grass']
starter = ['squirtle', 'bulbasaur', 'charmander', 'pikachu']


print(starter[int(1.0)].capitalize(), 'is a', typePokemon[3].capitalize(), 'type.')



spam = [['cat', 'bat'], [10, 20, 30, 40, 50]] 
print(spam[0]) 
print(spam[0][1]) 
print(spam[1][4])

# Annotation: Counts backward from the end. Extremely useful 
# when you want the final item of a list without calculating 
# its length (len(spam) - 1).

print()
print()
weapon = ['sword', 'axe', 'lance', 'bow']  
print(weapon)
print('weapon[0:4]  =', weapon[0:4])  
print('weapon[1:3]  =', weapon[1:3])
print('weapon[0:-1] =', weapon[0:-1])
print('weapon[1:]   =', weapon[1:])
print('weapon[:]    =', weapon[:])