\# Experiment 2: Binary Search Logarithmic Analysis



\## Aim

To verify the logarithmic behavior of Binary Search.



\## Algorithm

1\. Find the middle element.

2\. Compare with target.

3\. Search left half or right half.

4\. Repeat until found.



\## Experimental Observation



| Dataset Size | Iterations |

|-------------|-----------|

| 8 | 3 |

| 16 | 4 |

| 32 | 5 |

| 64 | 6 |

| 128 | 7 |



\## Time Complexity



Best Case: O(1)



Average Case: O(log n)



Worst Case: O(log n)



\## Space Complexity



O(1)



\## Interpretation



The number of iterations increases very slowly as the dataset size grows.



Each step eliminates half of the remaining elements.



This demonstrates logarithmic growth.



\## Conclusion



Binary Search is significantly more efficient than Linear Search for large sorted datasets because it reduces the search space by half at each iteration.

