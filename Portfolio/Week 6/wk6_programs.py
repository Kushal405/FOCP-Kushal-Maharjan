
# 1.Write a function that accepts a positive integer as a parameter and then returns a
# representation of that number in binary (base 2).


def decimal_to_binary(number):
    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must be a positive integer")

   
    if number == 0:
        return "0b0"

    binary_representation = ""

    while number > 0:
        binary_representation = str(number % 2) + binary_representation
        number //= 2

    return "0b" + binary_representation

# Testing the function
positive_integer = 42
binary_representation = decimal_to_binary(positive_integer)
print(f"The binary representation of {positive_integer} is: {binary_representation}")
print()



# 2.Write and test a function that takes an integer as its parameter and returns the
# factors of that integer. (A factor is an integer which can be multiplied by another to
# yield the original).


def number(num):
    factor = []
    for i in range(1, num + 1):
        if num % i == 0:
            factor.append(i)
    return factor

#testing the function
test = 12
result = number(test)

print(f"The factors of {number} are: {result}")
print()


#3.Write and test a function that determines if a given integer is a prime number. A
# prime number is an integer greater than 1 that cannot be produced by multiplying
# two other integers.


def prime_num(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

#Testing the function
print(prime_num(3))
print(prime_num(16))
print(prime_num(22))
print()

# 4.Computers are commonly used in encryption. A very simple form of encryption
#(more accurately "obfuscation") would be to remove the spaces from a message
#and reverse the resulting string. Write, and test, a function that takes a string
#containing a message and "encrypts" it in this way.''''



def encrypt_message(message):
    message_without_spaces = message.replace(" ", "")
    
    encrypted_message = message_without_spaces[::-1]
    
    return encrypted_message
# Testing the function
print(encrypt_message("Hello World!!.This is  week 6 portfolio"))
print()



#5.Another way to hide a message is to include the letters that make it up within
#seemingly random text. The letters of the message might be every fifth character,
#for example. Write and test a function that does such encryption. It should
#randomly generate an interval (between 2 and 20), space the message out
#accordingly, and should fill the gaps with random letters. The function should
#return the encrypted message and the interval used.
#For example, if the message is "send cheese", the random interval is 2, and for
 #clarity the random letters are not random:

#send cheese
 
#s e n d c h e e s e
 
#sxyexynxydxy cxyhxyexyexysxye'''


import random
import string

def encrypt_message(message):
   
    interval = random.randint(2, 20)
    
    encrypted_chars = []
    
    for i, char in enumerate(message):
        if char != ' ' and i % interval == 0:
            encrypted_chars.append(char)
        else:
            
            encrypted_chars.append(random.choice(string.ascii_lowercase))
    
    
    encrypted_message = ''.join(encrypted_chars)
    
    return encrypted_message, interval

# Testing the function
original_message = "send cheese"
encrypted_result, interval_used = encrypt_message(original_message)

print(f"Original Message: {original_message}")
print(f"Encrypted Message: {encrypted_result}")
print(f"Interval Used: {interval_used}")
print()
