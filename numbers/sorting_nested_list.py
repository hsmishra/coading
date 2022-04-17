"""
Sort any list, according to the second element of the sublist present within the main list.
Note: Here there are 3 methods
"""

#Using the Bubble Sort technique

def sort_list_using_bubble_sort(lst):
    l = len(lst) 
    for i in range(0, l): 
        for j in range(0, l-i-1): 
            if (lst[j][1] > lst[j + 1][1]): 
                tempo = lst[j] 
                lst[j]= lst[j + 1] 
                lst[j + 1]= tempo 
    return lst 


#Using sort() method
def sort_list_using_sort(lst):
    """
    The sort() method sorts the list ascending by default.
    While sorting via this method the actual content of the tuple is changed
    """
    lst.sort(key=lambda x:x[1])
    return lst

#Using sorted method
def sort_list_using_sorted(lst):
    """
    Sorted() sorts a list and always returns a list with the elements in a sorted manner
    ,without modifying the original sequence. It takes three parameters from which two are,
    optional, here we tried to use all of the three.
    """
    return sorted(lst, key=lambda x:x[1])

    
student = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
print(sort_list_using_bubble_sort(student))
