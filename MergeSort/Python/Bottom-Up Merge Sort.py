import time

def mergesortA(A,start, middle, end):
  left=middle-start+1
  right=end-middle;

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
  C=1
  while(C<=end):
    B=0
    while(B<=end-C):
      mergesortA(A,B,B+C-1, min((B + 2*C - 1),end))
      B+=2*C
    C+=C
  
arr=[573, -187, -400, -356, -100, 440, 355, -116, -9, 229, -5, 969, -179, 894, -664, 205, -753, -132, 271, 441, 976, -931, -67, -247, -382, 889, 496, -487, -998, -154, -573, 864, 962, -572, -676, -534, 478, -691, -555, -386, -868, -766, -660, 197, 742, 933, -943, 887, -201, -898, 971, -607, -260, 40, -148, 353, -449, 93, 52, -548, 174, 250, 96, -174, -231, 233, 286, 70, -372, -960, 358, 22, -981, -554, -562, 558, 746, 490, -621, -822, -86, 696, -642, -93, -873, 411, 619, -926, 780, -203, 420, -553, -523, -447, -68, 786, 645, 674, -383, 448
]
start = time.time_ns()
n=len(arr)
mergesort(arr,0,n-1)
end = time.time_ns()-start
print(end)
print("ns")
print("The Sorted-Array is: ", arr) 


