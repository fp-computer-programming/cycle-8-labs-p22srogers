# Author: SMR (AMDG) 12/2/21
# def sum_to(n):
# total = 0
# for i in range(n+1):
# total += i
#return total
from types import WrapperDescriptorType


def sum_to(n):
    total=0
    x=0
    while x<=int(n):
        x+=1
        total+=x
    return total
num=input("Enter an Integer: ")
print(sum_to(num))