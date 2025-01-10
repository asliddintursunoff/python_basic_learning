# from time import time
# def time_taken(func):
#     def wrap(*args):
#         a1 = time()
#         func(*args)
#         b = time()
#         print( b-a1)
#     return wrap
print("\n\nfibonachi with list")
def fibonaciList(num):
    lst = range(num)
    fib_vars = [0,1]
    if num==0 or num == 1:
        return zip(lst,fib_vars)
    else:
        for i in lst:
            if i>1:
                fn = fib_vars[i-1]+fib_vars[i-2]
                fib_vars.append(fn)
            else:
                continue
    return list(zip(lst,fib_vars))
print(fibonaciList(8))
print("\n\nfibonachi with generator")
def fibonaci(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp+b

a = 0
for x in fibonaci(21):
    print(f"{a} - {x}")
    a+=1
    

   
    

