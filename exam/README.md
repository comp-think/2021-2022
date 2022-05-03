# Written examinations (with keys)

In this page it is possible to find the link to the various written examination of the course Computational Thinking and Programming, academic year 2021/2022.


## 14 March 2022 written examination

**Text of the exam:** [PDF](./written-examination-2022-03-14.pdf)

**Solutions:**
* Section 1 (theory):
  1. Python is a high-level programming language
     
     Assembly is a low-level programming language
     
  2. [Solution](https://comp-think.github.io/exercises/understanding/beginner/exercise-14) available online.
     
  3. [Solution](https://comp-think.github.io/exercises/development/beginner/exercise-25) available online.
  
  4. The approach for finding a solution to this computational problem is based entirely on backtracking. In particular, we should develop it according to the following steps:
     * [leaf-win] if the last move has brought to a situation where there is only one peg, and it is in the central position, then a solution has been found, and the sequence of moves executed for coming to this solution is returned; otherwise,
     * [leaf-lose] if the last move has brought to a situation where there are no possible moves, then recreate the previous status of the board as if we did not execute the previous move, and return no solutions; otherwise,
     * [recursive-step] apply the algorithm recursively for each possible valid move executable according to the board’s current status until one of these recursive executions of the algorithm returns a solution. If none of them provides a solution, recreate the previous status of the board as if we did not execute the last move and return no solutions.

* Section 2 (understanding): [Solution](https://comp-think.github.io/exercises/understanding/advanced/exercise-28) available online.

* Section 3 (development): [Solution](https://comp-think.github.io/exercises/development/advanced/exercise-28) available online.


## 28 January 2022 written examination

**Text of the exam:** [PDF](./written-examination-2022-01-28.pdf)

**Solutions:**
* Section 1 (theory):
  1. 2
     
     8
     
  2. [Solution](https://comp-think.github.io/exercises/understanding/beginner/exercise-13) available online.
     
  3. [Solution](https://comp-think.github.io/exercises/development/beginner/exercise-24) available online.
  
  4. The merge sort is an algorithm using a divide a conquer approach for addressing the computational problem sorting all the items in a given list. The steps composing the algorithm can be summarised as follows:
  
  * [base case] if the input list has only one item, return the list as it is; otherwise,
  * [divide] split the input list into two balanced halves, i.e. containing almost the same number of items each;
  * [conquer] run the merge sort algorithm recursively on each of the halves obtained in the previous step;
  * [combine] merge the two ordered lists returned by the last step by using the algorithm merge and return the result.

  The last step uses an ancillary algorithm , called merge, that is responsible for combining two ordered input lists to return a new list that contains all the elements in the input lists ordered.


* Section 2 (understanding): [Solution](https://comp-think.github.io/exercises/understanding/advanced/exercise-27) available online.

* Section 3 (development): [Solution](https://comp-think.github.io/exercises/development/advanced/exercise-27) available online.
