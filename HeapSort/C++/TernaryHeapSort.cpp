#include <iostream>
using namespace std;

//To measure running time//
#include <chrono>
#include <unistd.h>

void printArray(int A[], int size){//Print Array//
  for (auto i = 0; i < size; i++){
    cout << A[i] << " ";}
}


//Part A: Check if parent is the largest among its children//
void HeapSortA(int A[],int n, int parent){
  int tmp;
  //Calculating the child position//
  int leftnode=parent*3+1;
  int middlenode=parent*3+2;
  int rightnode=parent*3+3;

  //Check if Left child is larger than parent//
  if(leftnode<n && A[leftnode]> A[parent]){
    tmp=leftnode;
  }else{
    tmp=parent;
  }

  //Check if middle child is larger than left child or parent//
  if(middlenode<n && A[middlenode]> A[tmp]){
    tmp=middlenode;
  }

  //Check if right child is larger than left, middle child or parent//
  if(rightnode<n && A[rightnode]> A[tmp]){
    tmp=rightnode;
  }

  //Perform swap and repeat for swaped element to acheive balance heap binary tree again//
  if(tmp!=parent){
    swap(A[parent],A[tmp]);
    HeapSortA(A,n,tmp);
  }
}


void HeapSort(int A[],int n){

  //Part A: Heapify//
  for (int size=n/3-1; size>=0; size--){
    HeapSortA(A,n,size);
  }


  //Part B: Removing and rebalancing//
  for(int last=n-1; last>0; last--){
    swap(A[0],A[last]);
    HeapSortA(A,last,0);
  }

}



int main() {
//Data Set//
int A[] = {100, 99, 98, 97, 96, 95, 94, 93, 92, 91,90, 89, 88, 87, 86, 85, 84, 83, 82, 81,80, 79, 78, 77, 76, 75, 74, 73, 72, 71,70, 69, 68, 67, 66, 65, 64, 63, 62, 61,60, 59, 58, 57, 56, 55, 54, 53, 52, 51,50, 49, 48, 47, 46, 45, 44, 43, 42, 41,40, 39, 38, 37, 36, 35, 34, 33, 32, 31,30, 29, 28, 27, 26, 25, 24, 23, 22, 21,20, 19, 18, 17, 16, 15, 14, 13, 12, 11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1};

//Start the stopwatch//
auto start = chrono::steady_clock::now();
auto arr_size = sizeof(A) / sizeof(A[0]); 

//Sorting function//
HeapSort(A,arr_size);

//Stop the stopwatch
auto end = chrono::steady_clock::now();

cout << "Elapsed time in nanoseconds: "
    << chrono::duration_cast<chrono::nanoseconds>(end - start).count()<< " ns" << endl;

//Print out array//
cout << "\nSorted array is \n";
  printArray(A, arr_size);
}
