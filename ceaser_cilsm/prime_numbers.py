def primeNumber(number):
    is_prime = True
    for i in range(2,number):
        if number % i ==0:
            is_prime = False
    if is_prime:
        return "it is prime number"
    else:
        return "It is not prime number"

print(primeNumber(int(input("Enter a number: "))))