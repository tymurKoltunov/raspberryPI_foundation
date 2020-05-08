def countdown():
    n = 4
    while (n > 0):
        yield n
        n -= 1

c = countdown()
print(c)
print(next(c))