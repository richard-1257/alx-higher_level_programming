# JavaScript - Warm up

This was the first JavaScript project I completed at ALX. Tasks involved writing various introductory-level JavaScript scripts on Node.js.

Function Prototypes 💾:

Prototypes for functions written in this project:

| File | Prototype |
| ---- | --------- |
| `13-add.js` | `exports.add = (a, b)` |
| `101-call_me_moby.js` |`function (x, theFunction)` |
| `102-add_me_maybe.js` | `function (number, theFunction)` |

## Tasks 📃
- 0. First constant, first print
     - [0-javascript_is_amazing.js](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x12-javascript-warm_up/0-javascript_is_amazing.js): JavaScript script that creates a constant variable `myVar` with the value `'Javascript is amazing'.` 
     - Usage: `./0-javascript_is_amazing.js`
     
- 1. 3 languages
     - [1-multi_languages.js](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x12-javascript-warm_up/1-multi_languages.js): JavaScript script that prints three lines.
     - Usage: `./1-multi_languages.js`
     - Line 1: `'C is fun'.`
     - Line 2: `'Python is cool'.`
     - Line 3: `'Javascript is amazing'.`
     
- 2. Arguments
     - [2-arguments.js](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x12-javascript-warm_up/2-arguments.js): JavaScript script that prints a message depending on the number of arguments passed.
     - Usage: `./2-arguments.js <arg 1> <arg 2> ...`
     - If no arguments are passed, prints `'No argument'.`
     - If one argument is passed, prints `'Argument found'.`
     - Otherwise, prints `'Arguments found'.`

- 3. Value of my argument
     - [3-value_argument.js](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x12-javascript-warm_up/3-value_argument.js): JavaScript script that prints the first argument passed to it.
     - Usage: `./3-value_argument.js <arg>`
     - If no argument is passed, prints `'No argument'.`

- 4. Create a sentence
     - [4-concat.js](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x12-javascript-warm_up/4-concat.js): JavaScript script that prints two arguments passed in the format `<arg 1> is <arg 2>.`
     - Usage: `./4-concat.js <arg1> <arg2>`
     
- 5. An Integer
     - [5-to_integer.js](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x12-javascript-warm_up/5-to_integer.js): JavaScript script that prints `My number: <first argument converted in integer>` if the first pased argument can be converted to an integer.
     - Usage: `./5-to_integer.js`
     - If the argument cannot be converted to an integer, prints `'Not a number'`.
     
- 6. Counting sort
     - [102-counting_sort.c](https://github.com/richard-1257/sorting_algorithms/blob/master/102-counting_sort.c): C function that sorts an array of integers in ascending order using the Counting Sort algorithm.
     - Assumes that the array will only contain numbers `>= 0`.
     - Prints the counting array after it has been initialized.
     - [102-O](https://github.com/richard-1257/sorting_algorithms/blob/master/102-O): Text file containing the best, average, and worst case time complexities of the Counting Sort algorithm, one per line.
     
- 7. Merge sort
     - [103-merge_sort.c](https://github.com/richard-1257/sorting_algorithms/blob/master/103-merge_sort.c): C function that sorts an array of integers in ascending order using the Merge Sort algorithm.
     - Implements the `top-down` Merge Sort algorithm
         - When an array is divided, the size of the left subarray is always less than or equal to the size of the right subarray.
         - Always sorts the left subarray before the right one.
     - Prints subarrays each time they are merged.
     - [103-O](https://github.com/richard-1257/sorting_algorithms/blob/master/103-O): Text file containing the best, average, and worst case time complexities of the Merge Sort algorithm, one per line.

- 8. Heap sort
     - [104-heap_sort.c](https://github.com/richard-1257/sorting_algorithms/blob/master/104-heap_sort.c): C function that sorts an array of integers in ascending order using the Heap Sort algorithm.
     - Implements the `sift-down` Heap Sort algorithm.
     - Prints the array after each swap.
     - [104-O](https://github.com/richard-1257/sorting_algorithms/blob/master/104-O): Text file containing the best, average, and worst case time complexiites of the Heap Sort algorithm, one per line.
     
- 9. Radix sort
     -[105-radix_sort.c](https://github.com/richard-1257/sorting_algorithms/blob/master/105-radix_sort.c): C function that sorts an array of integers in ascending order using the Radix Sort algorithm.
     - Implements the Least-Significant-Digit (LSD) Radix Sort algorithm.
     - Assumes that the array will only contain numbers `>= 0`.
     - Prints the array for each significant digit increase.
     - [105-O](https://github.com/richard-1257/sorting_algorithms/blob/master/105-O): Text file containing the best, average, and worst case time complexities of the Radix Sort algorithm, one per line.
     
- 10. Bitonic sort
      - [106-bitonic_sort.c](https://github.com/richard-1257/sorting_algorithms/blob/master/106-bitonic_sort.c):  C function that sorts an array of integers in ascending order using the Bitonic Sort algorithm.
      - Assumes that `size` is a power of 2 (ie. `size` can be expressed as `2^k` where `k >= 0`).
      - Prints subarrays each time they are merged.
      - [106-O](https://github.com/richard-1257/sorting_algorithms/blob/master/106-O): Text file containing the best, average, and worst case time complexities of the Bitonic Sort algorithm, one per line.
      
- 11. Quick Sort - Hoare Partition scheme
      - [107-quick_sort_hoare.c](https://github.com/richard-1257/sorting_algorithms/blob/master/107-quick_sort_hoare.c): C function that sorts an array of integers in ascending order using the Quick Sort algorithm.
      - Implements the Hoare partition scheme.
      - Always uses the last elemement of the partition being sorted as the pivot.
      - Prints the array after each swap.
      - [107-O](https://github.com/richard-1257/sorting_algorithms/blob/master/107-O): Text file containing the best, average, and worst case time complexities of the Quick Sort Hoare Partition cheme algorithm, one per line.
      
- 12. Dealer
      - [1000-sort_deck.c](https://github.com/richard-1257/sorting_algorithms/blob/master/1000-sort_deck.c): C function that sorts a `deck_node_t` doubly-linked list deck of cards.
      - Assumes that there are exactly 52 elements in the doubly-linked list.
      - Orders the deck from spades to diamonds and from aces to kings.
      
# Authors
<details><summary>Richard ifeanyi</summary>
