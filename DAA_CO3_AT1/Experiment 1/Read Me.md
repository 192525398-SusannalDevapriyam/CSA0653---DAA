\# Experiment 1: Merge Sort Memory Usage Analysis



\## Aim

To implement Merge Sort and analyze its memory usage.



\## Algorithm

1\. Divide the array into two halves.

2\. Recursively sort each half.

3\. Merge the sorted halves.



\## Memory Usage Analysis



| Input Size | Auxiliary Space |

|------------|----------------|

| 10 | O(n) |

| 100 | O(n) |

| 1000 | O(n) |



Merge Sort requires additional memory for temporary arrays during merging.



\## Time Complexity

Best Case: O(n log n)



Average Case: O(n log n)



Worst Case: O(n log n)



\## Space Complexity

O(n)



\## Interpretation



Merge Sort uses additional memory but provides consistent performance.



The extra memory requirement is the trade-off for achieving efficient and stable sorting.



\## Conclusion



Merge Sort is suitable for large datasets because it guarantees O(n log n) performance, although it requires extra memory.

