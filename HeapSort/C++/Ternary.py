
import time #To measure time#

#Heapifying Process#
def HeapsortA(A, n, parent):

  #Create number of nodes#
  leftnode=parent*3+1
  middlenode=parent*3+2
  rightnode=parent*3+3


  #Check if left node is larger than parent#
  if leftnode<n and A[leftnode]> A[parent]:
    tmp=leftnode
  else:
    tmp=parent

  #Check if middle node is larger than parent and left node#
  if(middlenode<n and A[middlenode]> A[tmp]):
    tmp=middlenode
  
  #Check if right node is larger than parent, right and left node#
  if(rightnode<n and A[rightnode]> A[tmp]):
    tmp=rightnode


  #If either children is larger, perform swap and rebalance with swap parent#
  if(tmp != parent):
    A[parent], A[tmp] = A[tmp], A[parent]
    HeapsortA(A,n,tmp)


#Structure of Heap Sort#
def Heapsort(A, n):

  #Calculate half the element of the array#
  size=n//3-1

  #Part A: Heapify#
  for size in range(size, -1, -1):
    HeapsortA(A, n, size)
 
 #Part B: Removing each element and rebalancing#
  for last in range(n-1, 0, -1):
    arr[last], arr[0] = arr[0], arr[last] 
    HeapsortA(A, last, 0)


 #The data set# 
arr=[573, -187, -400, -356, -100, 440, 355, -116, -9, 229, -5, 969, -179, 894, -664, 205, -753, -132, 271, 441, 976, -931, -67, -247, -382, 889, 496, -487, -998, -154, -573, 864, 962, -572, -676, -534, 478, -691, -555, -386, -868, -766, -660, 197, 742, 933, -943, 887, -201, -898, 971, -607, -260, 40, -148, 353, -449, 93, 52, -548, 174, 250, 96, -174, -231, 233, 286, 70, -372, -960, 358, 22, -981, -554, -562, 558, 746, 490, -621, -822, -86, 696, -642, -93, -873, 411, 619, -926, 780, -203, 420, -553, -523, -447, -68, 786, 645, 674, -383, 448

]

#Start stopwatch#
start = time.time_ns()
n=len(arr)
Heapsort(arr,n)

#Stop the stopwatch#
end = time.time_ns()-start

#Print array to confirm#
print(end)
print("ns")
print("The Sorted-Array is: ", arr) 

