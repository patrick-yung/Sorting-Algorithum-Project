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
  int leftnode=parent*4+1;
  int leftmidnode=parent*4+2;
  int rightmidnode=parent*4+3;
  int rightnode=parent*4+4;

  //Check if Left child is larger than parent//
  if(leftnode<n && A[leftnode]> A[parent]){
    tmp=leftnode;
  }else{
    tmp=parent;
  }

  //Check if leftmiddle child is larger than left child or parent//
  if(leftmidnode<n && A[leftmidnode]> A[tmp]){
    tmp=leftmidnode;
  }

  //Check if rightmiddle child is larger than left child, leftmiddle node or parent//
  if(rightmidnode<n && A[rightmidnode]> A[tmp]){
    tmp=rightmidnode;
  }

  //Check if right child is larger than other node or parent//
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
  for (int size=n/4-1; size>=0; size--){
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
int A[] = {-648, -25, -168, -716, 885, -394, -399, 834, 184, -733, -167, 355, 597, 282, 624, 147, 234, 472, 156, 5, 828, 615, 694, 491, -994, 762, 116, -495, 135, -693, 186, -270, -564, -247, 511, 1, 392, 528, 102, -628, -786, -431, -645, -60, -968, 882, 461, 845, -472, -682, 893, -449, -300, -752, -174, 14, 581, 416, 134, 575, 217, 247, -959, -575, 3, -458, 467, -413, -954, 485, 339, 245, 289, 124, 982, -607, -678, -102, 578, -578, -711, -207, -352, -199, -303, -838, 630, -953, -187, 902, -570, 852, -613, -386, -818, -79, -749, 420, -732, 360};

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
