import random
A=[random.randint(0,100) for i in range(20)]
def linear_search(arr,num_to_search):
    for i in range(len(arr)):
        if num_to_search==arr[i]:
            return num_to_search,"found at index:",i
    return num_to_search,"not found in the list"
num_to_search=random.randint(0,100)
print(A,num_to_search)
print(linear_search(A,num_to_search))
