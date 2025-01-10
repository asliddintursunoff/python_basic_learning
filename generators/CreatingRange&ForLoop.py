

class MyRange:
    item = 0
    def __init__(self,start,final):
        self.start = start
        self.final = final

    def __iter__(self):
        return self

    def __next__(self):
        if MyRange.item < self.final:
                num = MyRange.item
                MyRange.item +=1
                return num
        raise StopIteration("Hello bitch")



gen =MyRange(0,40)

for i in gen:
    print(i)

#
# def reverse_word(word):
#     if len(word) > 0:
#         print( word[-1], end="bitch")
#         return reverse_word(word[:-1])
# reverse_word(" ! tseb si nohtyp")

def for_loop(obj):
    itradi = iter(obj)
    while True:
        try:

            print(next(itradi))
        except:
            break


for_loop([1,4,5,6,7])



