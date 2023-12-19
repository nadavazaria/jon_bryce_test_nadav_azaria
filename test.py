from tools.numbers.simp import *
from tools.numbers.comp import *
from tools.col import my_zip,my_zip1 
from icecream import ic





def main(): 

# check if i can call comp befire first calling simp 
    sum_digits(456)
    add_2_nums(2,3)
    sum_dig = sum_digits(456)
    ic(sum_dig)
    sum_digits(123)
# check simp
    sum1 = sub_2_nums(2,1)
    ic (sum1)
# expected 1
    sum2 = add_2_nums(4,5)
    ic(sum2) 
# expected 9
    
# check comp
    sum_dig = sum_digits(456)
    ic(sum_dig)
# expected 15

    pal = is_pal(12321)
    ic(pal)
# expected True
    pal2 = is_pal(4563210)
    ic(pal2)
# expected False



    # check zip
    it1 =[1,2,3,4]
    it2 =['a','b','c','d']
    it3 =['a','b','c','d','e']
    output_list = my_zip(it1,it2)

    ic(output_list)
    output_list = my_zip(it1,it3)
    # expected error note because the lists are of t=different sizes
if __name__ == "__main__":
    main()
