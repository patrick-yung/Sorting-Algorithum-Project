import time #Measure Time
import random #For random number generate

#Moving all integers smaller than the pivot on the left, and larger on the right
def quickSortB(A,start,end):
  randpivot = random.randrange(start, end)
  pivot = A[randpivot]
  i = start
  j = end
  while(i<j):
    #move left position untill larger
    while(A[i]<pivot):
       i+=1
    #move right position untill smaller
    while(A[j]> pivot):
      j-=1
    #Perform Swap
    A[i],A[j]=A[j],A[i]
  return j;



def quickSort(A,start,end):
  #Perform quickSort on mid, so mid in right position
  if (end>start):
    mid=quickSortB(A,start,end)
    #Repeat on left and right array
    quickSort(A,start,mid-1)
    quickSort(A,mid+1,end)


#Array input
arr=[
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100

]
#Start to measure time take
start = time.time_ns()
n=len(arr)
quickSort(arr,0,n-1)

#Stop measure time taken + print out the result in nanoseconds
end = time.time_ns()-start
print(end)
print("ns")

#printing out the sorted array to confirme the algorithm worked
print("The Sorted-Array is: ", arr) 

