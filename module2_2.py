print("Введите  3 числа:")
first = int(input())
second = int(input())
third = int(input())
if first == second == third:
    print (int(3))
elif first == second or second == third or  third == first :
    print(int(2))
elif first!=second or second != third or third != first:
    print(0)
