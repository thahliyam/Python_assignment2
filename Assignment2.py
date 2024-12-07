# Data structures in python 
# List Exercise
# Q1. Create a list of 5 random numbers and print the list.
List=[23,21,1,3,56]
print('List of random numbers = ',List)

# Q2. Insert 3 new values to the list and print the updated list.
List.extend([7,5,16])
print('Updated list = ',List)

# Q3. Try to use a for loop to print each element in the list.
for i in List:
    print(i)

# Topic: Dictionary Exercise
# Q1. Create a dictionary with keys 'name', 'age', and 'address'
# and values 'John', 25,and 'New York' respectively.
Person={'Name':'John','Age':25,'Address':'New York'}
print(Person)
print(type(Person))

# Q2. Add a new key-value pair to the dictionary created in Q1
# with key 'phone' and value '1234567890'.
Person['Phone']='1234567890'
print(Person)

# Topic: Set Exercise
# Q1.Create a set with values 1, 2, 3, 4, and 5.
Set={1,2,3,4,5}
print(Set)

# Q2. Add the value 6 to the set created in Q1.
Set.add(6)
print(Set)

# Q3. Remove the value 3 from the set created in Q1.
Set.remove(3)
print(Set)

# Topic:Tuple Exercise
# Q1. Create a tuple with values 1, 2, 3, and 4
Tuple_t1=(1,2,3,4)
print(Tuple_t1)

# Q2. Print the length of the tuple created in Q1.
print(len(Tuple_t1))