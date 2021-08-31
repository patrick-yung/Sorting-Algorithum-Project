#include <iostream>
#include <chrono>//To measure Time//
#include <unistd.h>//To measure Time//
using namespace std;

void printArray(int A[], int size)//To print the Sorted array//
{
  for (auto i = 0; i < size; i++){
    cout << A[i] << " ";}
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
  while (index1 < left && index2 < right) {
    if (leftArray[index1] <= rightArray[index2]) {
      A[first] = leftArray[index1];
      index1++;
    }else{
      A[first] = rightArray[index2];
      index2++;
    }
    first++;
  }

//Copy the reminder of the empty array back into the orginal//
  while (index1 < left) {
    A[first] = leftArray[index1];
    index1++;
    first++;
  }
  while (index2 < right) {
    A[first] = rightArray[index2];
    index2++;
    first++;
  }  
}

void mergeSort(int array[], int const begin, int const end)
{
  if (begin >= end){//Return, if the array size(end-begin) is less than 2//
    return;}
 
  auto mid = begin + (end-begin)/2;//Divides the array into half, with mid as the pivot point// 
  mergeSort(array, begin, mid);//Divide the left array again//
  mergeSort(array, mid + 1, end);//Divide the right array again//
  mergesortA(array, begin, mid, end);//Conduct MergeSort//
}

int main() {
  //Array needed to be sorted//
  int arr[] = {};
  
  //Start to measure time taken//
  auto start = chrono::steady_clock::now();

  //The mergesort algorithm//
  auto arr_size = sizeof(arr) / sizeof(arr[0]);
  mergeSort(arr, 0, arr_size - 1);

  //Stop measure time taken + print out the result in nanoseconds//
  auto end = chrono::steady_clock::now();
  cout << "Elapsed time in nanoseconds: "<< chrono::duration_cast<chrono::nanoseconds>(end - start).count()<< " ns" << endl;

 //printing out the sorted array to confirme the algorithm worked//
  cout << "\nSorted array is \n";
  printArray(arr, arr_size);

}
