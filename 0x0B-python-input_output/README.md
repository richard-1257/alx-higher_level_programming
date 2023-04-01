
# Python - Input/Output

In this project, I practiced file handling in Python. I used the builtin `with,` `open,` and `read` functions with the `json` module to read and write files and serialize and deserialize objects with JSON.

Function Prototypes:
Prototypes for functions written in this project:
| File | Prototype |
| ---- | --------- |
| `0-read_file.py` | `def read_file(filename=""):` |
| `1-number_of_lines.py` |`def number_of_lines(filename=""):` |
| `2-read_lines.py` | `def read_lines(filename="", nb_lines=0):` |
| `3-write_file.py` | `def write_file(filename="", text=""):` |
| `4-append_write.py` | `def append_write(filename="", text=""):` |
| `5-to_json_string.py` | `def to_json_string(my_obj):` |
| `6-from_json_string.py` | `def from_json_string(my_str):` |
| `7-save_to_json_file.py` | `def save_to_json_file(my_obj, filename):` |
| `8-load_from_json_file.py` | `def load_from_json_file(filename):` |
| `10-class_to_json.py` | `def class_to_json(obj):` |
| `14-pascal_triangle.py` | `def pascal_triangle(n):` |
| `100-append_after.py` | `def append_after(filename="", search_string="", new_string=""):` |

## Tasks 📃
- 0. Read file
     - [0-read_file.py](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x0B-python-input_output/0-read_file.py):  Python function that prints the contents of a UTF8 text file to standard output.
     
- 1. Write to a file
     - [1-write_file.py](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x0B-python-input_output/1-write_file.py): Python function that writes a string to a UTF8 text file and returns the number of characters written.
     
- 2. Selection sort
     - [2-selection_sort.c](https://github.com/richard-1257/sorting_algorithms/blob/master/2-selection_sort.c): C function that sorts an array of integers in ascending order using the Selection Sort algorithm.
     - Prints the array after each swap.
     - [2-O](https://github.com/richard-1257/sorting_algorithms/blob/master/2-O): Text file containing the best, average, and worst case time complexities of the Selection Sort algorithm, one per line.

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
