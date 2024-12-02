my_set={1,2,3}
print(my_set)

my_set={2.5, "LEON", (1,2,3,4,5)}
print(my_set)

my_set={1,2,3,2,4,1,6,6,7,3,5}
print(my_set)

my_set=set([6,9,6,9,1,2,3])
print(my_set)

my_set=set([6,9,6,9,1,2,3,45,1,2,5,6,2,7,3,7,4,6,3,5,3,6,3,6,3,6,4,6,4,6,4,6,46,5,6,3,6,3,6,6,4,6,7,4,6,7,4,3,6,7,55,6,7])
print("orignal set")
print(my_set)

my_set.pop()
print("After removing the first element from the orignal set")
print(my_set)