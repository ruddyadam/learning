def fib(num):
    if num <= 2:
        return 1
    return fib(num - 2) + fib(num - 1)

while True:
    fibnum = int(input("Enter a fib number to caclulate: "))
    print(fib(fibnum))

