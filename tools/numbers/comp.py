from math import floor
from tools.numbers.simp import module_used


def is_pal(num):
    if module_used["finished totorial"]:    
        num_str = str(num)
        number_of_digits = len(num_str)
        # iterate over the first half of the number digit by digit rounded down 
        # so that i include odd number of digit numbers and ignoring the middle
        num_of_iter = floor(number_of_digits/2)
        for i in range (0,num_of_iter):
            # compare the first digit to the coresponding digit at the end of the number
            if not num_str[i] == num_str[number_of_digits - (i+1)]:
                return False
        return True
    else:
        print("you must first finish the toturial")

# define a function that takes a num input
def sum_digits(num):
    # make the number into a string so i can iterate over it 
    # from simp import module_used
    if module_used["finished totorial"]:
        num_string = str(num)
        # define a variable to add the indivigual digits into 
        output = 0
        for dig in num_string:
            # parse the digit into int form so i can add it to an int
            output += int(dig)
        return output
    else:
        print("you must first finish the toturial")