import random
A=sorted([random.randint(0,20) for i in range(10)])

def binary_search_iter(arr,num_to_search):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=(start+end)//2
        if num_to_search==arr[mid]:
            return "{} found at index: {}".format(num_to_search,mid)
        elif num_to_search<arr[mid]:
            end=mid-1
        else:
            start=mid+1
    return "{} not found in the given list".format(num_to_search)

num_to_search=random.randint(0,20)
print(A,num_to_search)
print(binary_search_iter(A,num_to_search))

def binary_search_recur(arr,num_to_search,start,end):
    mid=(start+end)//2
    if start>end:
        return "{} not found in the given list".format(num_to_search)
    else:
        if num_to_search==arr[mid]:
            return "{} found at index: {}".format(num_to_search,mid)
        elif num_to_search<arr[mid]:
            end=mid-1
            return binary_search_recur(arr,num_to_search,start,end)
        else:
            start=mid+1
            return binary_search_recur(arr,num_to_search,start,end)

print(binary_search_recur(A,num_to_search,0,9))
