# input() => n
# 1 to n,
# 3의 배수, "fizz"
# 5의 배수, "buzz"
# 15의 배수, "fizzbuzz"
# 나머지, 1

n = int(input())

for i in range(1, n+1) :
    if (n % 15 == 0) :
        print("fizzbuzz")
    elif (n % 5 == 0) :
        print("buzz")
    elif (n % 3 == 0) :
        print("fizz")
    else :
        print(i)
