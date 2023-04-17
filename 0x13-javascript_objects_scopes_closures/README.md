# JavaScript - Objects, Scopes and Closures

In this second ALX JavaScript project I dived into the infamously fun aspects of the language - scope, closures and this. I practiced working with objects and ES6-style classes.


Function Prototypes💾 :
Prototypes for functions written in this project:

| File | Prototype |
| ---- | --------- |
| `7-occurrences.js` | `exports.nbOccurences = function (list, searchElement)` |
| `8-esrever.js` |`exports.esrever = function (list)` |
| `9-logme.js` | `exports.logMe = function (item)` |
| `10-converter.js` | `exports.converter = function (base)` |


## Tasks 📃
- 0. Rectangle #0
     - [0-rectangle.js](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/0-rectangle.js): JavaScript script that defines an empty class `Rectangle.`
     
- 1. Rectangle #1
     - [1-rectangle.js](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/1-rectangle.js): JavaScript script that defines a class Rectangle. Builds on [0-rectangle.js](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/0-rectangle.js) with:
     - Constructor that initializes instance attributes `width` and `height` with given parameters `w` and `h.`
     
- 2. Rectangle #2
     - [2-rectangle.js](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/2-rectangle.js): JavaScript script that defines a class Rectangle. Builds on [1-rectangle.js](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/1-rectangle.js) with:
     - If provided `w` and `h` are less than or equal to `0`, creates an empty object.

- 3. Rectangle #3
     - [3-rectangle.js](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/3-rectangle.js): JavaScript script that defines a class Rectangle. Builds on [3-rectangle.js](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/3-rectangle.js) with:
     - Instance method print() that `prints` the rectangle using the `X` character.

- 4. Rectangle #4
     - [4-rectangle.js](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/4-rectangle.js): JavaScript script that defines a class Rectangle. Builds on [4-rectangle.js](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/4-rectangle.js) with:
     - Instance method `rotate()` that swaps the `width` and `height` of the `Rectangle.`
     - Instance method `double()` that multiplies the `width` and `height` of the `Rectangle` by `2.`
     
- 5. Cocktail shaker sort
     - [101-cocktail_sort_list.c](https://github.com/richard-1257/sorting_algorithms/blob/master/101-cocktail_sort_list.c): C function that sorts a `listint_t` doubly-linked list of integers in ascending order using the Cocktail Shaker Sort algorithm.
     - Prints the list after each swap.
     - [101-O](https://github.com/richard-1257/sorting_algorithms/blob/master/101-O): Text file containing the best, average, and worst case time complexities of the Cocktail Shaker Sort algorithm, one per line.
     
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
