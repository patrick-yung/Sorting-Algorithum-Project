#include <iostream>
#include <chrono> //To measure Time//
#include <unistd.h> //To measure Time//
using namespace std;

//Moving all integers smaller than the pivot on the left, and larger on the right//
int quickSortB(int A[], int start,int end){
  //create middle pivot point//
  int middle = start + (end - start)/2;
  int pivot = A[middle];

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
  int arr[] = {463, 627, 62, 616, 997, 958, -294, -721, 178, -552, -65, -998, 209, 174, -309, 311, 242, -730, 980, -609, -540, 991, -835, -970, -252, -514, 788, 310, 423, -267, 68, -784, 55, 115, 829, 585, 764, -985, 516, -482, -915, -935, -31, 886, -547, 720, -677, -494, 351, -685, 952, 842, 629, 654, 79, 474, -64, 488, 996, -661, -446, -341, -869, 530, 831, 120, 899, 552, 840, 353, 69, -326, 389, 8, 694, -602, -42, 950, 626, -322, 494, -371, 727, 885, -132, -333, -191, 13, 277, -630, -971, 978, -77, 138, -555, -270, -107, 709, -477, 319};

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
