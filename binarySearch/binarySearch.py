import time
import random
def binarySearch(arr,start,end,ele):
    mid=(start+end)//2
    if(start>end):
        return("Element not found")
    if(ele==arr[mid]):
        return(f"Element found at {mid} position")
    if(ele>arr[mid]):
        return binarySearch(arr,mid+1,end,ele)
    if(ele<arr[mid]):
        return binarySearch(arr,start,mid-1,ele)
def linearSearch(arr,ele):
    i=-1
    for k in arr:
        i+=1
        if(k==ele):
            return (f"Element found at {i} position")
    return("Element not found")

arr=[random.randint(1, 100000) for _ in range(10000)]
arr.append(89420)
arr=sorted(arr)
start=time.time()
print(binarySearch(arr,0,len(arr)-1,89420))
end=time.time()
print(end-start)
#tests algo for when element is not present
start=time.time()
print(linearSearch(arr,89420))
end=time.time()
print(end-start)