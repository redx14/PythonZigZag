#Andrey Ilkiv Assignment 4 problem 3 section 01 10/12/2020


#gets amount of cols user wants
cols = int(input('How many columns? '))

#checks if cols entered is not less than or equal to 0
#if it is lower or equal to 0 ask user again for input
while(cols <= 0):
    print("Invalid Entry! Try Aagain!")
    cols = int(input('How many columns? '))
#subtracts 1 from cols to be used in loops from 0 - cols
cols = cols - 1

#prints upper part of arrow
for i in range(0 , cols):
    #adds spaces ranging from 0 - cols for each line
    for j in range(0 , i):
        print(" ", end="")
    #prints 1 * after spaces are entered
    for k in range(1 , 2):
        print("*" , end="")
    print()
#prints lower part of arrow
for i in range(0 , cols + 1):
    #adds spaces ranging from col-0 for each line
    for j in range(0 , cols - i):
        print(" " , end="")
    #prints 1 * after spaces are entered
    for k in range(1 , 2):
        print("*" , end="")
    print()
