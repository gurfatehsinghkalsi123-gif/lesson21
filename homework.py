
list1 = list(map(int, input("Enter numbers separated by space: ").split()))

list2 = [x*x for x in list1]

print("List 1:", list1)
print("List 2 (squares):", list2)
