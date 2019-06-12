# input() => n
# 1 to n,
# 3의 배수, "fizz"
# 5의 배수, "buzz"
# 15의 배수, "fizzbuzz"
# 나머지, 1

n = int(input("숫자입력 : "))

if (n % 15 == 0) :
    print([n, 15*n, "fizzbuzz"])
elif (n % 3 == 0) :
    print([n, 3*n, "fizz"])
elif (n % 5 == 0) :
    print([n, 5*n, "buzz"])
else :
    print(n, n+1, n+2)
