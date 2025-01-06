class SuperList:
    def __init__(self,key):
        self.key = key

    def __len__(self):
        i = 0
        for k in self.key:
            i+=1
        return i
    def __append__(self,element):
        self.key += element
        return self.key

lst = SuperList([1,2,4,2,3,23,12,32])
print(len(lst))
print(lst.__append__(12))


