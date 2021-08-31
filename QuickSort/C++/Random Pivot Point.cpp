#include <iostream>
#include <cstdlib>//For randon number generating//
#include <chrono> //To measure Time//
#include <unistd.h> //To measure Time//
using namespace std;

//Moving all integers smaller than the pivot on the left, and larger on the right//
int quickSortB(int A[], int start,int end){
  srand(time(NULL));
  int random = start + rand() % (end - start);

  int pivot = A[random];
  int i = start;
  int j = end;
 
  while(i<j){
    while(A[i]<pivot){//move left position untill larger//
       i++;
    }
    while(A[j]> pivot){//move right position untill smaller//
      j--;
    }
    swap(A[i], A[j]);//Perform Swap//
  }
  return j;
}


void quickSort(int A[], int start, int end){

  if (end>start){
    //Perform quickSort on mid, so mid in right position//
    int mid=quickSortB( A, start, end);
    //Repeat on left and right array//
    quickSort(A, start, mid-1);
    quickSort(A, mid+1, end);
  }
}



//Print Array out//
void printArray(int A[], int size)
{
    int i;
    for (i = 0; i < size; i++){
        printf("%d ", A[i]);}
    printf("\n");
}
 


int main() {
  //Array input//
  int arr[] = {};

  //Start to measure time taken//
  auto start = chrono::steady_clock::now();

  //Perform quickSort//
  int n = sizeof(arr) / sizeof(arr[0]);
  quickSort(arr, 0, n - 1);


  //Stop measure time taken + print out the result in nanoseconds//
  auto end = chrono::steady_clock::now();
  cout << "Elapsed time in nanoseconds: "<< chrono::duration_cast<chrono::nanoseconds>(end - start).count()<< " ns" << endl;

  //Print array out//
  printf("Sorted array: \n");
  printArray(arr, n);
}
