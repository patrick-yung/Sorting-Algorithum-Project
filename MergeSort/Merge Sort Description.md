MergeSort focus on dividing an unsorted array of integers into two sets, and is repeated until the size of the sets are two or less. Afterwards, the set begins to merge together by comparing the smallest integers in each sets. 

TimSort is an additional feature that takes in a consideration that one set would more likely include a larger integer than th eaverage in one sub array compared to the other sub array. Then, it would switch to insertion sort to find the next position before resuming the original merge sort algorithm. 

Insertion Merge Sort is a combination of insertion sort and binary similar to Tim-sort, but perform insertion sort if meet KEY requirement(KEY is current set for array size less or equal to 7). Else it would perform normal merge sort

Bitonic Sort is unqiue as it perform swap rather than creating an array, but require the array size to be equal to power of two to ensure all sub array could be divided equally. Hence, a log function is used to obtain the sub array size.

Each algorithum besides tim sort, has two main function (mergesort and MergesortA). mergesort choose the size of the array to perform merge sort, and mergesortA perform the merge sort action.
