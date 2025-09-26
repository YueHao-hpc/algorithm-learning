#include <iostream>
#include <vector>
using namespace std;

class SelectBubbleInsert {
public:
    // Swap elements at positions i and j in the array
    static void swap(vector<int>& arr, int i, int j) {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

    // Selection Sort
    // Repeatedly find the minimum element and place it at the beginning
    static void selectionSort(vector<int>& arr) {
        if (arr.size() < 2) return;

        for (int i = 0; i < arr.size() - 1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < arr.size(); j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }
            swap(arr, i, minIndex);
        }
    }

    // Bubble Sort
    // Repeatedly swap adjacent elements if they are in the wrong order
    static void bubbleSort(vector<int>& arr) {
        if (arr.size() < 2) return;

        for (int end = arr.size() - 1; end > 0; end--) {
            for (int i = 0; i < end; i++) {
                if (arr[i] > arr[i + 1]) {
                    swap(arr, i, i + 1);
                }
            }
        }
    }

    // Insertion Sort
    // Build a sorted portion of the array one element at a time
    static void insertionSort(vector<int>& arr) {
        if (arr.size() < 2) return;

        for (int i = 1; i < arr.size(); i++) {
            for (int j = i - 1; j >= 0 && arr[j] > arr[j + 1]; j--) {
                swap(arr, j, j + 1);
            }
        }
    }
};