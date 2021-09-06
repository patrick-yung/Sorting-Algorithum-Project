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
  int leftnode=parent*2+1;
  int rightnode=parent*2+2;

  //Check if Left child is larger than parent//
  if(leftnode<n && A[leftnode]> A[parent]){
    tmp=leftnode;
  }else{
    tmp=parent;
  }

  //Check if right child is larger than left child or parent//
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
  for (int size=n/2-1; size>=0; size--){
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
int A[] = {573, -187, -400, -356, -100, 440, 355, -116, -9, 229, -5, 969, -179, 894, -664, 205, -753, -132, 271, 441, 976, -931, -67, -247, -382, 889, 496, -487, -998, -154, -573, 864, 962, -572, -676, -534, 478, -691, -555, -386, -868, -766, -660, 197, 742, 933, -943, 887, -201, -898, 971, -607, -260, 40, -148, 353, -449, 93, 52, -548, 174, 250, 96, -174, -231, 233, 286, 70, -372, -960, 358, 22, -981, -554, -562, 558, 746, 490, -621, -822, -86, 696, -642, -93, -873, 411, 619, -926, 780, -203, 420, -553, -523, -447, -68, 786, 645, 674, -383, 448};

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
