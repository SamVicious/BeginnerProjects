number = bin(int(input()))[2:]
number += number[0]
number = number[1:]
print(int(number, 2))