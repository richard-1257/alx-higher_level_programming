
# Python - Object-relational mapping

In this project, I learned about how object-relational mapping is used for database scripting. I became familiar with using MySQLdb and SQLAlchemy to query, create, edit, and delete tables in MySQL.


## Tasks 📃
- 0. Get all states
     - [0-select_states.py](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/0-select_states.py):  Python script that uses MySQLdb to list all states in the database `hbtn_0e_0_usa`.
     - Usage: `./0-select_states.py <mysql username> <mysql password> <database name>`.
     - Results are ordered by ascending `states.id`.
     
- 1. Filter states
     - [1-filter_states.py](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/1-filter_states.py): Python script that uses MySQLdb to list all states with names starting with `N` in the database `hbtn_0e_0_usa`.
     - Usage: `./1-filter_states.py <mysql username> <mysql password> <database name>`.
     - Results are ordered by ascending `states.id`.
     
- 2. Filter states by user input
     - [2-my_filter_states.py](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/2-my_filter_states.py): Python script that uses MySQLdb to display all values matching a given name in the `states` table of the database `hbtn_0e_0_usa`.
     - Usage: `./2-my_filter_states.py <mysql username> <mysql password> <database name> <state name searched>`.
     - Results are ordered by ascending `states.id`.
     - Uses string formatting to construct the SQL query.

- 3. SQL Injection...
     - [3-my_safe_filter_states.py](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/3-my_safe_filter_states.py): Python script that uses MySQLdb to display all values matching a given name in the `states` table of the database `hbtn_0e_0_usa`.
     - Usage: `./3-my_safe_filter_states.py <mysql username> <mysql password> <database name> <state name searched>`.
     - Results are ordered by ascending `states.id`.
     - Safe from SQL injections.

- 4. Cities by states
     - [4-cities_by_state.py](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/4-cities_by_state.py): Python script that uses MySQLdb to list all cities from the database `hbtn_0e_4_usa`.
     - Usage: `./4-cities_by_state.py <mysql username> <mysql password> <database name>`.
     - Results are ordered by ascending `cities.id`.
     
- 5. All cities by state
     - [5-filter_cities.py](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/5-filter_cities.py): Python script that uses MySQLdb to list all cities of a given state in the database `hbtn_0e_4_usa`.
     - Usage: `./5-filter_cities.py <mysql username> <mysql password> <database name>`.
     - Results are sorted by ascending `cities.id`.
     
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
