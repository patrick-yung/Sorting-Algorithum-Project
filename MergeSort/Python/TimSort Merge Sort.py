#Measure Time
import time

#Tim Sort requirement
KEY=7

#Tim's Sort insertion search on value on array(left to right)
def insertionsort(A, left,right,value):
  #Performe insertion sort untill array is sorted
  if(right>=left):
    #Divide array
    mid=left+(right-left)//2

    #Check if value is equal, less or larger than mid point of array
    if(value==A[mid]):
      return mid
    elif(A[mid]>value):
      return insertionsort(A,left,mid-1,value)
    else:
      return insertionsort(A,mid+1,right,value)

  #Return position of value
  if(A[right]<value):
    return right
  else:
    return right+1

#The main mergesort algorithm to compare one array to another
def mergesortA(A,start, middle, end):
  #Posistion of left and right array from mid to  end point
  left=middle-start+1
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
    

  #Perform comparison untill left or right array is empty
  index1=0
  index2=0
  index3=start
  key1=0
  key2=0
  while index1<left and index2<right:
    if(leftarray[index1]<rightarray[index2]):
      A[index3]=leftarray[index1]
      index3+=1
      index1+=1
      key1+=1
      key2=0
      
    else:
      A[index3]=rightarray[index2]
      index2+=1
      index3+=1
      key1=0
      key2+=1

    #Check if condition is meet for tim-sort
    if(key1>=KEY):
      key1=0;
      #Perform insertion sort 
      tmp=insertionsort(leftarray,index1+1,left-1,rightarray[index2])

      #Copy array untill result from insertion sort
      while (index1+1 < tmp):
        A[index3]=leftarray[index1]
        index3+=1
        index1+=1

    elif(key2>=KEY):
      key2=0;
      #Perform insertion sort 
      tmp=insertionsort(rightarray,index2+1,right-1,leftarray[index1])
      #Copy array untill result from insertion sort
      while (index2+1 < tmp):
        A[index3]=rightarray[index2]
        index3+=1
        index2+=1

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
  if start < end:
    middle = (start+(end-1))//2
    mergesort(A, start, middle)
    mergesort(A, middle+1, end)
    mergesortA(A, start,middle, end)

    
arr=[573, -187, -400, -356, -100, 440, 355, -116, -9, 229, -5, 969, -179, 894, -664, 205, -753, -132, 271, 441, 976, -931, -67, -247, -382, 889, 496, -487, -998, -154, -573, 864, 962, -572, -676, -534, 478, -691, -555, -386, -868, -766, -660, 197, 742, 933, -943, 887, -201, -898, 971, -607, -260, 40, -148, 353, -449, 93, 52, -548, 174, 250, 96, -174, -231, 233, 286, 70, -372, -960, 358, 22, -981, -554, -562, 558, 746, 490, -621, -822, -86, 696, -642, -93, -873, 411, 619, -926, 780, -203, 420, -553, -523, -447, -68, 786, 645, 674, -383, 448
]

start = time.time_ns()
n=len(arr)
mergesort(arr,0,n-1)
end = time.time_ns()-start
print(end)
print("ns")
print("The Sorted-Array is: ", arr) 
