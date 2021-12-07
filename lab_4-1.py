# Author: SMR (AMDG) 12/3/21
total=0
while True:
    number=input("Enter a number: ")
    if number=="-1":
        break
    else:
        total+=int(number)
print("The sum of all the numbers entered is {0}".format(total))


