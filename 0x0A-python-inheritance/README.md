
# 0x0A. Python - Inheritance

In this project, I learned about Python class inheritance. I learned about the differences between super- and sub-classes while practicing inheritance, definining classes with multiple base classes, and overiding inherited methods and attributes.

## Tests 🧪

- [tests](https://github.com/richard-1257/alx-higher_level_programming/tree/master/0x0A-python-inheritance/test): Folder of test files provided by ALX, as well as the following two independently-developed:
  - [1-my_list.txt](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x0A-python-inheritance/test/1-my_list.txt)
  - [7-base_geometry.txt](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x0A-python-inheritance/test/7-base_geometry.txt)

## Function Prototypes 💾
Prototypes for functions written in this project:
| File | Prototype |
| ---- | --------- |
| `0-lookup.py` | `def lookup(obj):` |
| `2-is_same_class.py` |`def is_same_class(obj, a_class):` |
| `3-is_kind_of_class.py` | `def is_kind_of_class(obj, a_class):` |
| `4-inherits_from.py` | `def inherits_from(obj, a_class):` |
| `101-add_attribute.py` | `def add_attribute(obj, att, value):` |


## Tasks 📃
- 0. Lookup
     - [0-lookup.py](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x0A-python-inheritance/0-lookup.py):  Python function that returns a list of available attributes and methods of an objects.
     
- 1. My list
     - [1-my_list.py](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x0A-python-inheritance/1-my_list.py): Python class `MyList` that inherits from `list.` Includes:
       - Public instance method `def print_sorted(self):` that prints the list in ascending sorted order (assumes all list elements are `int`s).
     
- 2. Exact same object
     - [2-is_same_class.py](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x0A-python-inheritance/2-is_same_class.py): Python function that returns `True` if an object is exactly an instance of a specified class; otherwise `False.`

- 3. Quick sort
     - [3-quick_sort.c](https://github.com/richard-1257/sorting_algorithms/blob/master/3-quick_sort.c): C function that sorts an array of integers in ascending order using the Quick Sort algorithm.
     - Implements the Lomuto partition scheme.
     - Always uses the last element of the partition being sorted as the pivot.
     - Prints the array after each swap.
     -[3-O](https://github.com/richard-1257/sorting_algorithms/blob/master/3-O): Text file containing the best, average, and worst case time complexities of the Quick Sort Lomuto Partition scheme algorithm, one per line.

- 4. Shell sort - Knuth Sequence
     - [100-shell_sort.c](https://github.com/richard-1257/sorting_algorithms/blob/master/100-shell_sort.c): C function that sorts an array of integers in ascending order using the Shell sort algorithm.
     - Implements the Knuth interval sequence.
     - Prints the array each time the interval is decreased.
     
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
