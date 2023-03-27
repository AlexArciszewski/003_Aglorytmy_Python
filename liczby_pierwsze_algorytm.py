from math import sqrt

""" 
Devs-Mentoring
Zad 1. 
Napisz funkcję, która przyjmie liczbę całkowitą n i zwróci pierwsze n liczb pierwszych. 

"""



def prime_generator(number: int) -> bool: #true flse
    prime_numbers = []
    if number == 0 or number == 1:
        return False
    
    for i in range(2,number):
        if number % i == 0:
            return False
    return True    
    
    
    
  
  
  
    

print(prime_generator(7))

def prime_generator(number: float) -> bool: #true flse
    prime_numbers = []
    if number == 0 or number == 1:
        return False
    
    for i in range(2,int(number/2)):
        if number % i == 0:
            return False
    return True    
    
    
    
  
  
  
    

print(prime_generator(7))



def prime_generator(number: float) -> bool: #true flse
    prime_numbers = []
    if number == 0 or number == 1:
        return False
       
    for i in range(2,int(number**0.5)):
        if number % i == 0:
            return False
       
    return True
    
print(prime_generator(7))




def prime_generator(number: int) -> None:
    prime_numbers = []
    for numbers in range(number + 1):
        if number == 0 or number == 1:
            return False
        else:
            for i in range(2,int(number**0.5)):
                if number % i == 0:
                    return False
                else:
                    prime_numbers.append(numbers)
    return(prime_numbers)
            
    
print(prime_generator(8))


print("z4")
def prime_gen(number: int) -> None:
    prime_numbers = []
    for number in range(number + 1):
        if number == 0 or number == 1:
            return False
       
        for i in range(2,int(number**0.5)):
            if number % i == 0:
                return False
            else:
                prime_numbers.append(number)
    
                return print(prime_numbers)
    
print(prime_gen(13))





print("z4")


def prime_gen(number: int) -> None:
    prime_numbers = []
    if number == 0 or number == 1:
        return False
      
    for i in range(2,int(number**0.5)):
        if number % i == 0:
            return False
        else:
            prime_numbers.append(number)
        return print(prime_numbers)
    
print(prime_gen(13))

print('z5') 
def func(number):
    list = []
    for number in range(0, number +1):
        list.append9
        if number == 0 or number == 1:
            return False
        
        for i in range(2,int(number**0.5)):
            if number % i == 0:
                return False
            else:
                list.append(number)
                print(list)
        return list
    
print(func(33))
        
        
        
        
        
""" 
def prime_generator(number: int) -> bool: 
    prime_numbers = []
    if number == 0 or number == 1:
        return False
       
    for i in range(2,int(number**0.5)):
        if number % i == 0:
            return False
       
    return True
    
print(prime_generator(7))



def primer_list(number):
    list = []
    for number in range(0, number + 1):
        if prime_generator(number) == True:
            list.append(number)
    return list       
print(primer_list(7))
    
def function_A():
      print("I am function A.")
  return
 
def function_B():
  print("I am function B.")
  function_A()
  return
 
function_B()
print("I am now outside the functions.")    
"""               
def primer_list(number):
    list = []
    for number in range(0, number + 1):
        if prime_generator(number) == True:
            list.append(number)
    return list       
print(primer_list(7))

        
    def prime_generator(number: int) -> bool: 
        prime_numbers = []
        if number == 0 or number == 1:
            return False
       
        for i in range(2,int(number**0.5)):
            if number % i == 0:
                return False
       
        return True
    
    print(prime_generator(7))
    

def is_prime(num):
    pass

#i druga funckja to

def prime_numbers(n):
    arr = []
     for i in range(n):
           if is_prime(i):
                arr.append(i)
            else:
                continue (edited)     

def prime_generator(number: int) -> bool: 
    
    if number == 0 or number == 1:
        return False
       
    for i in range(2,int(number**0.5)):
        if number % i == 0:
            return False
       
    return True

prime_generator(13)