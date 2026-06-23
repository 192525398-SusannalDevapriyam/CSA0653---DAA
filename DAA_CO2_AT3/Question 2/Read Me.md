\# Debugging Sequential String Matching



\## Aim

To identify and correct the loop condition error.



\## Error

The loop used range(n-m), which skipped the final alignment.



\## Correction

Changed range(n-m) to range(n-m+1).



\## Output

Pattern found successfully.



\## Worst Case Complexity

O(nm)



\## Space Complexity

O(1)

