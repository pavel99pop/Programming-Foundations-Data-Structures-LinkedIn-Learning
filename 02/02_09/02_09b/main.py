import math
#using built-in sorted method -> less efficient -> O(Nlog(n))
def find_second_smallest(my_list):
    if len(my_list) < 2:
        return None
    
    sorted_list = sorted(my_list)
    return sorted_list[1]   #won't work if duplicate values in list



#using custom method -> more efficient -> O(N)
def find_second_smallest_v2(my_list):
    if len(my_list) < 2:
        return None
    
    first_smallest = math.inf
    second_smallest = math.inf

    for item in my_list:
        if item < first_smallest:
            second_smallest = first_smallest
            first_smallest = item
        elif item < second_smallest:
            second_smallest = item
    
    return second_smallest

print(find_second_smallest_v2([5, 8, 3, 2, 6]))
