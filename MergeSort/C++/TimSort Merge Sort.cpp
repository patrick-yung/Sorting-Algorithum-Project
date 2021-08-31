#include <iostream>
using namespace std;
#include <chrono>
#include <unistd.h>

const int KEY=7;//Requirement for Tim-Sort//

void printArray(int A[], int size){//Print Array//
  for (auto i = 0; i < size; i++){
    cout << A[i] << " ";}
}

int insertionsort(int A[], int left, int right, int value){//perform insertion sort/binary sort on value//
  if(right>=left){
    int mid = left + (right - left) / 2;//Divide array//
    if(A[mid]==value){//Check if value is equal//
      return mid;
    }
    if(A[mid]>value){
      //repeat on left if smaller than mid value//
      return insertionsort(A, left, mid-1, value);
    }else{
      //repeat on right if larger than mid value//
      return insertionsort(A, mid+1, right, value);
      
    }
  }
  //Return location//
  if(A[right]<value){
    return right;
  }else{
    return right+1;
  }
  
  return -1;
}

void mergesortA(int A[], int const start, int const mid, int const end)//The main mergesort algorithm to compare one array to another//
{
  int left=mid-start+1;//position of start of left array//
  int right=end-mid;//position of start of right array//

//Create a copy of left array and right array//
 auto *leftArray = new int[left],
      *rightArray = new int[right];

  for(int tmp=0; tmp<left;tmp++){
    leftArray[tmp]=A[tmp+start];
  }
  for(int tmp=0; tmp<right;tmp++){
    rightArray[tmp]=A[tmp+1+mid];
  }

//Start to compare the first interger within each array, and store into the orginal array. Repeats untill one array is empty//
  auto index1=0,index2=0;
  int first=start;
  int leftcount=0;
  int rightcount=0;

  while (index1 < left && index2 < right) {
    if (leftArray[index1] <= rightArray[index2]) {
      rightcount=0;
      A[first] = leftArray[index1];
      index1++;
      leftcount++;
      first++;
      }
    else {
      leftcount=0;
      A[first] = rightArray[index2];
      index2++;
      rightcount++;
      first++;
      }
    //check if condition is meet to perform binary search//
    if(leftcount==KEY){
      int tmp=insertionsort(leftArray,index1,left,rightArray[index2]);
      while(index1+1<tmp){
        A[first] = leftArray[index1];
        index1++;
        first++;
      }
    A[first]=rightArray[index2];
    first++;
    index2++;
    leftcount=0;

    }else if (rightcount==KEY){
      int tmp=insertionsort(rightArray,index1,right,leftArray[index1]);

      while(index2+1<tmp){
        A[first] = rightArray[index2];
        index2++;
        first++;
      }
    A[first]=rightArray[index1];
    first++;
    index1++;
    rightcount=0;
    }
  }
  //Copy the reminder of the empty array back into the orginal//
  while (index1 < left) {
    A[first] = leftArray[index1];
    index1++;
    first++;}

  while (index2 < right) {
    A[first] = rightArray[index2];
    index2++;
    first++;
  }  
}

void mergesortB(int A[], int start, int mid, int end){
  int left=mid-start+1;
  int right=end-mid;

  auto *leftArray= new int[left];
  auto *rightArray= new int[right];

  for(int tmp=0; tmp<left;tmp++){
    leftArray[tmp]=A[tmp+start];
  }
  for(int tmp=0; tmp<right;tmp++){
    rightArray[tmp]=A[tmp+1+mid];
  }

  auto index1=0,index2=0;
  int first=start;
  int leftcount=0;
  int rightcount=0;

  while (index1 < left && index2 < right) {
    if (leftArray[index1] <= rightArray[index2]) {
      rightcount=0;
      A[first] = leftArray[index1];
      index1++;
      leftcount++;
      first++;
      }
    else {
      leftcount=0;
      A[first] = rightArray[index2];
      index2++;
      rightcount++;
      first++;
      }
  }
  while (index1 < left) {
    A[first] = leftArray[index1];
    index1++;
    first++;}

  while (index2 < right) {
    A[first] = rightArray[index2];
    index2++;
    first++;
  }  
}

void mergeSort1(int array[], int const begin, int const end)
{
    if (begin >= end)
        return;
    auto mid = begin + (end - begin) / 2;
    mergeSort1(array, begin, mid);
    mergeSort1(array, mid + 1, end);
    if(end-begin<=KEY){
    mergesortB(array, begin, mid, end);
    }else{
    mergesortA(array, begin, mid, end);}
}


int main() {

int A[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
91, 92, 93, 94, 95, 96, 97, 98, 99, 100};


auto start = chrono::steady_clock::now();
auto arr_size = sizeof(A) / sizeof(A[0]); 

mergeSort1(A,0,arr_size-1);

auto end = chrono::steady_clock::now();

cout << "Elapsed time in nanoseconds: "
    << chrono::duration_cast<chrono::nanoseconds>(end - start).count()<< " ns" << endl;

cout << "\nSorted array is \n";
  printArray(A, arr_size);
}
