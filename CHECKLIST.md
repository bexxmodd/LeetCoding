# Sorting Algorithms

**InsertionSort(A)**

$n \leftarrow A.length$;
$\\\quad$ $for$ $i \leftarrow$ $0..n - 1$
$\\\qquad$ $value \leftarrow A[i]$;
$\\\qquad$ $hole \leftarrow i$;
$\\\quad$ $while$ $hole > 0$ $and$ $A[hole - 1] > value$
$\\\qquad$ $A[hole] \leftarrow A[hole - 1]$;
$\\\qquad$ $hole \leftarrow hole - 1$;
$\\\quad$ $A[hole] \leftarrow value$;


-------------------
**BubbleSort(A)**

$n \leftarrow A.length$;
$\\$ $for$ $i \leftarrow$ $0..n - 1$;
$\\\quad$ $flag \leftarrow 0$;
$\\\quad$ $for$ $j \leftarrow$ $0..n - 2 - i$;
$\\\qquad$ $if A[i] > A[j + 1]$
$\\\qquad\quad$ $swap(A[j], A[j + 1])$;
$\\\qquad\quad$ $flag \leftarrow 1$;
$\\\quad$ $if$ $\neg flag$ $break$;

-------------------
3 - Merge Sort

-------------------
4 - Quick Sort
