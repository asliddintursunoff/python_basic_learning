class BOOK:
    def __init__(self, book_name):
        self.book_name = book_name

    def book(self):
        return self.book_name


lst = []
n = int(input("how many book you want to enter: "))
for i in range(0, n):
    a = input("Enter book name: ")
    lst.append(BOOK(a))
finding = input("Enter book name which you want to find in our library: ")
no = "we do not have this book"
for i in lst:

    if i.book() == finding:
        no = f"Yes we have this book {i.book()}"

print(no)
