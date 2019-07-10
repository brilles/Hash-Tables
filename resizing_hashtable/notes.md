HT collisions are when two keys hash to the same value

- collisions are unavoidable
- using LL Chaining to avoid the collisions
- elements in the hash table are stored as LL
- when retrieving a value, we traverse dow the LL until the matching key is found
- if Null -> the end of the list has been found
- 2 options LL or not
- if LL, each node in the LL needs to be traversed to check if the key matches
- if null, then place it (for insertion)
- if there is a match then we want to overwrite
- O(n) for LL
- degrade from constant to linear
- load factor is (number of entries) / (hash table capacity)
- when the LF passes a certain threshold, resizing can occur
