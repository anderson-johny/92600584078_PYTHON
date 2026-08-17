print("=============== Tuple Example ===============")

tuple = (10, 20, 30, 40, 50, 100, 80)
print("Tuple                :", tuple)
print("First element        :", tuple[0])
print("Last element         :", tuple[-1])
print("Slice (index 1 to 3) :", tuple[1:4])
print("Length of tuple      :", len(tuple))
print("Count of 20          :", tuple.count(20))
print("Index of 30          :", tuple.index(30))

print("=============== Set Example ===============")

set = {10, 20, 30, 40, 50, 20}
print("Set                  :", set)
set.add(60)
print("After adding 60      :", set)
set.remove(30)
print("After removing 30    :", set)
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Set A                :", set_a)
print("Set B                :", set_b)
print("Union                :", set_a.union(set_b))
print("Intersection         :", set_a.intersection(set_b))
print("Difference (A - B)   :", set_a.difference(set_b))
print("Symmetric Difference :", set_a.symmetric_difference(set_b))