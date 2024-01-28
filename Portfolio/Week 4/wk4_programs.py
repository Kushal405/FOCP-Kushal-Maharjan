

# 1.Functions are often used to validate input. Write a function that accepts a single
# integer as a parameter and returns True if the integer is in the range 0 to 100
# (inclusive), or False otherwise. Write a short program to test the function.


def integer_number(a):
    if 0<=a and a<= 100:
        return True
    else:
        return False

#testing the program
print(integer_number(0))
print(integer_number(100))
print(integer_number(-7))
Print()


# 2.Write a function that has a single string as its parameter, and returns the number of
# uppercase letters, and the number of lowercase letters in the string. Test the
# function with a short program.

def count_upper_lower(string):
    upper_count = 0
    lower_count = 0

    for char in string:
        if char.isupper():
            upper_count += 1
       
        elif char.islower():
            lower_count += 1

   
    return upper_count, lower_count


input_string = "Hello World!This is a  weekly task."
upper_count, lower_count = count_upper_lower(input_string)

print(f"Uppercase letters: {upper_count}")
print(f"Lowercase letters: {lower_count}")
print()

# 3.Modify your "greetings" program so that the first letter of the name entered is
# always in uppercase with the rest in lowercase. This should happen even if the user
# entered their name differently. So if the user entered arthur, ARTHUR, or even
# arTHur the name should be displayed as Arthur.


def greet(name):
    print(f"Hello, {name}!")

name = input("Please enter your name: ").title()
greet(name)
print()

# 4.When processing data it is often useful to remove the last character from some
# input (it is often a newline). Write and test a function that takes a string parameter
# and returns it with the last character removed. (If the string contains one or fewer
# characters, return it unchanged.)



def remove_char(s):
    if len(s) > 1:
        return s[:-1]
    else:
        return s

# Testing
print(remove_char("Hello, world!")) 
print(remove_char("Krisha"))              
print(remove_char(""))   
print()


# 5.Write and test a function that converts a temperature measured in degrees
# centigrade into the equivalent in fahrenheit, and another that does the reverse
# conversion. Test both functions.


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius        

print(celsius_to_fahrenheit(100))      
print(fahrenheit_to_celsius(77))        
print(fahrenheit_to_celsius(189)) 
print(celsius_to_fahrenheit(-10))       
print()


# 6.Write a program that takes a centigrade temperature and displays the equivalent in
# fahrenheit. The input should be a number followed by a letter C. The output should
# be in the same format.


def celsius_to_fahrenheit(temp):
    c = float(temp[:-1])
    f = c * 9.0 / 5.0 + 32
    return f"{f:.2f}F"

temp = input("Enter the temperature in centigrade : ")
if temp[-1].upper() == 'C':
    print(celsius_to_fahrenheit(temp))
else:
    print("Invalid input. Please enter a number followed by a letter C.")
print()

# 7.Write a program that reads 6 temperatures (in the same format as before), and
# displays the maximum, minimum, and mean of the values.


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    temperatures = []

    for i in range(6):
        input_str = input(f"Enter temperature {i+1} in Celsius:")

        try:
            celsius_temperature = float(input_str[:-1])
        except ValueError:
            print(f"Invalid input for temperature {i+1}. Please enter a valid temperature followed by 'C'.")
            return

        temperatures.append(celsius_temperature)

  
    fahrenheit_temperatures = [celsius_to_fahrenheit(temp) for temp in temperatures]

 
    max_temperature = max(fahrenheit_temperatures)
    min_temperature = min(fahrenheit_temperatures)
    mean_temperature = sum(fahrenheit_temperatures) / len(fahrenheit_temperatures)

    # Display the results
    print(f"Maximum temperature: {max_temperature:.2f}F")
    print(f"Minimum temperature: {min_temperature:.2f}F")
    print(f"Mean temperature: {mean_temperature:.2f}F")

if __name__ == "__main__":
    main()
print()

# 8.Modify the previous program so that it can process any number of values. The input
# terminates when the user just pressed "Enter" at the prompt rather than entering a
# value.



def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    temperatures = []

    while True:
        input_str = input("Enter a temperature in Celsius (or press Enter to finish): ")

        if not input_str:
            break

        try:
            celsius_temperature = float(input_str[:-1])
        except ValueError:
            print("Invalid input. Please enter a valid temperature followed by 'C' or press Enter to finish.")
            continue

        temperatures.append(celsius_temperature)

    if not temperatures:
        print("No temperatures entered.")
        return

    # Convert all temperatures to Fahrenheit
    fahrenheit_temperatures = [celsius_to_fahrenheit(temp) for temp in temperatures]

    # Calculate maximum, minimum, and mean
    max_temperature = max(fahrenheit_temperatures)
    min_temperature = min(fahrenheit_temperatures)
    mean_temperature = sum(fahrenheit_temperatures) / len(fahrenheit_temperatures)

    
    print(f"Maximum temperature: {max_temperature:.2f}F")
    print(f"Minimum temperature: {min_temperature:.2f}F")
    print(f"Mean temperature: {mean_temperature:.2f}F")

if __name__ == "__main__":
    main()

