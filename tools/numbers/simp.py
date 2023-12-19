
module_used = {"finished totorial": False}

def add_2_nums(num1,num2):
    global module_used
    module_used["finished totorial"] = True        
    return num1 + num2

def sub_2_nums(num1,num2):
    global module_used
    module_used["finished totorial"] = True
    return num1 - num2