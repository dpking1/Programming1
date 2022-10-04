#  1. Write an if statement that assigns 20 to the variable y, and assigns 40 to the variable
#  z if the variable x is greater than 100.

# x = int(input("give a value for x: "))

# if x > 100:
   # y = 20
   # z = 40

#print(y)
#print(z)

# 5.
# gathering input
amount1 = int(input('choose a numerical amount: '))
amount2 = int(input('choose another numerical amount:'))

# write conditional nested statement
if amount1 > 10:
    if amount2 < 100:
        if amount1 > amount2:
            print(amount1)
        elif amount2 > amount1:
            print(amount2)
        else:
            amount2 == amount1
            print("amount 1 is {amount1} ")