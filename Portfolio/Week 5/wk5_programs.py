
#1.Using command-line arguments involves the sys module. Review the docs for this module and using the information in there write a short program that when run from the command-line reports what operating system platform is being used

import sys
print()
print("the OS platform being used is:",sys.platform)
print()


#2.Write a program that, when run from the command line, reports how many arguments were provided. (Remember that the program name itself is not an argument).

import sys
print("the number of arguments are:",len(sys.argv))
print()


#3.Write a program that takes a bunch of command-line arguments, and then prints out the shortest.
# If there is more than one of the shortest length, any will do. 
#Hint: Don't overthink this. A good way to find the shortest is just to sort them.

import sys
arg=sys.argv.sort(key=len)
print("the shortest argument is",arg)
print()


#4.Last week you wrote a program that processed a collection of temperature readings entered by the user and 
#displayed the maximum, minimum, and mean. Create a version of that program that takes the values from the command-line instead.
# Be sure to handle the case where no arguments are provided!

import sys

temperatures = [float(arg) for arg in sys.argv[1:]]
if not temperatures:
    print("No temperature provided")
    sys.exit(1)
    
max_temp = max(temperatures)
min_temp = min(temperatures)
mean_temp = sum(temperatures) / len(temperatures)
print(f'Maximum temperature: {max_temp:.2f}')
print(f'Minimum temperature: {min_temp:.2f}')
print(f'Mean temperature: {mean_temp:.2f}')
print()


#5.Write a program that takes the name of a file as a command-line argument, and creates a backup copy of that file. 
#The backup should contain an exact copy of the contents of the original and should, obviously, have a different name.

import sys

filename = sys.argv[1]

shutil.copy(filename, filename + '.bak')

print(f'Backup copy of {filename} created as {filename}.bak')
print()
