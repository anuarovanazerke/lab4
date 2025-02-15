"""def square_generator(N):
    for i in range(N + 1):
        yield i ** 2

N = int(input("N ="))
for num in square_generator(N):
    print(num, end=" ")



def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("n ="))
print(",".join(str(num) for num in even_numbers(n)))



def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n =int(input("n = "))
print(list(divisible_by_3_and_4(n)))

a=int(input("a = "))
b=int(input("b = "))
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

for sq in squares(a, b):
    print(sq)"""


n=int(input("n = "))
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

for num in countdown(n):
    print(num, end=" ")




