# the function recieves two lists and reurns a list of dictionaries 
def my_zip(it1,it2):
    # i check if the lists are of the same size 
    if(len(it1)!= len(it2)):
        "if not i print an error for the user"
        print("cannot zip items of differnt lengths")
        return ''
    else:
        # i create an empty list that will be the finished output  
        output = []
        for par in it1:
            # i iterate over the list and create an int that indicates the number of the parameter 
            i = 0
            # adding the parameter from list1 and list2 to the output
            output.append({par:it2[i]})
            # plus the iteration number
            i += 1  

        return output
def my_zip1(it1,it2):
    return list(zip(it1,it2))
