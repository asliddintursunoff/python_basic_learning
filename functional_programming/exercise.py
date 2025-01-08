"""Every problem  get them from ChatGPT"""

"""Problem 1:
Write a decorator @process_numbers that:

Filters out numbers that do not satisfy a given condition. The condition is that the number should be a multiple of 3 or 5.
Transforms the filtered numbers by squaring them.
Returns a dictionary where the keys are the original numbers and the values are the squared values."""
numbers = [1, 3, 5, 8, 10, 15, 20]
def process_numbers(func):
    def wrap_func(*args , **kwargs):

       func(*args , **kwargs)
       lst = {item:item**2 for item in func(*args,**kwargs) if item%3==0 or item%5==0}

       return lst


    return wrap_func
@process_numbers
def get_numbers(number):
    return number
print(get_numbers(numbers))

print("******************************************************\n******************************************************\n")
"""Problem 2 :
You are given two lists of dictionaries representing student grades in different subjects, and you need to process these data using higher-order functions and functional programming techniques.

students_grades_1: A list of dictionaries containing student names and their grades in Math.
students_grades_2: A list of dictionaries containing student names and their grades in Science.
You need to write a Python function process_grades that performs the following tasks:"""

students_grades_1 = [
    {"name": "John", "Math": 65},
    {"name": "Alice", "Math": 72},
    {"name": "Bob", "Math": 55},
    {"name": "Charlie", "Math": 45}
]

students_grades_2 = [
    {"name": "John", "Science": 60},
    {"name": "Alice", "Science": 50},
    {"name": "Bob", "Science": 45},
    {"name": "Charlie", "Science": 40}
]

students = list(zip(students_grades_1,students_grades_2))
print(students)

filtering = list(filter((lambda x: x[0]["Math"]>=50 and x[1]["Science"]>=50) , students  ))
print(filtering)


def average_score(lst,subject):
    res = list(map(lambda i : i[subject] , lst))
    avr = sum(res)/len(res)
    return avr
print(average_score(students_grades_2,"Science"))
