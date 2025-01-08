a = "hello"
b = ""
# for x in range(len(a)):
#     b += a[-1]
#     a = a[:-1]
print(a)
new = ""
# def rewrite(obj):
#
#     if len(obj)==0:
#         return new
#     else:
#         new += obj[-1]
#         return rewrite(obj[:-1])
#
# print(rewrite(a))

def hoho(func):
    def wrap(item):
        print("*******")
        func(item)
        print("**********")

    return wrap
@hoho
def hi(greeting):
    print(greeting)

hi("bro")