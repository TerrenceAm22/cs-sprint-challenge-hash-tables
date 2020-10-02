Hashing Functions
is any function that can be used to map data of arbitrary size to fixed-size values.
Collision resolution
Linear probing is iterating through the table looking for the next available slot.


Performance of basic hash table operations
Most of the operations are constant lookup.  but they could be O(n) due to instances where the same elements are hashed to same key.

Load factor
The Load factor is a measure that decides when to increase the HashMap capacity to maintain the get() and put() operation complexity of O(1).

Automatic resizing
 load factor exceeds some threshold 

Various use cases for hash tables
Password Verification
Solving the ceasar cipher

