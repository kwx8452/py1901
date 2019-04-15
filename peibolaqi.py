def fun(num):
    a = 0
    b = 1
    yield a
    yield b
    count = 0
    while count <num:
        a,b = 0+b, a+b
        yield b
        count+=1
r = fun(10)
for r in r:
    print(r)

