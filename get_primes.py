import numpy as np

def is_even(a):
    if a%2 !=0:
        return False
    else:
        return True

def is_prime(a):
    if a==1|a==2:
        return false
    elif is_even(a):
        return False
    elif get_factorials(a)>2:
            return False
    else:
            return True

def get_factorials(a):

    divisors=2

    for i in range(2,a-1):
        if (a/i).is_integer():
            divisors+=1

    return divisors

def get_primes(a):
    primes=[]
    for i in range(1,a+1):
        if is_prime(i):
            primes.append(i)
    return primes


number=int(input("Enter a number: "))
primes=get_primes(number)

print("There are ",len(primes)," primes between 1 and ",number,"\n")
print("The primes are as follows:",primes,"\n")

import timeit

start = timeit.default_timer()

#Your statements here

stop = timeit.default_timer()

print(stop-start," seconds to execute")
