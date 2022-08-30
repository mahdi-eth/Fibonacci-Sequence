def fibonacci_maker(n):
    number1 = 0
    fibonacci = 1
    term = 0
    print(0)
    while term <= n:
        print(fibonacci)
        number2 = fibonacci + number1
        number1 = fibonacci
        fibonacci = number2
        term += 1
        

n = abs(int(input("Enter a number to see the fibonacci sequence up to that number : ")))
fibonacci_maker(n)