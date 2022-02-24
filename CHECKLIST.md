# Sorting Algorithms

${\bf InsertionSort(A)}$
$\\n \leftarrow A.length$;
$\\\quad$ $for$ $i \leftarrow$ $0..n - 1$
$\\\qquad$ $value \leftarrow A[i]$;
$\\\qquad$ $hole \leftarrow i$;
$\\\quad$ $while$ $hole > 0$ $and$ $A[hole - 1] > value$
$\\\qquad$ $A[hole] \leftarrow A[hole - 1]$;
$\\\qquad$ $hole \leftarrow hole - 1$;
$\\\quad$ $A[hole] \leftarrow value$;

</br>

-------------------
${\bf BubbleSort(A)}$
$\\n \leftarrow A.length$;
$\\$ $for$ $i \leftarrow$ $0..n - 1$;
$\\\quad$ $flag \leftarrow 0$;
$\\\quad$ $for$ $j \leftarrow$ $0..n - 2 - i$;
$\\\qquad$ $if A[i] > A[j + 1]$
$\\\qquad\quad$ $swap(A[j], A[j + 1])$;
$\\\qquad\quad$ $flag \leftarrow 1$;
$\\\quad$ $if$ $\neg flag$ $break$;

</br>

-------------------
${\bf MergeSort(A)}$
$\\n \leftarrow A.length$;
$\\ if n < 2$
$\\\quad return$
$\\ mid \leftarrow n \div 2$;
$\\ left \leftarrow A[0:mid]$;
$\\ right \leftarrow A[mid: n - 1]$;
$\\ \textit{\textbf{Merge(left, right, A)}}$;


${\bf Merge(L,R,A)}$
$\\ i \leftarrow 0$;
$\\ j \leftarrow 0$;
$\\ k \leftarrow 0$;
$\\ while$ $i < L.length$ and $j < R.length$
$\\\quad if$ $L[i] \le R[i]$
$\\\qquad A[k] \leftarrow L[i]$;
$\\\qquad i \leftarrow i + 1$;
$\\\quad else$
$\\\qquad A[k] \leftarrow R[j]$;
$\\\qquad j \leftarrow j + 1$;
$\\\quad k \leftarrow k + 1$;
$\\ while$ $i < L.length$
$\\\quad A[k] \leftarrow L[i]$;
$\\\quad i \leftarrow i + 1$;
$\\\quad k \leftarrow k + 1$;
$\\ while$ $j < R.length$
$\\\quad A[k] \leftarrow L[j]$;
$\\\quad j \leftarrow j + 1$;
$\\\quad k \leftarrow k + 1$;

</br>

-------------------

${\bf Quick Sort(A, start, end)}$
$\\ if$ $start < end$
$\\\quad pivotIndex \leftarrow \textit{\textbf{Partition}}(A, start, end)$;
$\\\quad \textit{\textbf{QuickSort}}(A, start, pivotIndex - 1)$;
$\\\quad \textit{\textbf{QuickSort}}(A, pivotIndex + 1, end)$;


${\bf Partition(A, start, end)}$
$\\ pivotValue \leftarrow A[end]$;
$\\ pivotIndex \leftarrow start$;
$\\ for$ $i \leftarrow start \ldots end - 1$
$\\\quad if$ $A[i] \le pivotValue$
$\\\qquad \textit{\textbf{Swap}}(A[i], A[pivotIndex])$;
$\\\qquad pivotIndex \leftarrow pivotIndex + 1$;
$\\ \textit{\textbf{Swap}}(A[pivotIndex], A[end])$;
