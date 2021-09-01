import time #Measure Time
import math #to round down to find mid point

#Moving all integers smaller than the pivot on the left, and larger on the right
def quickSortB(A,start,end):
  middle = math.floor(start+(end-start)/2)
  pivot = A[middle]
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
arr=[463, 627, 62, 616, 997, 958, -294, -721, 178, -552, -65, -998, 209, 174, -309, 311, 242, -730, 980, -609, -540, 991, -835, -970, -252, -514, 788, 310, 423, -267, 68, -784, 55, 115, 829, 585, 764, -985, 516, -482, -915, -935, -31, 886, -547, 720, -677, -494, 351, -685, 952, 842, 629, 654, 79, 474, -64, 488, 996, -661, -446, -341, -869, 530, 831, 120, 899, 552, 840, 353, 69, -326, 389, 8, 694, -602, -42, 950, 626, -322, 494, -371, 727, 885, -132, -333, -191, 13, 277, -630, -971, 978, -77, 138, -555, -270, -107, 709, -477, 319
]
#Start to measure time take
start = time.time_ns()
n=len(arr)
quickSort(arr,0,n-1)

#Stop measure time taken + print out the result in nanoseconds
end = time.time_ns()-start
print(str(end)+' ns')

#printing out the sorted array to confirme the algorithm worked
print("The Sorted-Array is: ", arr) 

