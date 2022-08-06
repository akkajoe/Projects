print('Hi, we will multiply  your number with its previous number until the previous number is 1')
user_input = input("Enter a number ")
num = int(user_input)
n = num
def multiplier(n):
    if n < 0:
        print("Sorry the num cannot be negative")
    elif n == 0:
        print("The result is 1")
    else:
        mult = 1
        while n > 0:
            mult = mult * n
            n -= 1
        print(mult)
multiplier(n)