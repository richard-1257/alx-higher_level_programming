
# Python - Network #1

This project involved learning how to use the `urllib` and `requests` Python libraries to send and receive HTTP messages to URL's. I practiced sending `GET` and `POST` requests, fetching JSON resources, and interacting with API's (the Star Wars API, GitHub API, and Twitter API).

## Tasks 📃
- 0. What's my status? #0
     - [0-hbtn_status.py](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x11-python-network_1/0-hbtn_status.py):  Python script that fetches `https://intranet.hbtn.io/status`.
     - Uses `urllib`.
     
- 1. Response header value #0
     - [1-hbtn_header.py](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x11-python-network_1/1-hbtn_header.py): Python script that displays the `X-Request-Id` response header variable of a request to a given URL.
     - Usage: `./1-hbtn_header.py <URL>`
       - Uses `urllib.`
     
- 2. POST an email #0
     - [2-post_email.py](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x11-python-network_1/2-post_email.py): Python script that sends a POST request to a given URL with a given email, and displays the response body.
     - Usage: `./2-post_email.py <URL> <email>`
       - Uses `urllib`.

- 3. Error code #0
     - [3-error_code.py](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x11-python-network_1/3-error_code.py): Python script sends a request to a given URL and displays the response body.
     - Handles HTTP errors
       - Uses `urllib`.

- 4. What's my status? #1
     - [4-hbtn-status.py](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x11-python-network_1/4-hbtn_status.py): Python script that fetches `https://intranet.hbtn.io/status`.
     - Uses `requests`.
     
- 5. Response header value #1
     - [5-hbtn_header.py](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x11-python-network_1/5-hbtn_header.py): Python script that displays the `X-Request-Id` response header variable of a request to a given URL.
     - Usage: `./5-hbtn_header.py <URL>`
       - Uses `requests`.
     
- 6. POST an email #1
     - [6-post_email.py](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x11-python-network_1/6-post_email.py): Python script that sends a `POST` request to a given URL with a given email, and displays the response body.
     - Usage: `./6-post_email.py <URL> <email>`.
       - Uses `requests`.
     
- 7. Error code #1
     - [7-error_code.py](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x11-python-network_1/7-error_code.py): Python script sends a request to a given URL and displays the response body.
     - Handles HTTP errors
         - Uses `requests`.

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
<details><summary>Richard ifeanyi</summa
