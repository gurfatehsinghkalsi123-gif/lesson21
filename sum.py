loan = [1, 2, 3, 54, 21, 32, 43]
print(loan)
sum = 0 
for item in loan:
    sum = sum+item
print("The sum of all the numbers is", sum)
avg = sum/len(loan)
print("the avg of the list is: ", avg)
mv = min(loan)
print("the minimun is :", mv)
mx = max(loan)
print("the maximum is:", mx)