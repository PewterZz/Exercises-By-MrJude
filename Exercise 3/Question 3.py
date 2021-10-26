# Question 3
def num_atoms(grams, atomic=196.97):
    moles = grams/atomic
    atoms = moles * (6.022*(10**23))
    print(atoms)

num_atoms(10,1.008)
