#Measure Time
import time

#The main mergesort algorithm to compare one array to another
def mergesortA(A,start, middle, end):
  #Posistion of left array from start to mid point
  left=middle-start+1
  #Posistion of right array from mid to  end point
  right=end-middle;

#Create a copy of left and right array
  leftarray=[]
  rightarray=[]
  tmp=0
  tmp1=0
  while(tmp<left):
    leftarray.append(A[tmp+start])
    tmp+=1
  while(tmp1<right):
    rightarray.append(A[middle+tmp1+1])
    tmp1+=1
    

  #Start to compare the first interger within each array, and store into the orginal array. Repeats untill one array is empty
  index1=0
  index2=0
  index3=start
  while index1<left and index2<right:
    if(leftarray[index1]<rightarray[index2]):
      A[index3]=leftarray[index1]
      index3+=1
      index1+=1
    else:
      A[index3]=rightarray[index2]
      index2+=1
      index3+=1
#Copy the reminder of the empty array back into the orginal
  while index1 < left:
    A[index3]=leftarray[index1]
    index1+=1
    index3+=1

  while index2 < right:
    A[index3]=rightarray[index2]
    index2+=1
    index3+=1
  return
  
  
def mergesort(A,start,end):

  if start < end:#Return, if the array size(end-begin) is less than 2
    middle = (start+(end-1))//2#Divides the array into half, with mid as the pivot point
    mergesort(A, start, middle)  #Divide the left array again
    mergesort(A, middle+1, end)#Divide the right array again
    mergesortA(A, start,middle, end)#Conduct MergeSort


# Array needed to be sorted
arr=[463, 627, 62, 616, 997, 958, -294, -721, 178, -552, -65, -998, 209, 174, -309, 311, 242, -730, 980, -609, -540, 991, -835, -970, -252, -514, 788, 310, 423, -267, 68, -784, 55, 115, 829, 585, 764, -985, 516, -482, -915, -935, -31, 886, -547, 720, -677, -494, 351, -685, 952, 842, 629, 654, 79, 474, -64, 488, 996, -661, -446, -341, -869, 530, 831, 120, 899, 552, 840, 353, 69, -326, 389, 8, 694, -602, -42, 950, 626, -322, 494, -371, 727, 885, -132, -333, -191, 13, 277, -630, -971, 978, -77, 138, -555, -270, -107, 709, -477, 319
]

#Start to measure time take
start = time.time_ns()
n=len(arr)
mergesort(arr,0,n-1)

#Stop measure time taken + print out the result in nanoseconds
end = time.time_ns()-start
print(end)
print("ns")

#printing out the sorted array to confirme the algorithm worked
print("The Sorted-Array is: ", arr) 
